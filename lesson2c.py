# python dictionary
person = {

"first name" : "john",
"lastname" : "doe",
"age" : 25 ,
"colors" : ["blue" , " green"],
"salary" : 5000 ,
}
# show output
print(person)
# print age
print(person["age"])
# print salary
print(person["salary"])
# add new key valeu 
person["passport"]="b008hn"
# show out put 
print(person)
# change age to 34 
person["age"]=34
# show output 
print(person)
# delete last name 
del person["lastname"]
# show output 
print(person)