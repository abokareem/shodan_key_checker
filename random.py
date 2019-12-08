import random

while True:
	def my_array(length=32):
		numbers  = '0123456789'
		LETTERS  = 'ABCDEFGHIJKLMNOPRSTUVZ'
		letters	 = 'abcdefghijklmnoprstuvz'
		#return ''.join(random.choice(numbers)			# numbers
		#return ''.join(random.choice(LETTERS)			# LETTERS
                #return ''.join(random.choice(letters)			# letters
		return ''.join(random.choice(numbers + LETTERS + letters) 	# numbers and LETTERS and letters
	for i in range(length))
	print (my_array(32))
