#Python program to perform various dictionary operations.
dict = {
    "name" : "Ankit Pal",
    "class" : "12th",
    "subject & marks" : {
        "Hindi" : 90,
        "English" : 86,
        "Math" : 70,
        "Physics" : 75,
        "Chemistry" : 78,
    } 
}
print(dict)
print(type(dict),"\n")
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("name"))
dict.update({"city" : "Ayodhya"})
print(dict)
