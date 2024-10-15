# A dictionary representing a user's profile
user_profile = {
    "name": "Tom",
    "age": 30,
    "email": "tom@example.com",
    "preferences": {"newsletter": True, "theme": "dark"},
}

# Accessing values by key
print(f"User's name is {user_profile['name']}")
print(f"User prefers the {user_profile['preferences']['theme']} theme")

# Dynamically adding new key-value pairs
user_profile["location"] = "Netherlands"
print(f"Updated user profile: {user_profile}")

# Updating an existing value
user_profile["age"] = 31
print(f"User's updated age is {user_profile['age']}")


import json

# JSON string received from an API (for example)
json_data = """{
    "name": "Tom",
    "age": 30,
    "location": "Netherlands",
    "preferences": {
        "newsletter": true,
        "theme": "dark"
    }
}"""
# Parse the JSON data into a Python dictionary
user_profile = json.loads(json_data)
# Now user_profile is a dictionary and can be accessed dynamically
print(f"User's name from JSON: {user_profile['name']}")
print(f"User prefers the {user_profile['preferences']['theme']} theme")
# Modifying the dictionary
user_profile["age"] += 1  # Incrementing age
# Convert the modified dictionary back to a JSON string
updated_json_data = json.dumps(user_profile, indent=4)
print(f"Updated JSON data:\n{updated_json_data}")

from types import SimpleNamespace

# Example dictionary
user_profile = {
    "name": "Tom",
    "age": 30,
    "location": "Netherlands",
    "preferences": {"newsletter": True, "theme": "dark"},
}
# Convert dictionary to object
user_obj = SimpleNamespace(**user_profile)
# Access as object attributes
print(user_obj.name)  # Tom
print(user_obj.location)  # Netherlands
print(user_obj.preferences)  # Still a dict, not an object
