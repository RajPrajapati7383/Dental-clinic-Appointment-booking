from agent import agent
import re

def contains_date_time(text):
    '''
        Function to check if input contains both date and time
    '''
    date_pattern = r"\b\d{1,2}(st|nd|rd|th)?\b"
    time_pattern = r"\b\d{1,2}(:\d{2})?\s*(AM|PM|am|pm)?\b"
    return re.search(date_pattern, text) and re.search(time_pattern, text)

def run_conversation():
    '''
        Function to handle the conversation dynamically
    '''
    print("Agent: Hello! Welcome to the dental clinic.")

    while True:
        user_input = input("You: ")

        if contains_date_time(user_input):
            response = agent.run(f"Use BookAppointment tool to book: {user_input}")
            print(f"Agent: {response}")
            break
        else:
            response = agent.run(f"Use JustGreeting tool to ask for date and time: {user_input}")
            print(f"Agent: {response}")

# Start conversation
if __name__ == "__main__":
    run_conversation()