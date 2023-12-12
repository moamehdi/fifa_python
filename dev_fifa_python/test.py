

fileData = "FIFA_World_Cup/FIFA-2022.txt";
fileResult = "FIFA_World_Cup/results.txt";

column = str(input("quelle column"))

i=0
columnindex = 0



file1 = open(fileData, "r")
file2 = open(fileResult, "w")

for line in file1 :
    texte=line.split(",")
    for word in texte:
        i+=1
        if word == column:
            columnindex = i

        if i == columnindex:
            continue
        else:
            if i == 0:
                continue
            else:
                print(i)
                file2.write(word + ",")

