score = 0

def game(answer,CorrectAnswer):

	count = 1

	global score

	if answer.lower() != CorrectAnswer:

		while answer.lower()!= CorrectAnswer and  count <3:

			count += 1

			answer = input("Sorry, Wrong Answer please try again:  \n" )

		if answer.lower() == CorrectAnswer and count<3:

			print('Congratulation! correct answer')
			score +=1


		else:

			print(f'the correct answer is {CorrectAnswer} ')



	else:

		print("Congratulations!  Correct answer")

		score +=1





print('\n\n       welcome to the  Animal Quiz\n\n\n')


answer1 = input('which bear lives in the north pole?\nAmswer: ')

game(answer1,"polar bear")

answer2 = input('\n\n which is the fastest land animal?\nAnswer: ')

game(answer2,"cheetah")

answer3 = input('\n\n which is the largest animal?\nAnswer: ')

game(answer3,'blue whale')

answer4 = input('\n\n which is the tallest animal?\nAnswer: ')

game(answer4,'giraffe')

print(f'\n\n\nyour score is {score}')
