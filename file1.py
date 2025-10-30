#import json
#a=0
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
##for i in range(1000000):
   # print (data[a]['title'])
   # a +=1

import json
a=0
data = json.load(open("./movies.json", encoding="utf8"))
movies = open("./movies.json", encoding="utf8")
year = input("After what year would you want your movies to be displayed? ")
for i in data(a):
 print (data[a]['year'])
 