#! /bin/env python3
import re

def greet_back(time_of_day):
    if time_of_day == "dia":
        return f"Bom {time_of_day}!"
    else:
        return f"Boa {time_of_day}!"

def genki_back(_):
    return "Comigo está tudo bem, e com você?"

intent_dict = {
    r"\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))": "greetings",
    r"\b(?:[Tt]udo)?\s?(?:(?:[bB]em)|(?:[bB]ão)|(?:[fF]irme)|(?:em\sriba))\?": "genki"
}

action_dict = {
        "greetings": greet_back,
        "genki": genki_back
}

command = input("Digite o seu comando: ")
for key, value in intent_dict.items():
    pattern = re.compile(key)
    groups = pattern.findall(command)
    if groups:
        print(f"{action_dict[value](groups[0])}", end=" ")
print()