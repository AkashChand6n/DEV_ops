person = {"first_name": "John", "last_name": "Doe", "age": 30,
          "hobbies":["reading","travelling","coding"],
          "skill":{"python": "advance","java": "intermediate"}}
person["address"]="kerala"
print(person)
print(len(person))
print(person.get("skill"))

# #implimentation of sort in dictionary
# #sort by bubble sort

# print("address" in person) #check if key is present in dictionary
# print("address" in person.keys()) #check if key is present in dictionary

# print(person.pop("address")) #remove key value pair from dictionary
# print(len(person))

# del person["hobbies"] #remove key value pair from dictionary
# print(len(person))

# person["skill"]["figma"].append = "intermediate"

person_copy=person.copy()
del person
# print(person_copy.keys())

keys = person_copy.keys()
for i in keys:
    print(person_copy[i],"\n")

