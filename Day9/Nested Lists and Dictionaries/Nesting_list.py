# nested list in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# printing the specific value
print(travel_log["France"][1]) # prints "Lille"

# nested list
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])