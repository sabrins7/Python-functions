import random


#  Define the question bank
questions = {
    "science": [{"q": "What is the chemical symbol for water?", "ans": "H2O"},
                {"q": "Which planet is known as the Red Planet?", "ans": "Mars"},
                {"q": "What is the speed of light in a vacuum (approximately)?", "ans": "300000 km/s"},
                {"q": "What is the powerhouse of the cell?", "ans": "Mitochondria"},
                {"q": "What gas do plants absorb from the atmosphere?", "ans": "Carbon Dioxide"},
                {"q": "What is the force that pulls objects towards each other?", "ans": "Gravity"},
                {"q": "What is the process by which plants make their own food?", "ans": "Photosynthesis"}
    ],
      "history": [{"q": "In what year did World War II end?", "ans": "1945"},
                {"q": "Who was the first President of the United States?", "ans": "George Washington"},
                {"q": "What ancient civilization built the Colosseum?", "ans": "Roman"},
                {"q": "In what year did the Titanic sink?", "ans": "1912"},
                {"q": "Who led the Indian independence movement against British rule?", "ans": "Mahatma Gandhi"},
                {"q": "What was the name of the ship that carried the Pilgrims to America?", "ans": "Mayflower"},
                {"q": "In what year did the French Revolution begin?", "ans": "1789"},
                {"q": "What important mathematical term, still widely used today, is derived from the name of Muhammad al-Khwarizmi?", "ans": "algorithm"},
      ],
       
        "culture": [{"q": "What is the holy book of Islam?", "ans": "Quran"},
        {"q": "In which city was the Prophet Muhammad (peace be upon him) born?", "ans": "Mecca"},
        {"q": "What is the name of the month of fasting in Islam?", "ans": "Ramadan"},
        {"q": "What is the direction of prayer (Qibla) for Muslims?", "ans": "Kaaba"},
        {"q": "What are the five pillars of Islam?", "ans": "Shahada, Salat, Zakat, Sawm, Hajj"},
        {"q": "What is the celebration that marks the end of Ramadan called?", "ans": "Eid al Fitr"},
        {"q": "What is the name of the cube-shaped building in Mecca that is the most sacred site in Islam?", "ans": "Kaaba"},
        {"q": "What language is the Quran primarily written in?", "ans": "Arabic"}
    ]
        
}       

players = []
scores = {}
rounds = 4

def ask_question(player):
    print(f" {player}, it's your  turn ")
    #defines a variable that saves the keys of (dictionary=names of categories) as list.
    available_categories = list(questions.keys())
    
    while True:
        #taking input and assuring that spaces and capital or small letter will not effect
        chosen_category = input("Choose a category (science, history, culture): ").strip().lower()

        if chosen_category in available_categories:
            break
        else:
            print("Invalid category. Please choose from:", ", ".join(available_categories))
            print("Ending your turn.")
            return False # finishes the turn due to invalid category choise

    #print(f"\nQuestion in {chosen_category} for {player}:")
    question_data = random.choice(questions[chosen_category])
    question_text = question_data["q"]
    correct_answer = question_data["ans"].strip().lower()
    print(f"Question: {question_text}")
    player_answer = input (f"Your answer:   ").strip().lower()

    if player_answer == correct_answer:
            scores[player] = scores.get(player, 0) + 1
            print(f"Correct! {scores[player]} point \n")
            return True   # correct answer
    else:
            print(f"Incorrect. The correct answer was: {correct_answer}")
            return False # wrong answer

# show score
def show_scores():
    print("Current Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")
        
# --- Display game results
def declare_winner():
    if scores:
        highest_score = max(scores.values())
        winners = [player for player, score in scores.items() if score == highest_score]
        if len(winners) == 1:
             print(f"\nThe winner is {winners[0]} with a score of {highest_score} congratulations!")
                  #{winners[0]} with a score of {highest_score}!")
        elif len(winners) > 1:
            winners_str = ", ".join(winners)
            print(f"\nIt's a tie! The winners are {winners_str} with a score of {highest_score}!")
        else:
            print("\nNo one scored any points in this game.")
    else:
        print("No players participated.")

def main():
     print("Welcome to the Quiz Game!")
     while True:
          try:
               num_players = int(input("How many players?"))
               if num_players < 1:
                    print("Error: Please enter at least one player.")
               else:
                    break
          except ValueError:
               print("Error: Invalid input.Pleae enter a number.")
     players = []
     for i in range(num_players):
          player_name = input(f"Enter name for player {i+1}: ").strip()
          players.append(player_name)
          scores[player_name] = 0

     for current_round in range(rounds):
          print(f"\n--- Round {current_round + 1} ---")
          for player in players:
             ask_question(player)
             show_scores()

     print("\n--- Game Over! ---")
     declare_winner()


if __name__ == "__main__":
    main()
    


