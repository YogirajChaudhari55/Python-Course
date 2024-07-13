#program to greet all the persin names stored n a list and which starts with S
#i=["harry","Soham,"Sachin,"Rahul"]

l=["harry","Soham","Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Greetings {name}")