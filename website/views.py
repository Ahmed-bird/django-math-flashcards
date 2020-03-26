from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def add(request):
	from random import randint

	num_1 = randint(0, 9)
	num_2 = randint(0, 9)

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		if not answer:
			my_answer = 'Hey! You forgot to fill up the form'
			detail = ''
			color = 'warning'
			num_1 = old_num_1
			num_2 = old_num_2
		else:
			result = int(old_num_1) + int(old_num_2)
			if int(answer) == result:
				# my_answer = 'Correct! ' + old_num_1 + ' + ' + old_num_2 + ' is ' + answer
				my_answer = 'Correct!'
				detail = old_num_1 + ' + ' + old_num_2 + ' is ' + answer
				color = 'success'
			else:
				# my_answer = 'Incorrect! ' + old_num_1 + ' + ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
				my_answer = 'Incorrect!'
				detail = old_num_1 + ' + ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
				color = 'danger'

		return render(request, 'add.html', {
			'my_answer' : my_answer,
			'detail' : detail,
			'color' : color,
			'num_1' : num_1,
			'num_2' : num_2,
		})

	return render(request, 'add.html', {
		'num_1' : num_1,
		'num_2' : num_2,
	})

def subtract(request):
	from random import randint

	num_1 = randint(0, 9)
	num_2 = randint(0, 9)

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		if not answer:
			my_answer = 'Hey! You forgot to fill up the form'
			detail = ''
			color = 'warning'
			num_1 = old_num_1
			num_2 = old_num_2
		else:
			result = int(old_num_1) - int(old_num_2)
			if int(answer) == result:
				# my_answer = 'Correct! ' + old_num_1 + ' - ' + old_num_2 + ' is ' + answer
				my_answer = 'Correct!'
				detail = old_num_1 + ' - ' + old_num_2 + ' is ' + answer
				color = 'success'
			else:
				# my_answer = 'Incorrect! ' + old_num_1 + ' - ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
				my_answer = 'Incorrect!'
				detail = old_num_1 + ' - ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
				color = 'danger'

		return render(request, 'subtract.html', {
			'my_answer' : my_answer,
			'detail' : detail,
			'color' : color,
			'num_1' : num_1,
			'num_2' : num_2,
		})

	return render(request, 'subtract.html', {
		'num_1' : num_1,
		'num_2' : num_2,
	})

def multiply(request):
	from random import randint

	num_1 = randint(0, 9)
	num_2 = randint(0, 9)

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		if not answer:
			return render(request, 'multiply.html', {
				'my_answer' : 'Hey! You forgot to fill up the form',
				'color' : 'warning',
				'num_1' : old_num_1,
				'num_2' : old_num_2,
			})

		result = int(old_num_1) * int(old_num_2)
		if int(answer) == result:
			# my_answer = 'Correct! ' + old_num_1 + ' x ' + old_num_2 + ' is ' + answer
			my_answer = 'Correct!'
			detail = old_num_1 + ' x ' + old_num_2 + ' is ' + answer
			color = 'success'
		else:
			# my_answer = 'Incorrect! ' + old_num_1 + ' x ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
			my_answer = 'Incorrect!'
			detail = old_num_1 + ' x ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
			color = 'danger'

		return render(request, 'multiply.html', {
			'my_answer' : my_answer,
			'detail' : detail,
			'color' : color,
			'num_1' : num_1,
			'num_2' : num_2,
		})

	return render(request, 'multiply.html', {
		'num_1' : num_1,
		'num_2' : num_2,
	})

def divide(request):
	from random import randint

	num_1 = randint(0, 9)
	num_2 = randint(1, 9)

	if request.method == 'POST':
		answer = request.POST['answer']
		old_num_1 = request.POST['old_num_1']
		old_num_2 = request.POST['old_num_2']

		if not answer:
			return render(request, 'divide.html', {
				'my_answer' : 'Hey! You forgot to fill up the form',
				'color' : 'warning',
				'num_1' : old_num_1,
				'num_2' : old_num_2,
			})

		result = int(old_num_1) // int(old_num_2)
		if int(answer) == result:
			# my_answer = 'Correct! ' + old_num_1 + ' / ' + old_num_2 + ' is ' + answer
			my_answer = 'Correct!'
			detail = old_num_1 + ' / ' + old_num_2 + ' is ' + answer
			color = 'success'
		else:
			# my_answer = 'Incorrect! ' + old_num_1 + ' / ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
			my_answer = 'Incorrect!'
			detail = old_num_1 + ' / ' + old_num_2 + ' is not ' + answer + ' it\'s ' + str(result)
			color = 'danger'

		return render(request, 'divide.html', {
			'my_answer' : my_answer,
			'detail' : detail,
			'color' : color,
			'num_1' : num_1,
			'num_2' : num_2,
		})

	return render(request, 'divide.html', {
		'num_1' : num_1,
		'num_2' : num_2,
	})
