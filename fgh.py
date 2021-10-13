from Question import Question


question_prompts = [
 "Waar woon ik?\n(a) Amsterdam\n(b) Purmerend\n(c) Uterecht\n\n",
 "Hoe oud ben ik?\n(a) 14\n(b) 15\n(c) 16\n\n",
 "Wat is mijn liefelings eten?\n(a) pizza\n(b) shusi\n(c) pannen koeken\n\n"
]
    
questions = [
   Question(question_prompts[0], "b"),
   Question(question_prompts[1], "c"),
   Question(question_prompts[2], "c"),
]

def run_test(questions):
   score = 0
   for question in questions:
       answer = input(question.prompt) 
       if answer == question.answer:
           score += 1
           print("je heb er " +  str(score) + " goed van de 3")
run_test(questions)
