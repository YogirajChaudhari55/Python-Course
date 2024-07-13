#What will be the length of this set
#My answer is 2 because 20 and 20.0 are same in terms of python
s=set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))