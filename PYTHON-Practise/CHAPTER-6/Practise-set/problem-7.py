#Program to find out whether a given post is talking about "harry" or not

post="Harry bhai kya baat karte ho"

if("Harry".lower() in post.lower()):
    print("Post is talking about harry bhai")
else:
    print("Not talking")