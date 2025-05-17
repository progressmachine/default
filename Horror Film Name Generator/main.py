import random

# Lists of spooky words
adjectives = [
    "Bloody", "Dark", "Cursed", "Haunted", "Evil", "Twisted", "Deadly", "Sinister", "Forgotten", "Burning", "Strange", "Curious"
]

nouns = [
    "Forest", "House", "Mirror", "Doll", "Basement", "Shadows", "Grave", "Whisper", "Night", "Silence", "Child", "Spirit", "Start"
]

phrases = [
    "of the Dead", "from Hell", "in the Fog", "Under the Moon", "that Screamed", "on Elm Street",
    "of No Return", "Beneath the Floor", "Behind the Door", "from the Attic", "of the Children"
]

def generate_title():
    title_type = random.choice(["adj_noun", "noun_phrase", "adj_noun_phrase"])
    
    if title_type == "adj_noun":
        return f"The {random.choice(adjectives)} {random.choice(nouns)}"
    elif title_type == "noun_phrase":
        return f"The {random.choice(nouns)} {random.choice(phrases)}"
    else:
        return f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(phrases)}"

# Main CLI loop
def main():
    print()
    print("🎃 Welcome to the Horror Film Name Generator! 🎬")
    print()
    x = input("Do you want to generate a Horror Film's Name? (y/n): ").lower()
    
    if x == 'y':
        while True:
            title = generate_title()
            print(f"\n👉 Your horror film title: **{title}**")
            print()
            again = input("Generate another? (y/n): ").lower()
            if again != 'y':
                print("👻 Stay spooky!")
                break
    else:
        print("👻 Stay spooky!")


if __name__ == "__main__":
    main()