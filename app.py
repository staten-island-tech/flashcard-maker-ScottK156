import json
class flash_cards:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer
    def to_dict(self):
        return {"question":self.question,"answer":self.answer}
    def display(self):
        return f"{self.question} {self.answer}"


""" mode = input("What mode would you like to use? ")
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
            cards_data = []

        # Append new card
        cards_data.append(my_card.to_dict())

        # Save updated data back to file
        with open("cards.json", "w") as file:
            json.dump(cards_data, file, indent=4)
        
        step = input("would you like to contuine or exit ")
        if step.lower() == "exit":
            break
elif mode.lower() == "student":
    while True:
     x = 0
     y= 0
     with open("cards.json", "r") as file:
            cards_data = json.load(file)
     for cards in cards_data:
         lebron = (cards['question'])
         guess = input(f"what matches to {lebron} ")
         if guess == cards['answer']:
             x += 1
             if y % 5 == 0 and y > 0:
                 y += 2
             else:
                 y+= 1
             print(f"correct streak is {x} and your score is {y}")
             step = input("Would you like to contuine or exit ")
             if step.lower() == "exit":
                 break
         else:
             print("incorrect")
             x = 0
             step = input("Would you like to contuine or exit ")
             if step.lower() == "exit":
                 break
     print(f"your final score was {y}")
     break """
class teacher:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    def to_file(key,value):
         # Load existing data
        try:
                with open("cards.json", "r") as file:
                    cards_data = json.load(file)
        except FileNotFoundError:
            cards_data = []

        # Append new card
        cards_data.append(my_card.to_dict())

        # Save updated data back to file
        with open("cards.json", "w") as file:
            json.dump(cards_data, file, indent=4)
class student:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def game():
         x = 0
         y = 0
         for cards in cards_data:
             lebron = (cards["question"])
             guess = input(f"what matches to {lebron}? ")
             if guess.lower() == cards["answer"]:
                 x += 1
                 if y % 5 == 0 and y > 0:
                     y += 2
                 else:
                     y += 1
             else:
                 print("incorrect") 
             print(f"Score:{y} Streak:{x}")
             step = input("exit or continue ")
             if step.lower() == "exit":
                 print(f"Final Score: {y}")
                 break
    
        
mode =input("what role do you want to use? ")
if mode.lower() == "teacher":
 while True : 
        key = input("Give me a word ")
        value = input("Give me the answer ")
        my_card = flash_cards(key,value)
        teacher.to_file(key,value)
        step = input("continue or exit ")
        if step.lower() == "exit":
            break
elif mode.lower() == "student":
     with open("cards.json", "r") as file:
         cards_data = json.load(file)
     while True:
        student.game()
        break










