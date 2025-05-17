import random

# List of creepy fortunes
fortunes = [
    "You will hear whispers in the silence tonight...",
    "A shadow watches you while you sleep...",
    "Your reflection will blink before you do.",
    "Someone you trust hides a secret.",
    "Do not look under your bed tonight.",
    "Your name is being spoken... by someone long gone.",
    "The wind carries a message only the dead understand.",
    "A door will open that was never meant to.",
    "What you lost will return... but not as you remember it.",
    "You're not alone right now."
]

def get_fortune():
    return random.choice(fortunes)

def main():
    print("\n🧿 Welcome to the Cursed Fortune Teller 🧙‍♂️")
    
    start = input("\nDo you dare to know your fate? (y/n): ").lower()
    
    if start != 'y':
        print("\n🔒 You chose safety ... for now.\n")
        return

    while True:
        fortune = get_fortune()
        print(f"\n🔮 Your fate: \"{fortune}\"")
        
        again = input("\nAsk again? (y/n): ").lower()
        if again != 'y':
            print("\n👁️ Farewell, mortal. Your destiny awaits... \n")
            break

if __name__ == "__main__":
    main()