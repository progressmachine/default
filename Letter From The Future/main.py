import time

letter = """
Hey bro,
You made it.

I’m sitting in a little café in Leipzig. I just finished a lecture on sustainable infrastructure — in German. 
It still blows my mind sometimes. Not because it’s a surprise I made it… but because I remember the version of me who refused to quit, no matter how slow it felt.

You remember those 40-minute Anki grinds?
The days when progress felt invisible?
The 3 AM research shifts, squeezing in flashcards between experiments?

That’s the version of us I’m proud of — not because he was perfect — but because he was relentless.

Everyone else waited for motivation. You? You waited for nothing. You got up, showed up, and stacked hours like bricks.

Remember how small it felt at first? 2.81 days of German total after 7 months?
Now you're sitting on over 700 hours logged. Fluent. Free. Focused.

Here’s what I wish I could whisper back to you in 2025:

- The effort compounds, even when it feels invisible.
- One hour a day is enough, if it’s every day.
- Your future isn’t built on motivation. It’s built on refusal to quit.

You didn't just learn German.
You became the type of man who never lets time slip by unlived.

So keep going.
Do today’s reps.
You’re not just learning a language.
You’re building the life you already know is yours.

I’ll see you in a few years. You’ll recognize me —
I speak German like I was born here.

— Pranish, 2028 🇩🇪
"""

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

typewriter(letter)