# ********************
# dictionaries
# ********************
person = {
  "name": "yoshi",
  "age": 30,
  "job": "egg collector"
}

print(person["name"])
print(person["age"])

# ********************
# methods
# ********************
print(person.get("name")) # get(key, defaultValue)

print(person.keys()) # dict_keys -> dictionary views
print(person.values()) # dict_values -> dictionary views
print("age" in person.keys()) # True

copied_person = person.copy() # clone
print("copied person:", copied_person)

person.update({"name": "mario", "age": 35})
print("updated person:", person)

person.clear()
print('cleared person:', person)