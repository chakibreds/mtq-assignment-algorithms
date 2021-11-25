import sys,random,json
import time
import numpy as np

# @param n nb students
# @param k nb institutions
def generate_capacities(n, k):
    totals = np.array([n])

    a = np.random.random((k, 1))  # create random numbers
    a = a/np.sum(a, axis=0) * totals  # force them to sum to totals

    # Ignore the following if you don't need integers
    a = np.round(a)  # transform them into integers
    remainings = totals - np.sum(a, axis=0)  # check if there are corrections to be done
    for j, r in enumerate(remainings):  # implement the correction
        step = 1 if r > 0 else -1
        while r != 0:
            i = np.random.randint(6)
            if a[i,j] + step >= 0:
                a[i, j] += step
                r -= step
    result = np.concatenate(a).ravel().tolist()
    return [int(i) for i in result]

# Generate preferences of the students and institutions
# @param n: number of students
# @param k: number of institutions
# @param rand_capacities: if True, capacities are randomly generated
def generate_pref(n,k,rand_capacities=True): 
    dict_stud={}
    dict_univ={}

    if rand_capacities:
        capacities = generate_capacities(n, k)
    else:
        capacities = [round(int(n/k)) + 1 for i in range(k)]

    for i in range(k):
        dict_univ["I"+str(i+1)]= {'capacities': capacities[i], 'preferences' : []}


    # students preferences
    i = 1
    while (i<=n): 
        dict_stud["E"+str(i)] = []
        inst = list(dict_univ.keys())

        while len(inst) > 0:
            choice = random.choice(inst)
            inst.remove(choice)
            dict_stud["E"+str(i)].append(choice)
        i+=1
    # institutions preferences
    i = 1
    while(i<=k):
        students = list(dict_stud.keys())
        while len(students) > 0:
            choice = random.choice(students)
            students.remove(choice)
            dict_univ["I"+str(i)]['preferences'].append(choice)
        i+=1
    
    return dict_stud,dict_univ

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} nb_students nb_institutions path/to/file.json")
        exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    file_name = sys.argv[3]
    start = time.time()
    dict_stud, dict_univ = generate_pref(n,k,rand_capacities=True)
    end = time.time()

    print(f"Generation des préferences en {round(start-end,2)} secondes.")

    with open(file_name, 'w') as outfile:
        start = time.time()
        json.dump({'students' : dict_stud, 'institutions':dict_univ}, outfile)
        end = time.time()
    
    print(f"File '{file_name}' generated.\ntime = {round(start-end,2)} secondes.")

