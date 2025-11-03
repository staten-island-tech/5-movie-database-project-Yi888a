#import json
#a=0
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
##for i in range(1000000):
   # print (data[a]['title'])
   # a +=1

#import json
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
#year = input("After what year would you want your movies to be displayed? ")
#for i in data:
# if int(i['year']) > int(year):
      # print (i['year'], i['title'])
 
import json
data = json.load(open("./movies.json", encoding="utf8"))
movies = open("./movies.json", encoding="utf8")
afteryear = input("After what year would you want your movies to be displayed? ")
beforeyears = input ("Before what year would you want your movies to be displayed? ")
for i in data:
    if int(i['year']) > int(afteryear):
      print (i['year'], i['title'])
      for i in data:
       if int(i['year']) < int(beforeyears):
         print (i['year'], i['title'])