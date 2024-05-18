#slicing = creatuing a substring by extracting elements from another astring
#           indexing[] or slice()
#           [start:stop:step]

name = "You Know Me"

first_name = name[0:3:]
First_name = name[:3]

last_name = name[9:11]

New_name =name[0:11:2]
new_name = name[::2]

reversed_name = name[::-1]

print(reversed_name)
print(new_name)
print(New_name)

website1 = "http://google.com"
website2 = "http://AlldogsGotoheaven.com"

#positive and negitive indexing
slice = slice(7, -4)

print(website1[slice])
print(website2[slice])

#slice was created in a way that would capture ANY website name, indepedant of length
