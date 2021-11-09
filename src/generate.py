import sys,os,random

#k == n2 si on veut avoir n2 choix pour les étudiants sachant que n2 == nb etablissments 
def generate_stu(n,k,file_path): 
    dict_stud={}
    dict_univ={}
    f = open(file_path,"w")
    f.write(str(n)+"\n")
    f.write(str(k)+"\n")
    i = 1
    while (i<=n): 
        dict_stud["E"+str(i)] = []
        f.write("E"+str(i))
        j = 1 
        while (j<=k):
            choice = "I"+str(random.randrange(1,k+1,1))
            if choice not in dict_stud["E"+str(i)]: 
                dict_stud["E"+str(i)].append(choice)
                f.write(";"+choice)
                j+=1
        i+=1
        f.write("\n")

    i = 1 
    while(i<=k):
        dict_univ["I"+str(i)] = []
        f.write("I"+str(i))
        j = 1 
        while (j<=n):
            choice = "E"+str(random.randrange(1,n+1,1))
            if choice not in dict_univ["I"+str(i)]: 
                dict_univ["I"+str(i)].append(choice)
                f.write(";"+choice)
                j+=1
        i+=1
        f.write("\n")
    f.close()
    return dict_stud





if __name__ == "__main__":
    dict_stud = generate_stu(5,5,"test.txt")
    print(dict_stud)

