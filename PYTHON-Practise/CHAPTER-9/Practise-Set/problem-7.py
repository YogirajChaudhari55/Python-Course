#Program to find out the line number where python is present from que 6

with open("log.txt") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if('python' in line):
        print(f"Yes python is present, at Line no:{lineno}")
        break
    lineno+=1

