import json
import random

def run_quiz(statements_by_topic):
    print("Welcome to the Quiz!")
    print("Available topics:")
    topics = list(statements_by_topic.keys())
    for i, topic in enumerate(topics, start=1):
        print(f"{i}: {topic}")
    
    try:
        chosen_index = int(input("Choose a topic by number: ").strip()) - 1
        if chosen_index < 0 or chosen_index >= len(topics):
            print("Invalid number. Exiting.")
            return
        chosen_topic = topics[chosen_index]
    except ValueError:
        print("Invalid input. Exiting.")
        return
    
    print(f"\nYou chose: {chosen_topic}")
    print("Answer True or False for each statement.\n")
    
    try:
        statements = statements_by_topic[chosen_topic]
    except KeyError:
        print(f"Error: The topic '{chosen_topic}' does not exist in the data.")
        return
    
    random.shuffle(statements)
    
    for i, item in enumerate(statements, start=1):
        statement = item["Statement"]
        correct_answer = item["Correct Answer"]
        explanation = item["Explanation"] 
        
        print(f"Statement: {statement}")
        user_answer = input("Your answer (True/False): ").strip()
        
        if user_answer.lower() == correct_answer.lower() or user_answer.lower() == correct_answer[0].lower():
            print("Correct!")
            print(f"Explanation: {explanation}\n")
        elif user_answer.lower() in ["quit", "exit"]:
            print("Bye bye")
            break
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
            print(f"Explanation: {explanation}\n")

try:
    with open("statements_by_topic.json", "r", encoding="utf-8") as f:
        statements_by_topic = json.load(f)
except FileNotFoundError:
    print("Error: The file 'statements_by_topic.json' was not found.")
    statements_by_topic = {}
except json.JSONDecodeError:
    print("Error: Failed to decode JSON from 'statements_by_topic.json'.")
    statements_by_topic = {}

run_quiz(statements_by_topic)