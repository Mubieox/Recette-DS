Dessert={"gateau chocolat":["chocolat","oeuf","farine","sucre","beurre"],
         "gateau yaourt":["yaourt","oeuf","farine","sucre"],
         "crepes":["oeuf","farine","lait"],
         "quatre-quarts":["oeuf","farine","beurre","sucre"],
         "kouignamann":["farine","beurre","sucre"]}

def nb_ingredients(D,r):
    if r in D.keys():
        return len(D[r])
    
print(nb_ingredients(Dessert,"gateau chocolat"))

def recette_avec(D,i):
    lr=[]
    for r,li in D.items():
        if i in li:
            lr.append(r)
    return lr

print(recette_avec(Dessert,"levure"))

def tous_ingredients(D):
    ei=[]
    for li in D.values():
        for i in li:
            if i not in ei:
                ei.append(i)
    return ei

print(tous_ingredients(Dessert))

def ingredient_principal(D):
    nbi={}
    for i in tous_ingredients(Dessert):
        nbi[i]=0
    for li in D.values():
        for i in li:
            nbi[i]+=1
    max=0
    ip=""
    for i,nb in nbi.items():
        if nb>max:
            max=nb
            ip=i
    return ip


print(ingredient_principal(Dessert))

def table_ingredient(D):
    ti={}
    for i in tous_ingredients(Dessert):
        ti[i]=[]
    for r,li in D.items():
        for i in li:
            ti[i].append(r)
    return ti

print(table_ingredient(Dessert))

def recette_sans(D,i):
    nlr={}
    for r,li in D.items():
        if i not in li:
            nlr[r]=li
    return nlr

print(recette_sans(Dessert,"beurre"))