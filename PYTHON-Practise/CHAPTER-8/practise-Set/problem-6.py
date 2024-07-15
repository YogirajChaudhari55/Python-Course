#Python function which converts inches to cms

#1 inches = 2.54 cms

n=float(input("Enter the inches to convert in cms: "))

def inches_to_cms(n):
    cms = 2.54 * n
    return cms

print(inches_to_cms(n))