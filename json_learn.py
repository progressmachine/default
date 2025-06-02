
# Q: What library do I need to work with JSON in Python?
import json

# Q: How do I create a Python dictionary that I want to convert to JSON?
data = {
    "name": "Sita",
    "age": 30,
    "is_programmer": True,
    "skills": ["Python", "JavaScript", "SQL"]
}

# Q: How do I convert the Python dictionary into a JSON string?
json_string = json.dumps(data)

# Q: How do I print the JSON string?
print("JSON string:", json_string)  # JSON string: {"name": "Sita", "age": 30, "is_programmer": true, "skills": ["Python", "JavaScript", "SQL"]}

# Q: How do I save this JSON string to a file?
with open("data.json", "w") as file:
    file.write(json_string)

# Q: How do I read JSON data back from a file?
with open("data.json", "r") as file:
    loaded_json = file.read()

# Q: How do I convert the JSON string back into a Python dictionary?
data_loaded = json.loads(loaded_json)

# Q: How do I access a value from the loaded dictionary?
print("Name from loaded data:", data_loaded["name"])  # Name from loaded data: Sita

# Total Output:

# JSON string: {"name": "Sita", "age": 30, "is_programmer": true, "skills": ["Python", "JavaScript", "SQL"]}
# Name from loaded data: Sita