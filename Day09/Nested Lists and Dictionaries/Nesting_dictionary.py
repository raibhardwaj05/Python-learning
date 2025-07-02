# Nested dictionary

travel_log = {
    "France": {
        "cities_visted": 3,
        "total_visits": 12,
        "cities_name": ["Paris", "Lille", "Dijon"]
    },

    "Germany": {
        "cities_visted": 2,
        "total_visits": 12,
        "cities_name": ["Stuttgart", "Berlin"]
    }
}

# to print any specific value
print(travel_log["France"]["cities_name"][1])