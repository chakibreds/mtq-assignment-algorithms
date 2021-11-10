import sys,random,json

# Generate preferences of the students and institutions
# @param n: number of students
# @param k: number of institutions
def generate_pref(n,k,file_path): 
    dict_stud={}
    dict_univ={}
   
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
        dict_univ["I"+str(i)] = []
        j = 1 
        while (j<=n):
            choice = "E"+str(random.randrange(1,n+1,1))
            if choice not in dict_univ["I"+str(i)]: 
                dict_univ["I"+str(i)].append(choice)
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
    dict_stud, dict_univ = generate_pref(n,k,file_name)
    with open(file_name, 'w') as outfile:
        json.dump({'students' : dict_stud, 'institutions':dict_univ}, outfile)
    
    print(f"File {file_name} generated.")

