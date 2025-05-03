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
                {"q": "Who painted the Mona Lisa?", "ans": "Leonardo da Vinci"},
                ],

    "culture": [{"q": "What is the holy book of Islam?", "ans": "Quran"},
                {"q": "In which city was the Prophet Muhammad (peace be upon him) born?", "ans": "Mecca"},
                {"q": "What is the name of the month of fasting in Islam?", "ans": "Ramadan"},
                {"q": "What is the direction of prayer (Qibla) for Muslims?", "ans": "Kaaba"},
                {"q": "What are the five pillars of Islam?", "ans": "Shahada, Salat, Zakat, Sawm, Hajj"},
                {"q": "What is the celebration that marks the end of Ramadan called?", "ans": "Eid al-Fitr"},
                {"q": "What is the name of the cube-shaped building in Mecca that is the most sacred site in Islam?", "ans": "Kaaba"},
                {"q": "What language is the Quran primarily written in?", "ans": "Arabic"}
                ]
}


#print(questions["science"])

players = []
scores = {}
rounds = 3

def ask_question(player):
    print(f"\n {player}'s turn ")
    available_categories = list(questions.keys())
   #chosen_category = input ("Choose a category (science, history, culture): ").strip().lower()

    while True:
        chosen_category = input("Choose a category (science, history, culture): ").strip().lower()
        if chosen_category in available_categories:
            break
        else:
            print("Invalid category. Please choose from:", ", ".join(available_categories))
            print("Ending your turn.")

    print(f"\nQuestion in {chosen_category} for {player}:")
ask_question("jojo")

    