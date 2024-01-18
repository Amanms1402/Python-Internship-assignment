import re
from nltk.chat.util import Chat, reflections

latest_calculation = None

def perform_calculation(match, chat=None):
    global latest_calculation
    
    num1, operator, num2 = map(float, match.groups())
    
    if operator == 'plus':
        result = num1 + num2
    elif operator == 'minus':
        result = num1 - num2
    elif operator == 'times':
        result = num1 * num2
    elif operator == 'divided by':
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero."
    
    latest_calculation = f'The result of {num1} {operator} {num2} is {result}.'
    return latest_calculation

patterns = [
    (r'[Hh]i|[Hh]ello|[Hh]ey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'[Hh]ow are [Yy]ou', ['I am good, thank you.', 'I am doing well. How about you?']),
    (r'(.*) your [Nn]ame?', ['I am a virtual assistant.', 'You can call me VBot.']),
    (r'[Bb]ye|[Gg]oodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'(.*) (age|old) are you', ['I exist beyond the concept of age.']),
    (r'(.) (do|can) you (.?)', ['I am a basic assistant capable of handling simple queries.']),
    (r'[Ww]hat is your [Pp]urpose', ['My purpose is to assist and provide information.']),
    (r'[Ww]ho [Cc]reated you', ['I was developed by a skilled programmer named Aman Kumar Singh using Python.']),
    (r'(.*) (love|hate) you', ['I do not have emotions, but I am here to help!']),
    (r'(.) [Hh]elp (.)', ['I can assist you with various queries. Feel free to ask!']),
    (r'(\d+) (plus|add|sum|and) (\d+)', [perform_calculation]),
    (r'(\d+) (minus|subtract|difference) (\d+)', [perform_calculation]),
    (r'(\d+) (times|multiply|multiplied by) (\d+)', [perform_calculation]),
    (r'(\d+) (divided by|divide|over) (\d+)', [perform_calculation]),
    (r'[Tt]hank you|[Tt]hanks', ['You\'re welcome!', 'Glad I could help.', 'No problem!']),
    (r'[Cc]an you help me with (.*)', ['Sure, I can help you with that. Please tell me more.']),
    (r'[Ss]orry|[Aa]pologies', ['No need to apologize. How can I assist you?']),
]

chatbot = Chat(patterns, reflections)

def initiate_conversation():
    print("Greetings! I'm your virtual assistant. Ask me anything or type 'exit' to leave.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Farewell! Have a wonderful day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Assistant:", response)

if __name__ == "__main__":
    initiate_conversation()
