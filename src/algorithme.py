import sys, json

# Algorithme de mariage stable de Gale & Shapley
# @param data : studients and institutions preferences (id, liste de préférences)
def galeShapley(data):
    libre = [k for k in data['students'].keys()]
    
    prochain = {}
    for s in data['students']:
        prochain[s] = 0
    
    affectation = {}
    for i in data['institutions']:
        affectation[i] = []
    
    while len(libre) > 0:
        s = libre[0]
        k1 = data['students']
        k2 = k1[s]
        k3 = prochain[s]
        k4 = k2[k3]
        i = k4

        # i = data['students'][s][prochain[s]]

        if (len(affectation[i]) < int(data['institutions'][i]['capacities'])):
            affectation[i].append(s)
            libre.remove(s)
        else:
            pire_s = affectation[i][0]
            for x in affectation[i]:
                if data['institutions'][i]['preferences'].index(x) > data['institutions'][i]['preferences'].index(pire_s):
                    pire_s = x

            if (data['institutions'][i]['preferences'].index(s) < data['institutions'][i]['preferences'].index(pire_s)):
                affectation[i].remove(pire_s)
                affectation[i].append(s)
                libre.append(pire_s)
                libre.remove(s)

        prochain[s] += 1
    return affectation



def galeShapley2(data):
    libreI = [k for k in data['institutions'].keys()]
    prochainE = {}
    #dejAffect = {}
    for insti in data['institutions'].keys():
        prochainE[insti] = 0
        #dejAffect[insti] = 0
    affectation = {}
    for i in data['institutions']:
        affectation[i] = []

    while len(libreI) > 0 :
        i = libreI[0] 
        while (data['institutions'][i]['capacities'] - len(affectation[i])) > 0: 
            if (len(data['institutions'][i]['preferences']) > prochainE[i]) : 
                e = data['institutions'][i]['preferences'][prochainE[i]]
                acctuI = ""
                for inst in affectation:
                    if e in affectation[inst] : 
                        acctuI = inst
                if acctuI != "":
                    if (data['students'][e].index(i) < data['students'][e].index(acctuI)):
                        affectation[acctuI].remove(e)
                        affectation[i].append(e)
                        libreI.append(acctuI)
                else : 
                    affectation[i].append(e)
                prochainE[i] += 1
        
        libreI.remove(i)

    return affectation





# print the affectation in a human-readable format
def printAffectation(affectation):
    for i in affectation:
        print("Institution " + i + " : " + str(affectation[i]))

# calculate satisfaction of the affectation
def satisfaction(affectation, data):
    s = 0
    return s