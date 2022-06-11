#!/usr/bin/env python
# coding: utf-8

# In[ ]:


mot_de_passe =""
while not mot_de_passe == "jojo":
    mot_de_passe=input("quel est le mot de passe ?")

c = "john"
a=13
b=2
print("Bonjour je m'appelle " + c +" j'ai "+ str(a*b)+ " ans.")

def demander_nom():
    d=""
    while d=="":
        d=input("et toi comment tu t'appelle? ")
    return d
def demander_age ():
    age = 0
    while age == 0:
        age_ = input("quel est votre age ? ")
        try:
            age = int(age_)
        except:
            print("erreur: vous devez rentrer un nombre pour l'age")
    return age
m = demander_nom()
k=demander_age()

print("bien venue " + m + " vous avez " + str(k) + " ans.")
print("l'an prochain vous aurez " + str(k+1) + " ans.")


# In[ ]:




