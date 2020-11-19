filename = 'programming_poll.txt'

prompt = "What is your favorite programming language?  \n"

languages = []
flag = True

while flag:
	language = input(prompt)
	languages.append(language)

	repeat = input("Would you like to let another person respond? (yes/no)  ")
	if repeat == 'no':
		flag = False 

with open(filename, 'w') as file_object:
	for language in languages:
		file_object.write(f"-{language}\n")