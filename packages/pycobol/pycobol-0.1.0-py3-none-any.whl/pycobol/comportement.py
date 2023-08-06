from dataclasses import dataclass, field
from decimal import *
import re
#######################
####  Comportement ####
#######################

@dataclass
class Comportement():
    ''' Permet de cadrer les variables de type ALN et NUM
    
    :param type_:  str
    :param longueur: int
    :param valeur: str

    >>> obj = Comportement('ALN' , 10 , None)
    >>> obj.initialize()
    >>> obj.valeur_externe
    '          '
    >>> obj = Comportement('ALN' , 10 , 'eric' )
    >>> obj.initialize()
    >>> obj.valeur_externe
    'eric      '
    >>> len(obj.valeur_externe)
    10
    >>> obj = Comportement('NUM' , 10 , None )
    >>> obj.initialize()
    >>> obj.valeur_externe
    '0000000000'
    >>> obj = Comportement('NUM' , 10 , 50 )
    >>> obj.initialize()
    >>> obj.valeur_externe
    '0000000050'
    >>> len(obj.valeur_externe)
    10
    >>> obj = Comportement('SNUM' , 10 , None )
    >>> obj.initialize()
    >>> obj.valeur_externe
    '+0000000000'
    >>> obj = Comportement('SNUM' , 10 , -50 )
    >>> obj.initialize()
    >>> obj.valeur_externe
    '-0000000050'
    >>> len(obj.valeur_externe)
    11
    '''    
    type_: str
    longueur: int
    valeur: str

    def __post_init__(self):
        #print(self)
        if self.type_ in ['ALN', 'ALP', 'GRP'] :
            self.padding = ' '
            self.direction = 'left'
            self.defaut =''
        else:    
            self.padding = '0'
            self.direction = 'right'
            self.defaut = 0
            
                

    def initialize(self):
        ''' charge les zones en fonction de leur nature'''
        self.valeur_externe = None 
        if self.valeur == None :
            self.valeur_externe = self.padding * self.longueur
            self.valeur = self.defaut

            if self.type_[0] == 'S' and self.valeur >= 0:
                self.valeur_externe = '+' + self.valeur_externe  
        else: 
            if self.direction == 'left':
                self.valeur = str(self.valeur)
                lg_ = len(self.valeur)
                chaine = self.valeur
                if lg_ > self.longueur:
                    chaine = self.valeur[:self.longueur]
                self.valeur_externe = str(chaine).ljust(self.longueur,self.padding)
            else:
               # print('STOP4', self)
                self.valeur_externe = str(abs(self.valeur)).rjust(self.longueur,self.padding) 
                if self.type_[0] == 'S' and self.valeur < 0:
                     self.valeur_externe = '-' + self.valeur_externe
                elif self.type_[0] == 'S' and self.valeur >= 0:
                     self.valeur_externe = '+' + self.valeur_externe  
    

    def move_value(self,objetzone,  newvaleur):
        ''' methode pour affecter une valeur à une zone
            L'objet comportement est dejà instancié il connait la valeur de départ
            
            :param newvaleur:  Nouvelle valeur a affecter (int ou str)
         '''
        if self.direction == 'left' :
            newvaleur = str(newvaleur) 
            lg_ = len(newvaleur)      
            if lg_ > self.longueur:
                lg_ = self.longueur 
            else:
                newvaleur= newvaleur.ljust(self.longueur,self.padding)   
                lg_ = len(newvaleur)
            objetzone.valeur_externe = newvaleur[:lg_] 
            objetzone.interne = objetzone.valeur_externe   
        else:
            if objetzone.valeur_externe[0] == '+' or objetzone.valeur_externe[0] == '-':
                objetzone.valeur_externe = objetzone.valeur_externe[1:]
            try :
                lg_ = len(str(abs(newvaleur)))
                _valeur = str(abs(newvaleur))
                # la zone n est pas numerique
                # est elle numerique ?
            except: 
                try: 
                    newvaleur = int(newvaleur)
                    lg_ = len(str(abs(newvaleur)))
                    _valeur =  str(abs(newvaleur))
                # warning int ou float ? TODO
                except:
                    lg_ = len(newvaleur)
                    _valeur = newvaleur
                    ### c est de l'alpha

            if lg_ > self.longueur :
                lg_ =lg_ - self.longueur
            else:
                lg_ = 0     
            objetzone.valeur_externe = _valeur[lg_:].rjust(self.longueur,self.padding) 
                    
            if self.type_[0] == 'S' and newvaleur < 0:
                     objetzone.valeur_externe = '-' + objetzone.valeur_externe
            elif self.type_[0] == 'S' and newvaleur >= 0:
                     objetzone.valeur_externe = '+' + objetzone.valeur_externe
            try: 
                objetzone.valeur_interne = int(objetzone.valeur_externe)                  
            except: 
                objetzone.valeur_interne = objetzone.valeur_externe
                
    @classmethod
    def from_object(cls, obj ):
        ''' Methode de classe retournant un objet comportement à partir d'une instance de zone

            :param: zone : objet zonage
        '''   
        return cls(obj.son_type , obj.longueur_utile, obj.valeur_initialisation)

############################
####  ComportementFloat ####
############################  

class ComportementFloat(Comportement):

    @classmethod
    def from_object(cls, obj ):
        ''' Methode de classe retournant un objet comportement à partir d'une instance de zone
            :param: zone  objet zonage
        '''   
        return cls(obj.decimale, obj.son_type , obj.longueur_utile, obj.valeur_initialisation)

    def __init__(self,decimale, *args ):
         self.decimale = decimale
         super().__init__(*args)
         self.padding = '0'
         self.direction = 'right'
         self.defaut = 0
         self.valeur_externe ='0'
         self.valeur_interne =0.



    def initialize(self):
        longueur_entier = self.longueur - self.decimale
        if self.valeur == None :
            longueur_entier = self.longueur - self.decimale
            decimale_str = self.padding  *  self.decimale
            longueur_entier_str =  self.padding  *  longueur_entier
            self.valeur_externe = longueur_entier_str + ',' +  decimale_str
            self.valeur_interne = float(self.defaut)
        else:
            value_str = abs(self.valeur)
            value_str = str(value_str)
            tb_ = []
            if '.' in value_str :
                tb_ = value_str.split('.')
                tb_[1] = tb_[1].ljust(2, '0')
                if len(tb_[1]) > self.decimale:
                    lg_ = len(tb_[1])  - self.decimale 
                    tb_[1] = tb_[1][lg_:]
            else:
                tb_.append(value_str)
                tb_.append( '0' * self.decimale)
            tb_[0] = tb_[0].rjust(longueur_entier,'0')
            if len(tb_[0]) > longueur_entier:
                lg_ = len(tb_[0])  - longueur_entier 
                tb_[0] = tb_[0][lg_:]

            self.valeur_externe = tb_[0] + ',' + tb_[1]
            str_ = self.valeur_externe.replace(',', '.')
            self.valeur_interne = float(str_)
            if self.type_[0] == 'S' and self.valeur < 0:
                     self.valeur_externe = '-' + self.valeur_externe
                     self.valeur_interne = -1 * self.valeur_interne
            elif self.type_[0] == 'S' and self.valeur >= 0:
                     self.valeur_externe = '+' + self.valeur_externe  
    
    def move_value(self,objetzone,  newvaleur):
        ''' methode pour affecter une valeur à une zone
            L'objet comportement est dejà instancié il connait la valeur de départ
            :newvaleur: float ou int 
         '''
        longueur_entier = self.longueur - self.decimale
        newvaleur_str  = str(abs(newvaleur))
        tabl = objetzone.valeur_externe.split(',')
        newvl_ = []
        if '.' in newvaleur_str:
            newvl_ = newvaleur_str.split(',')
        else:
            newvl_.append(newvaleur_str)
            newvl_.append('0' * self.decimale)
        
        if tabl[0] == '+'  or  tabl[0] == '-':
            tabl[0] = tabl[0][1:]
        lg_ =   len(newvl_[0])  
        if lg_ > longueur_entier:
            lg_ = lg_ - longueur_entier
        else:
            lg_ = 0
        tabl[0] =  str(newvl_[0])[lg_:].rjust(longueur_entier,self.padding)   
        lg_ =   len(newvl_[1])  
        if lg_ > self.decimale:
            lg_ = lg_ - self.decimale
        else:
            lg_ = 0
        tabl[1] =  str(newvl_[1])[lg_:].rjust(self.decimale,self.padding)   
        objetzone.valeur_externe = tabl[0] + ',' + tabl[1]
        
  
                 
        if self.type_[0] == 'S' and newvaleur < 0:
                 objetzone.valeur_externe = '-' + objetzone.valeur_externe
        elif self.type_[0] == 'S' and newvaleur >= 0:
                 objetzone.valeur_externe = '+' + objetzone.valeur_externe
        str_v = objetzone.valeur_externe.replace(',', '.')
        objetzone.valeur_interne = float(str_v)           
################
####  Value ####
################    
@dataclass              
class Value():
        ''' Cette classe prend en charge les valeurs : type str ou numerique 
        presence d 'un signe , partie entiere ou decimale

        >>> obj = Value("eric")
        >>> obj.numerique
        False
        >>> obj = Value(1961)
        >>> obj.numerique
        True'''
        origine: str
        formate :str    = field(init = False)
        non_signe: str  = field(init = False)
        numerique: bool = field(init = False)
        def __post_init__(self):
            self.formate = self.origine
            origine_ = str(self.origine)
            if type(self.origine) == str:
               self.numerique = False 
            else: 
                self.numerique = True
                if '-' in origine_ or '+' in origine_ :
                    self.non_signe = False
                    if '-' in self.origine:
                        self.formate = self.formate.repplace('-', '')
                        self.signe ='-'
                    elif '-' in self.origine:
                        self.formate = self.formate.repplace('+', '')
                        self.signe ='+'        
                else:
                    self.non_signe = True
                if ',' in origine_:
                    self.formate = self.formate.replace(',' , '.')                             
                    tab_  = re.search(r'(\d+)\.(\d+)' , self.formate) 
                    self.entier = tab_[1]
                    self.decimale = tab_[2]
                    






if __name__ == '__main__':  
    import doctest          
    #doctest.run_docstring_examples(Comportement,None, verbose = 0)
    #doctest.run_docstring_examples(Value,None, verbose = 1)
    doctest.testmod()