# Program to find if a student is passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects ad take marks as an input from the user.

marks1=int(input("Enter the marks of English: "))
marks2=int(input("Enter the marks of Math: "))
marks3=int(input("Enter the marks of Science: "))

sum=marks1+marks2+marks3

percentage=(sum*100)/300

if(percentage>40 and marks1>33 and marks2>33 and marks3>33):
    print("Passed",percentage)

else:
    print("Failed",percentage)

