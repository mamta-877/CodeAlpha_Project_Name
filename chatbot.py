import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you!",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem",]
 ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to know that you're %1",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]
def chatbot():
    print("Hi, I'm your chatbot! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()
chatbot()