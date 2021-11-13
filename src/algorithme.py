import sys, json

# Algorithme de mariage stable de Gale & Shapley
# @param data : studients and institutions prefrences (id, liste de préférences)
def GaleShapley(data):
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

