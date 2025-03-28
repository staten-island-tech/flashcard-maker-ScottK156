import json
import random
class flash_cards:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return {"question":self.question,"answer":self.answer}
    def display(self):
        return f"{self.question} {self.answer}"


mode = input("What mode would you like to use?")
if mode.lower() == "teacher":
    while True:

        question = input("Give me the Flashcard word ")
        answer =input("Give me the answer to that card ")
        my_card = flash_cards(question,answer)
        print(my_card.display())

        # Load existing data
        try:
                with open("cards.json", "r") as file:
                    cards_data = json.load(file)
        except FileNotFoundError:
            cars_data = []

        # Append new car
        cards_data.append(my_card.to_dict())

        # Save updated data back to file
        with open("cards.json", "w") as file:
            json.dump(cards_data, file, indent=4)
        
        step = input("would you like to contuine or exit ")
        if step.lower() == "exit":
            break
elif mode.lower() == "student":
    while True:
     with open("cards.json", "r") as file:
            cards_data = json.load(file)
     for cards in cards_data:
         lebron = random.choice(cards['question'])
         print(lebron)





