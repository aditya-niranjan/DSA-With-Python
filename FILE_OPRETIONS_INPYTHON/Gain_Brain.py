import random

questions = {
    "q1": "What is the sum of 23, 19, and 42?",
    "q2": "Multiply 'eight' with 7 and enter the result.",
    "q3": "In the following paragraph, how many times does the word 'magic' appear?",
    "q4": "Which number is the greatest among these: 12, 89, 3, 45, 17?",
    "q5": "Fill in the blank: ___ × 9 = 81",
    "q6": "What is 10 + 5?",
    "q7": "What is 7 × 6?",
    "q8": "What is 100 - 25?",
    "q9": "What is 9 divided by 3?",
    "q10": "What is 2 squared?",
    "q11": "What is the capital letter of 'a'?",
    "q12": "How many letters are in the word 'banana'?",
    "q13": "Which number is even: 3, 5, 6, 7?",
    "q14": "What is 11 + 11?",
    "q15": "Which number comes first: 4 or 9?",
    "q16": "How many legs does a cat have?",
    "q17": "What is 3 × 5?",
    "q18": "What is the opposite of 'hot'?",
    "q19": "Which color is a fruit: red, blue, orange?",
    "q20": "What day comes after Monday?",
    "q21": "What is 12 divided by 4?",
    "q22": "How many fingers on one hand?",
    "q23": "Which is bigger: 99 or 100?",
    "q24": "What is the third letter in 'apple'?",
    "q25": "How many vowels in 'hello'?",
    "q26": "What is 20 minus 8?",
    "q27": "Which number is odd: 2, 4, 5, 8?",
    "q28": "What comes next: A, B, C, ___?",
    "q29": "What is 15 + 5?",
    "q30": "How many hours in a day?"
}

answers = {
    "a1": 42,
    "a2": 56,
    "a3": 1,
    "a4": 89,
    "a5": 9,
    "a6": 15,
    "a7": 42,
    "a8": 75,
    "a9": 3,
    "a10": 4,
    "a11": "A",
    "a12": 6,
    "a13": 6,
    "a14": 22,
    "a15": 4,
    "a16": 4,
    "a17": 15,
    "a18": "cold",
    "a19": "orange",
    "a20": "Tuesday",
    "a21": 3,
    "a22": 5,
    "a23": 100,
    "a24": "p",
    "a25": 2,
    "a26": 12,
    "a27": 5,
    "a28": "D",
    "a29": 20,
    "a30": 24
}


# Step 1: Pick a random question key
random_key = random.choice(list(questions.keys()))

# Step 2: Map to corresponding answer key
answer_key = "a" + random_key[1:]

# Step 3: Ask until correct using walrus operator
while (user_input := input(f"{questions[random_key]}\nYour answer: ")) != str(answers[answer_key]):
    print("❌ Incorrect! Try again...\n")
else:
    print("✅ Correct! Well done.")
