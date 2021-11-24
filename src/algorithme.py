import sys, json

# Algorithme de mariage stable de Gale & Shapley
# @param data : studients and institutions preferences (id, liste de préférences)
def galeShapleyStudents(data):
    libre = [k for k in data['students'].keys()]
    
    prochain = {}
    for s in data['students']:
        prochain[s] = 0
    
    affectation = {}
    for i in data['institutions']:
        affectation[i] = []
    
    while len(libre) > 0:
        s = libre[0]
        i = data['students'][s][prochain[s]]
        if int(data['institutions'][i]['capacities']) == 0 :
            prochain[s] += 1
            continue
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


def galeShapleyInstituts(data):
    libreI = [k for k in data['institutions'].keys()]
    prochainE = {}

    for insti in data['institutions'].keys():
        prochainE[insti] = 0

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
            else:
                break
        
        libreI.remove(i)

    return affectation

# print the affectation in a human-readable format
def printAffectation(affectation):
    print("Institutions : [Étudiants affectés]")
    for i in affectation:
        print("Institution " + i + " : " + str(affectation[i]))

# write affection in a json file
def writeAffectation(affectation, filename, format='json'):
    if (format == 'json'):
        with open(filename, 'w') as outfile:
            json.dump(affectation, outfile)
    elif (format == 'csv'):
        with open(filename, 'w') as outfile:
            for i in affectation:
                for s in affectation[i]:
                    outfile.write(s + ";" + i + "\n")
    else:
        print(f"Format '{format}' inconnu")

# draw graph from csv file using networkx
def drawGraph(filename):
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.read_edgelist(filename, delimiter=';', create_using=nx.Graph(), nodetype=str)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000, font_size=8)
    plt.show()


# calculate satisfaction of the affectation
def studentSatisfaction(affectation, data):
    s = 0
    nb_institutions = len(data['institutions'])
    for institution in affectation :
        for student in affectation[institution] :
            if nb_institutions == 1:
                s += 1
            else:
                s += 1 - (data['students'][student].index(institution) / (nb_institutions - 1))
    return round(s / len(data['students']), 2)

def institutionSatisfaction(affectation, data):
    sat = 0
    nb_students = len(data['students'])
    for institution in affectation :
        sat_inst = 0
        # calculer pour chaque institution la satisfaction de l'institut
        capacity = data['institutions'][institution]['capacities']
        if capacity == 0:
            sat_inst = 1
        else:
            for student in affectation[institution] :
                index = data['institutions'][institution]['preferences'].index(student)
                if nb_students > 2 * capacity:
                    if index < capacity:
                        sat_inst += 1
                    elif index < nb_students - capacity - 1:
                        pas = 1 / (nb_students - 2 * capacity - 1)
                        sat_inst += 1 - ((index - capacity + 1) * pas)
                else:
                    if index < capacity:
                        sat_inst += 1
            sat += sat_inst / capacity


    return round(sat / len(data['institutions']), 2)