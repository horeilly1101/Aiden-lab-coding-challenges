# Hugh O'Reilly
# Aiden Lab Coding Challenge
# 1B Number to String Challenge

import sys

def find_arithmetic_sequence(num_seq):
	'''
	Takes a sequence of digits as input and outputs a sequence of
	tuples, where the digits in the tuples are the indices of the
	inputted sequence where there are arithmetic sequences.

	If there are no arithmetic sequences, return an empty sequence
	'''
	# Create an empty sequence
	out_seq = []

	# Iterate through the sequence and search for arithmetic
	# sequences
	for idx in range(len(num_seq) - 1):
		cont = True
		diff = num_seq[idx + 1] - num_seq[idx]
		tup = [idx, idx + 1]
		i = 1

		while cont:
			if idx + i + 1 < len(num_seq):
				if num_seq[idx + i + 1] - num_seq[idx + i] == diff:
					tup.append(idx + i + 1)
					i += 1
				else:
					cont = False
			else:
				cont = False

		if len(tup) > 2:
			out_seq.append(tuple(tup))

	return out_seq

def find_geometric_sequence(num_seq):
	'''
	Takes a sequence of digits as input and outputs a sequence of
	tuples, where the digits in the tuples are the indices of the
	inputted sequence where there are geometric sequences.

	If there are no geometric sequences, return an empty sequence
	'''
	# Create an empty sequence
	out_seq = []

	# Iterate through the sequence and search for geometric
	# sequences
	for idx in range(len(num_seq) - 1):

		if num_seq[idx]:
			cont = True
			quot = num_seq[idx + 1] / num_seq[idx]
			tup = [idx, idx + 1]
			i = 1

			while cont:
				if num_seq[idx] * quot != num_seq[idx + 1]:
					break

				if idx + i + 1 < len(num_seq) and num_seq[idx + 1]:
					if num_seq[idx + i + 1] / num_seq[idx + i] == quot and \
						num_seq[idx + i] * quot == num_seq[idx + i + 1]:
						tup.append(idx + i + 1)
						i += 1
					elif idx + i + 2 < len(num_seq):
						if int(str(num_seq[idx + i + 1]) + str(num_seq[idx + i + 2])) \
							/ num_seq[idx + i] == quot and num_seq[idx + i] * quot == \
							int(str(num_seq[idx + i + 1]) + str(num_seq[idx + i + 2])):
							tup.append(idx + i + 1)
							tup.append(idx + i + 2)
							cont = False
						else:
							cont = False
					else:
						cont = False
				else:
					cont = False

			if len(tup) > 2:
				out_seq.append(tuple(tup))

	return out_seq

def find_years(num_seq):
	'''
	Takes a sequence of digits as input and outputs a sequence of
	tuples, where the digits in the tuples are the indices of the
	inputted sequence where there are years.

	If there are no years, return an empty sequence

	Note: I decided to only allow years after 1199.  Personally,
	I feel these four digit numbers are more often associated with
	years than the ones I excluded.  Also, I decided to include years as
	a criterion becase a) they're manageable chunks of digits and b)
	if something noticeable happened on a particular year chosen by
	the algorithm, that only helps the user memorize the inputted
	number better.
	'''
	# Create an empty sequence
	out_seq = []
	cont = True

	# Iterate through the sequence and search for years
	for idx in range(len(num_seq) - 3):
		year = ""
		i = 0
		while i < 4:
			year = year + str(num_seq[idx + i])
			i += 1
		if year[0] == "1":
			if int(year[1]) > 1:
				out_seq.append((idx, idx + 1, idx + 2, idx + 3))
		elif year[0] == "2":
			if (int(year[1]) == 0) and (int(year[2]) < 2):
				out_seq.append((idx, idx + 1, idx + 2, idx + 3))

	return out_seq

def find_product(num_seq):
	'''
	Takes a sequence of digits as input and outputs a sequence of
	tuples, where the digits in the tuples are the indices of the
	inputted sequence where there are two digits followed by their product.

	If there are no multiples, return an empty sequence
	'''
	# Create an empty sequence
	out_seq = []
	cont = True

	# Iterate through the input sequence and search for products
	for idx in range(len(num_seq) - 2):
		tup = [idx, idx + 1]

		# Consider the case where the product is 1 digit
		if num_seq[idx] * num_seq[idx + 1] == num_seq[idx + 2]:
			tup.append(idx + 2)
			out_seq.append(tuple(tup))

		# Consider the case where the product is 2 digits
		elif num_seq[idx] * num_seq[idx + 1] >= 10 and idx < len(num_seq) - 3:
			if num_seq[idx] * num_seq[idx + 1] == \
				int(str(num_seq[idx + 2]) + str(num_seq[idx + 3])):
				tup.append(idx + 2)
				tup.append(idx + 3)
				out_seq.append(tuple(tup))
	return out_seq

def find_symmetry(num_seq):
	'''
	Takes a sequence of digits as input and outputs a sequence of
	tuples, where the digits in the tuples are the indices of the
	inputted sequence where there is symmetry.
	(Only returns tuples of length 3 or greater)

	If there is no symmetry, return an empty sequence
	'''
	# Create an empty sequence
	out_seq = []
	cont = True

	# Iterate through the sequence and search for symmetry
	for idx in range(len(num_seq) - 1):
		tup1 = []
		tup2 = []

		# Find symmetry around two like numbers
		if num_seq[idx] == num_seq[idx + 1]:
			tup1 = [idx, idx + 1]
			i = 1
			cont1 = True
			while cont1:
				if idx - i >= 0 and idx + 1 + i < len(num_seq):
					if num_seq[idx - i] == num_seq[idx + 1 + i]:
						tup1 = [idx - i] + tup1 + [idx + 1 + i]
						i += 1
					else:
						cont1 = False
				else:
					cont1 = False
			if len(tup1) > 0:
				out_seq.append(tuple(tup1))

		# Find symmetry around a single number
		if idx - 1 >= 0:
			if num_seq[idx - 1] == num_seq[idx + 1]:
				tup2 = [idx - 1, idx, idx + 1]
				i = 1
				cont2 = True
				while cont2:
					if idx - 1 - i >= 0 and idx + 1 + i < len(num_seq):
						if num_seq[idx - i - 1] == num_seq[idx + 1 + i]:
							tup2 = [idx - i - 1] + tup2 + [idx + 1 + i]
							i += 1
						else:
							cont2 = False
					else:
						cont2 = False
			if len(tup2) > 0:
				out_seq.append(tuple(tup2))

	return out_seq

def string_to_seq(in_str):
	'''
	Converts a string of digits to a sequence of digits
	'''
	out_seq = []

	for char in in_str:
		out_seq.append(int(char))

	return out_seq

def label_and_combine_tuples(num_seq):
	'''
	Takes a sequence of digits as input.  Calls the "find" functions, labels
	the outputted tuples, and then combines the tuples in a sequence that 
	it then outputs
	'''
	arithmetic = find_arithmetic_sequence(num_seq)
	arithmetic_tup = []
	for elem in arithmetic:
		arithmetic_tup.append((elem, "(arithmetic)"))

	geometric = find_geometric_sequence(num_seq)
	geometric_tup = []
	for elem in geometric:
		geometric_tup.append((elem, "(geometric)"))

	years = find_years(num_seq)
	years_tup = []
	for elem in years:
		years_tup.append((elem, "(year)"))

	product = find_product(num_seq)
	product_tup = []
	for elem in product:
		product_tup.append((elem, "(product)"))

	symmetry = find_symmetry(num_seq)
	symmetry_tup = []
	for elem in symmetry:
		symmetry_tup.append((elem, "(symmetry)"))

	return arithmetic_tup + geometric_tup + years_tup + product_tup + symmetry_tup

def num_to_word(in_str):
	'''
	Takes a string of digits as input and outputs a mix of numbers
	and letters to help remember the original number

	NOTE: I chose to order the intervals in nondecreasing order
	by their last index value because it can be shown that greedily
	selecting these intervals from smallest to largest such that no
	intervals overlap is an optimal way to align the most intervals.
	In fact, we proved this result in COMP 182 at Rice University.
	I thought this would be a good way to approach this particular problem
	because the more patterns there are, the easier it is to memorize
	the number.
	'''
	# Convert the inputted string into a sequence of digits
	num_seq = string_to_seq(in_str)

	# Label and combine the tuples outputted by the "find" functions
	label_tup = label_and_combine_tuples(num_seq)

	# Sort the tuples of indices in nondecreasing order by their last 
	# index value
	label_tup.sort(key = lambda tup: tup[0][-1])
	
	# Get rid of overlapping indices
	order_tup = [label_tup[0]]
	for tup in label_tup:
		if tup[0][0] > order_tup[-1][0][-1]:
			order_tup.append(tup)

	# Order the digits back into a string
	out_string = ""
	i = 0
	count = 0
	while i < len(in_str):
		if len(order_tup) > 0:
			if i in order_tup[0][0]:
				if i > 0:
					out_string += " - "
				for idx in order_tup[0][0]:
					out_string += in_str[idx]
				out_string += " " + order_tup[0][1]
				i += len(order_tup[0][0])
				order_tup.pop(0)
				count = 0

			else:
				if (count % 4) == 0 and i > 0:
					out_string += " - "
				out_string += in_str[i]
				i += 1
				count += 1

		else:
			if (count % 4) == 0 and i > 0:
				out_string += " - "
			out_string += in_str[i]
			i += 1
			count += 1

	return out_string 
	
# Run num_to_word at command line in terminal
if len(sys.argv) == 2:
	if len(sys.argv[1]) > 9 and len(sys.argv[1]) < 21:
		print " "
		print "Input:", sys.argv[1]
		print "Output:", num_to_word(sys.argv[1])
		print " "
		print "(arithmetic), the digits form an arithmetic sequence"
		print "(geometric), the digits form a geometric sequence"
		print "(year), the digits represent a year after 1199"
		print "(product), the last number is the product of the first two digits"
		print "(symmetry), the digits are symmetric"
		print " "
	else:
		# Error message
		print " "
		print "Please input a 10-20 digit number"
		print " "




