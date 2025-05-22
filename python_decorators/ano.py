import time
from functools import wraps

# --- Decorators ---

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} ran in {end - start:.4f} seconds.")
        return result
    return wrapper

# --- Core Flashcard Logic ---

@logger
@timer
def run_flashcards(cards):
    score = 0
    for question, answer in cards.items():
        print(f"\nQuestion: {question}")
        user_input = input("Your answer: ").strip()
        if user_input.lower() == answer.lower():
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The answer was: {answer}")
    print(f"\nYour score: {score}/{len(cards)}")

# --- Entry Point ---

if __name__ == "__main__":
    flashcards = {
        "Capital of Germany": "Berlin",
        "5 + 7": "12",
        "Python keyword for a function": "def"
    }

    print("🧠 Welcome to Flashcard Quiz!\n")
    run_flashcards(flashcards)