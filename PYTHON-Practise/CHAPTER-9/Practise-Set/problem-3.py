# Program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files ina folder for  13-yrs old.

def generateTable(n):
    table =""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"

    with open(f"Table/table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)
