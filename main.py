# List Comprehension
# new_list = [new_item for item in list]

# Dictionary Comprehension
#new_dict = {new_key:new_value for (key,value) in dict.items() if test}

#for (index, row) in student_data_frame.iterrows():
 #   print(row.score)
import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

df = pd.read_csv("nato_phonetic_alphabet.csv")

#Looping through the dataframe one row at a time and taking the letter and code from each row and putting it into a dict
nato_dict = {row.letter:row.code for (index,row) in df.iterrows()}




#{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


code_name = 0
def generate_phonetic():

    try:
        name = input("What is your name? ").replace(" ", "").upper()
        code_name = [nato_dict[char] for char in name]
    except KeyError:
        print("Only use letters please.")
        generate_phonetic()
    else:
        print(code_name)

generate_phonetic()

