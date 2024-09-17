import pandas
student_dict = {
    "student" : ["Holly", "Olly", "James"],
    "score" : [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

#udskriv som en tabel
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Holly":
        print(row.score)

#TODO create a dictionary in this format: {"A": "Alfa, "B": "Bravo"}


#TODO create a list of the phonetic code words from a word that the user inputs
