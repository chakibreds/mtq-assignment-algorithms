import sys,random,json

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
        capacities = [int(n/k)+1]*k
    # students preferences
    i = 1
    while (i<=n): 
        dict_stud["E"+str(i)] = []
        j = 1 
        while (j<=k):
            choice = "I"+str(random.randrange(1,k+1,1))
            if choice not in dict_stud["E"+str(i)]: 
                dict_stud["E"+str(i)].append(choice)
                j+=1
        i+=1

    # institutions preferences
    i = 1 
    while(i<=k):
        dict_univ["I"+str(i)] = {'capacities': capacities[i-1], 'preferences' : []}
        j = 1 
        while (j<=n):
            choice = "E"+str(random.randrange(1,n+1,1))
            if choice not in dict_univ["I"+str(i)]['preferences']: 
                dict_univ["I"+str(i)]['preferences'].append(choice)
                j+=1
        i+=1
    return dict_stud,dict_univ

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} nb_students nb_institutions path/to/file.json")
        exit(1)

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    file_name = sys.argv[3]
    dict_stud, dict_univ = generate_pref(n,k,rand_capacities=True)
    with open(file_name, 'w') as outfile:
        json.dump({'students' : dict_stud, 'institutions':dict_univ}, outfile)
    
    print(f"File '{file_name}' generated.")

