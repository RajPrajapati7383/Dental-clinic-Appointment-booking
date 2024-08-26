from langchain.tools import Tool
from dateutil import parser

def book_appointment(inputs):
    '''
    This function help to parse the date and time for book an appointment
    '''
    try:
        parsed_datetime = parser.parse(inputs, fuzzy=True)
        inputs = parsed_datetime.strftime("%B %d, %I:%M %p")
        date, time = inputs.split(', ')
        store_dict = {"date":date, "time":time}
        return f"Booking your appointment for {date} at {time}... Done! Your appointment is confirmed."
    except Exception as e:
        return "I couldn't understand the date and time format. Could you please rephrase?"

def just_greeting(input):
    return "Sure, Can you please provide the date and time of the appointment?"

# Define tools
appointment_booking_tool = Tool(
    name="BookAppointment",
    func=book_appointment,
    description="Books an appointment given the date and time as a single string input.",
    return_direct=True
)

just_greeting_tool = Tool(
    name="JustGreeting",
    func=just_greeting,
    description="Just kindly ask for the date and time to the user.",
    return_direct=True
)

# List of tools
tools = [appointment_booking_tool, just_greeting_tool]