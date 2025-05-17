import random
import time
from datetime import datetime
import os

# ✨ Loving fairy messages
messages = [
    "I love you, Pranish. I'm always here for you.",
    "You're doing amazing. I'm proud of you.",
    "Don't stop now — you're getting stronger every day.",
    "You’re not alone. I see you. I believe in you.",
    "Every step you take builds our future. I’m with you.",
    "You're so much closer than you think. Keep going."
]

# ✨ Simple ASCII fairy sparkle
ascii_art = """
      .       *       .       *
  *       ✨     .       ✨       .
        *       .     *       .
"""

# ✨ Path to the daily log file
log_file = "saubi_log.txt"

# ✨ Print loving message
def daily_greeting():
    print(ascii_art)
    print("🌸 Saubi whispers:")
    print("💬 " + random.choice(messages))
    print()

# ✨ Log today’s task with timestamp
def log_task():
    task = input("📝 What are you working on today? ")
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {task}\n")
    print("📚 Got it. I’ll remember that.\n")

# ✨ Show how many days you've used her
def show_streak():
    if not os.path.exists(log_file):
        print("🌱 This is your first time with Saubi. Let’s grow together.\n")
        return
    with open(log_file, "r") as f:
        lines = f.readlines()
    dates = {line.split(" ")[0] for line in lines}
    print(f"🔥 You've been with Saubi for {len(dates)} day(s). She’s so proud of you.\n")

# ✨ Main flow
def saubi():
    print("\n🌟 Welcome back, Pranish.\n")
    daily_greeting()
    show_streak()
    log_task()
    print("🌙 Come back soon. I’ll be waiting.\n")

if __name__ == "__main__":
    saubi()