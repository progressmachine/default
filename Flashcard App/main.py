import json
import os
import time

FILE_NAME = "flashcards.json"

def load_flashcards():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_flashcards(flashcards):
    with open(FILE_NAME, "w") as f:
        json.dump(flashcards, f, indent=4)

def main():
    flashcards = load_flashcards()

    while True:
        print("\nFlashcard App")
        print("1. Add flashcard")
        print("2. Review flashcards")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            question = input("Enter question: ")
            answer = input("Enter answer: ")
            flashcards.append({"question": question, "answer": answer})
            save_flashcards(flashcards)
            print("Flashcard added and saved!")

            # ah! so the output of json.load() really just depends on what it was fed

        elif choice == "2":
            if not flashcards:
                print("No flashcards to review yet.")
            else:
                for i, card in enumerate(flashcards, 1): # goes through the list (flashcards) of dictionaries
                    print(f"\nFlashcard {i}: {card['question']}") # each instance of card is a dictionary
                    input("Press Enter to see the answer ...")
                    print(f"Answer: {card['answer']}")
                    time.sleep(0.2)
        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()