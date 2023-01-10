dictionary = {
    "1": "C14",
    "2": 5,
    "3": [],
    "4": {},
    "5": 3,
    "6": {
        "name": "first_name",
        "average": {
            "1": 20,
            "2": 30,
            "height": []
        },
    },
    "7": "Thank you",
}


value = dict(name="Mr Sam", age=30)

group = {"name": "Mr Same",
         "age": 30,
         "skill": {
             "soft": {},
             "tech": {},
         }
         }

print(value["name"])
print(group["skill"]["soft"])
print()
print(dictionary)
