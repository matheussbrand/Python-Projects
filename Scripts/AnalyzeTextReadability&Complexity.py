# This code analyzes the readability and complexity of 
# texts for machine learning in Python.


from textstat import textstat

#text = "The Devil hath power to assume a pleasing shape."
#William Shakespeare

#text = "Out of your vulnerabilities will come your strength."
#Freud

text = "You take the blue pill, the story ends, you wake up in your bed and believe whatever you want to believe"
#Matrix

#text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id lacus a urna pulvinar pretium. Phasellus tempor neque sed magna."

#8-30: Very difficult.Best understood by university graduates.
#30-50: Difficult. Best understood by college students.
#50-60: Fairly difficult. High school students should be able to understand.
#68-70: Standard. Easily understood by 13- to 15-year-old students.
#70-80: Fairly easy.
#80-98: Easy.Easily understood by an average 11-year-old student.
#98-100: Very easy. Easily understood by an average 18-year-old student.

print(textstat.flesch_reading_ease(text))
print(textstat.flesch_kincaid_grade(text))
print(textstat.gunning_fog(text))
print(textstat.automated_readability_index(text))
print(textstat.coleman_liau_index(text))
print(textstat.linsear_write_formula(text))
print(textstat.dale_chall_readability_score(text))

print(textstat.difficult_words(text))
print(textstat.difficult_words_list(text))
