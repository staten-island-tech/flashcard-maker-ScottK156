import json

class flash_cards:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return {"question":self.question,"answer":self.answer}
    def display(self):
        return f"{self.question} {self.answer}"
my_card = flash_cards("science","hello")
print(my_card.display())

try:
    with open("FlashCards.json", "r") as file:
        cards_data = json.load(file)
except FileNotFoundError:
    cards_data = []

# Append new car
cards_data.append(my_card.to_dict())

# Save updated data back to file
with open("FlashCards.json", "w") as file:
    json.dump(cards_data, file, indent=4)
        
#Student Mode


#Teacher Mode
