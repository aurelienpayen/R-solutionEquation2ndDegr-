from math import *

def eq_sec_deg(a,b,c):
    delta = b**2-4*a*c
    if delta > 0:
        texte = "Les deux solutions de x sont: X1= " +str (-b + sqrt(delta)/2*a) + " et X2= " + str (-b - sqrt(delta)/2*a)
    elif delta == 0:
        texte = "L'unique solution de l'équation est: X0= " + str (-b/2*a)
    elif delta < 0:
        texte = "Il n'y a pas solution pour cette équation proposée."
    print (texte)
        
    
    
eq_sec_deg(1,2,1)
