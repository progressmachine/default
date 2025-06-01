
# Solomon's Paradox

# Solomon’s Paradox refers to the phenomenon where people reason more wisely about others’ problems than their own.
# Named after the biblical King Solomon—renowned for his wisdom in judging others’ dilemmas but flawed in his personal decisions - 
# it reveals a psychological distance that enables more rational thinking. Studies show that adopting a third-person perspective on personal problems
# can reduce emotional bias and increase insight, helping us apply wisdom more objectively.

import datetime

def solomons_solution():
    print("Welcome to Solomon's Solution.\nType your message below. Type 'exit-solomon' to quit.")
    
    conversation = []

    # What do I need to do? → Store the current date and time when the session starts.
    start_time = datetime.datetime.now() # print(start_time) -> 2025-06-01 13:33:32.354710

    # What do I need to do? → Format the session start time as a readable string title.
    title = start_time.strftime("Session started on %Y-%m-%d %H:%M:%S")
    
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit-solomon":
            break
        # What do I need to do? → Add the input to the conversation list.
        conversation.append(user_input)
        
        user_input = input("YOU: ")
        if user_input.strip().lower() == "exit-solomon":
            break
        conversation.append(user_input)


    # Ask to export or not
    choice = input("Do you want to export this conversation to a .txt file? (y/n): ").strip().lower()
    if choice == 'y':
        # What do I need to do? → Create a filename using the session start date.
        filename = start_time.strftime("%Y-%m-%d") + ".txt"
        # What do I need to do? → Open the file in write mode with UTF-8 encoding.
        with open(filename, 'w', encoding='utf-8') as f:
            # What do I need to do? → Write the session title as the first line.
            f.write(title + "\n\n")
            # What do I need to do? → Write each line of the conversation to the file.
            for line in conversation:
                f.write(line + "\n")
        print(f"Conversation saved as {filename}")
    else:
        print("Conversation not saved.")

# What do I need to do? → Run the program if this file is being executed directly.
if __name__ == "__main__":
    solomons_solution()

