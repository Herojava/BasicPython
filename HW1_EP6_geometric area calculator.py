# HW1_EP6_geometric area calculator.py
import time

time.sleep(0.75)
print('Hi, I am a geometric area calculator')
print('----------------------------')
print('----------------------------')
time.sleep(0.75)
user = input('Who are you?\n:: ')
print('----------------------------')
print('----------------------------')
time.sleep(0.75)
print('Wellcome {} to geometric area calculator v.0'.format(user))
print('----------------------------')
print('----------------------------')

program = ['Square area calculator', 'Triangle area calculator', 'Circle area calculator']
time.sleep(0.75)

while True:
	for i, p in enumerate(program, start=1):
		print('Please press {} for {}'.format(i, p))
	print('Q for quit the program')
	print('----------------------------')
	print('----------------------------')
	program_number = input('Select program No. : ')

	if program_number == '1':
		width = ''
		length = ''
		time.sleep(0.3)
		print('----------------------------')
		print('----------------------------')
		print('Square area calculator')
		print('----------------------------')
		print('----------------------------')	
		time.sleep(0.3)	
		while not width.isdigit():
			width = input('width (cm) :: ')
			time.sleep(0.3)
			if not width.strip().isdigit():
				print('Please input the number only!!!')
		time.sleep(0.3)
		while not length.isdigit():
			length = input('length (cm) :: ')
			time.sleep(0.3)
			if not length.strip().isdigit():
				print('Please input the number only!!!')
		time.sleep(0.75)
		print('----------------------------')
		print('----------------------------')
		print(f'Square area is {float(width)*float(length)} sq.cm.')
		print('----------------------------')
		print('----------------------------')
		time.sleep(2)

	elif program_number == '2':
		base_width = ''
		height = ''
		time.sleep(0.3)
		print('----------------------------')
		print('----------------------------')
		print('Triangle area calculator')
		print('----------------------------')
		print('----------------------------')
		time.sleep(0.3)	
		while not base_width.isdigit():
			base_width = input('base width (cm) :: ')
			time.sleep(0.3)
			if not base_width.strip().isdigit():
				print('Please input the number only!!!')
		time.sleep(0.3)
		while not height.isdigit():
			height = input('height (cm) :: ')
			if not height.strip().isdigit():
				print('Please input the number only!!!')
		time.sleep(0.75)
		print('----------------------------')
		print('----------------------------')
		print(f'Triangle area is {0.5*float(base_width)*float(height)} sq.cm.')
		print('----------------------------')
		print('----------------------------')
		time.sleep(2)

	elif program_number == '3':
		radius = ''
		time.sleep(0.3)
		print('----------------------------')
		print('----------------------------')
		print('Circle area calculator')
		print('----------------------------')
		print('----------------------------')
		time.sleep(0.3)
		while not radius.isdigit():
			radius = input('radius (cm) :: ')
			if not radius.strip().isdigit():
				print('Please input the number only!!!')
		time.sleep(0.75)
		print('----------------------------')
		print('----------------------------')
		print(f'Circle area is {float(radius)**2} sq.cm.')
		print('----------------------------')
		print('----------------------------')
		time.sleep(2)

	elif program_number.lower() == 'q':
		time.sleep(0.5)
		print('Good bye.')
		time.sleep(0.5)
		print('----------------------------')
		print('----------------------------')
		break

	else:
		time.sleep(0.75)
		print('----------------------------')
		print('----------------------------')
		print('----------------------------')
		print('Something Wrong!!!,\nPlease input a program number again')
		print('----------------------------')
		print('----------------------------')
		print('----------------------------')
		time.sleep(2)
