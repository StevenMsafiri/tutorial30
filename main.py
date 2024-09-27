import json

with open("./Password manager/Password data.json", "r") as file:
    data = json.load(file)
    print(type(data))

# Searching for a key if exists
website_input = input("Enter website address: ")
print(type(website_input))

if website_input in data:
    print((data[website_input]["email"]))

else:
    print("Please enter a valid website address")