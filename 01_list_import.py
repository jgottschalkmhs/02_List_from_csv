import csv
import random

# Get list from csv and import it

# name of csv file goes here...
with open('colours.csv', 'r') as f:

    # make csv file into list
    file = csv.reader(f)
    my_list = list(file)

print(my_list)

# to choose a question and answer...
# choose an item from the main list, this item is itself a list
question_ans = random.choice(my_list)

# first item in small list
question = question_ans[0]
answer = question_ans[1]

print()
print("Question: What colour is {}".format(question))
print("Answer: {} is {}".format(question, answer))
