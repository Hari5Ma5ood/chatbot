# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

def get_answer_from_internet(query):
    r = requests.get(f'https://google.com/search?q={query}')
    content = r.content
    return content


def train_chat_bot(bot_instance):
    trainer = ListTrainer(bot_instance)
    trainer.train(["in the name of ", "ALLAH"])
    trainer.train(['Who is the most beneficient', 'who ever eill rais my pay'])
    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_chat = ChatBot('Haris First')
    chatboot_training = train_chat_bot(my_chat)
    exit_conditions = [':q', 'exit']
    while True:
        query = input('> ')
        if query in exit_conditions:
            break
        else:
            print(f':P {my_chat.get_response(query)}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
