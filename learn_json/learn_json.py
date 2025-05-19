import json

def intro():
    print("\n👋 Welcome to the JSON Learning Program!")
    print("JSON = JavaScript Object Notation")
    print("It's a way to store and exchange data using key-value pairs like a Python dictionary.\n")

def show_example():
    python_data = {
        "name": "Pranish",
        "age": 18,
        "is_student": True,
        "languages": ["German", "Nepali", "English"]
    }

    print("📦 Python Dictionary:")
    print(python_data)

    json_data = json.dumps(python_data, indent=4)
    print("\n🔁 Converted to JSON string (serialization):")
    print(json_data)

    back_to_python = json.loads(json_data)
    print("\n🔄 Back to Python dictionary (deserialization):")
    print(back_to_python)

def interactive_learning():
    print("\n🧪 Let's try converting your own data!")
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    student = input("Are you a student? (yes/no): ").lower() == 'yes'
    langs = input("List some languages you know (comma separated): ").split(',')

    user_dict = {
        "name": name,
        "age": age,
        "is_student": student,
        "languages": [lang.strip() for lang in langs]
    }

    print("\n✅ Your data in Python dictionary:")
    print(user_dict)

    # Convert dictionary to JSON string
    json_version = json.dumps(user_dict, indent=4)
    print("\n📄 Your data as JSON string:")
    print(json_version)

    # Convert back to dictionary (simulate receiving JSON)
    parsed_json = json.loads(json_version)

    print("\n📚 Accessing values from JSON (converted back to dictionary)...")
    print(f"Hello {parsed_json['name']}! You know {len(parsed_json['languages'])} languages.")

def main():
    intro()
    show_example()
    interactive_learning()

if __name__ == "__main__":
    main()
