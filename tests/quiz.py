import re
import json

txt_file = "output.txt"  # Replace with your text file name
with open(txt_file, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"\d+\.\s+(.*?)(True|False)\.\s+(.*?)(?=\d+\.|$)" # this pattern shows the question, answer, and explanation and has three groups.
matches = re.findall(pattern, content, re.DOTALL) # findall does not return the groups, but the whole match. use this to get the groups. use re.DOTALL to match across multiple lines.

# next, we process the extracted data because we want to extract the question, answer, and explanation from the matches.

questions = [] # square brackets are used to create a list because we want to store the questions, answers, and explanations in a list and the only way to do that is to use a list. we cant use dictionaries because we have multiple questions, answers, and explanations. we use a list of tuples to store the questions, answers, and explanations. examlpe of list of tuples: [(question1, answer1, explanation1), (question2, answer2, explanation2), ...]
for match in matches: # this because we want to extract the question, answer, and explanation from the matches and store them in a list. and we use a for loop to iterate over the matches.
    statement = match[0].strip() # the first group is the statement, so we extract it and remove any leading or trailing whitespaces. %strip() removes leading and trailing whitespaces.
    correct_answer = match[1].strip() # the second group is the correct answer, so we extract it and remove any leading or trailing whitespaces.
    explanation = match[2].strip() # the third group is the explanation, so we extract it and remove any leading or trailing whitespaces.
    questions.append((statement, correct_answer, explanation)) # we append a tuple of the statement, correct answer, and explanation to the questions list.

# print the questions, answers, and explanations
for i, (statement, correct_answer, explanation) in enumerate(questions, start=1): # we use enumerate to loop over the questions list and get the index and the tuple containing the statement, correct answer, and explanation.
    print(f"Statement {i}: {statement}") # print the statement
    print(f"Correct Answer: {correct_answer}") # print the correct answer
    print(f"Explanation: {explanation}\n") # print the explanation


# Quiz program

print("Welcome to the Quiz! Answer True or False for each statement.\n")

json_dict_file = "quiz_data_dict.json"  # Replace with your JSON file name

with open(json_dict_file, "r", encoding="utf-8") as f:
    
        quiz_data_dict = json.load(f)

for question, data in quiz_data_dict.items():
        
        print(f"{question}: {data['Statement']}")
        
        user_answer = input("\nYour answer (True/False): ").strip()
        
        if user_answer.lower() == data["Correct Answer"].lower():
            
            print("Correct!")
        
        elif user_answer.lower() in ["quit", "exit"]:
            
            print("Bye bye")
            
            break
        
        else:
            
            print("Incorrect.")
        
        print(f"Explanation: {data['Explanation']}\n")
