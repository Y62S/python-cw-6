# write your code here
person = {
    "name" : "yousef",
    "age" : 16,
    "hobbies" : ["martial arts" , "shooting", "riding"]

}
print(person["name"])
print(person["age"])
person["age"] = 17
person["country"] = "kuwait"
print(person)
print(f"number of objects in dictionary: {len((person))}")
person["hobbies"].append("coding")

def check_hobbies(person):
    if len(person["hobbies"]) >= 3:
         return print("wow you are amazing!")
    else:
         return print("keep exploring your hobbies!")
check_hobbies(person)   
