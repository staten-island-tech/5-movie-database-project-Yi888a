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
 
#import json
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
#afteryear = input("After what year would you want your movies to be displayed? ")
#for i in data:
   # if int(i['year']) > int(afteryear):
     # print (i['year'], i['title'])
#beforeyears = input ("Before what year would you want your movies to be displayed? ")
#for i in data:
      # if int(i['year']) < int(beforeyears):
        # print (i['year'], i['title'])

#import json
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
#duringyear = input("During what year do you want your movies to show?")
#for i in data:
  #  if int(i['year']) == int(duringyear):
       # print (i['year'], i['title'])

#import json
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
#searchmovie = input("What movie do you want to view data for? ")
#for i in data:
# if (i['title']) == searchmovie:
#  print (i['year'], i['title'], i['cast'], i['genres'], i['extract'])

#import json
#data = json.load(open("./movies.json", encoding="utf8"))
#movies = open("./movies.json", encoding="utf8")
#genresearch = input("What genre do you wish to view? ")
#for i in data: 
# if genresearch in i['genres']:
       # print(i['year'], i['title'], i['cast'], i['genres'])