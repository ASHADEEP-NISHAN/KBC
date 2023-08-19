print("welcome to Ashadeep's KBC")
questions= [
    [
        "What is the capital of France?",
        "1) Madrid", "2) Berlin", "3) Paris", "4) London",
        3  # Correct answer is option 3 (Paris)
    ],

    [
        "Which planet is known as the Red Planet?",
        "1) Venus", "2) Mars", "3) Jupiter", "4) Saturn",
        2  # Correct answer is option 2 (Mars)
    ],

    [
        "Which gas do plants use for photosynthesis?",
        "1) Carbon dioxide", "2) Oxygen", "3) Nitrogen", "4) Chlorine",
        1  # Correct answer is option 1 (Carbon dioxide)
    ],

    [
        "What is the largest mammal in the world?",
        "1) Elephant", "2) Blue whale", "3) Giraffe", "4) Lion",
        2  # Correct answer is option 2 (Blue whale)
    ],

    [
        "Which famous scientist developed the theory of relativity?",
        "1) Isaac Newton", "2) Galileo Galilei", "3) Albert Einstein", "4) Nikola Tesla",
        3  # Correct answer is option 3 (Albert Einstein)
    ],

    [
        "What is the chemical symbol for gold?",
        "1) Au", "2) Ag", "3) Cu", "4) Fe",
        1  # Correct answer is option 1 (Au)
    ],

    [
        "What is the tallest mountain in the world?",
        "1) Mount Kilimanjaro", "2) Mount Everest", "3) Mount McKinley", "4) Mount Fuji",
        2  # Correct answer is option 2 (Mount Everest)
    ],

    [
        "Which famous playwright wrote 'Romeo and Juliet'?",
        "1) William Shakespeare", "2) Jane Austen", "3) Charles Dickens", "4) Mark Twain",
        1  # Correct answer is option 1 (William Shakespeare)
    ],

    [
        "What is the chemical symbol for water?",
        "1) H2O", "2) Co2", "3) O2", "4) N2",
        1  # Correct answer is option 1 (H2O)
    ],

    [
        "What is the process by which plants make their own food?",
        "1) Respiration", "2) Digestion", "3) Photosynthesis", "4) Fermentation",
        3  # Correct answer is option 3 (Photosynthesis)
    ],

    [
        "Who painted the Mona Lisa?",
        "1) Vincent van Gogh", "2) Leonardo da Vinci", "3) Michelangelo", "4) Pablo Picasso",
        2 # Correct answer is option 2 (Leonardo da Vinci)
    ],

    [
        "What is the symbol for the element oxygen?",
        "1) Ox", "2) O", "3) Oz", "4) Oh",
        3  # Correct answer is option 3 (Oz)
    ],

    [
        "Which gas do humans breathe in?",
        "1) Carbon dioxide", "2) Oxygen", "3) Nitrogen", "4) Helium",
        3 # Correct answer is option 3 (Nitrogen)
    ],

    [
        "Who wrote the book '1984'?",
        "1) George Orwell", "2) Aldous Huxley", "3) J.R.R. Tolkien", "4) Ray Bradbury",
        1 # Correct answer is option 1 (George Orwell)
    ]
]

levels = [0,1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i+1]}")
    print(f"{questions[i][0]}")
    print(f" {question[1]}           {question[2]} ")
    print(f" {question[3]}           {question[4]} ")
    i+=1
    ua = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (ua == 0):
        money = levels[i - 1]
        break
    if (ua == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i+1]}")
        if (i > 4 and i< 9):
            money = 10000
        elif (i> 9 and i<14):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")