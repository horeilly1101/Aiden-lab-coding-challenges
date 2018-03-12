# Hugh O'Reilly
# Aiden Lab Coding Challenge
# 1A Bucket Challenge

import sys

def bucket_challenge(bucket_sizes, target_value):
	'''
	Takes an array of bucket sizes and a target value

	Restrictions on input: we assume that the values in
	bucket_sizes are greater than 0

	Returns a 1 if the buckets can be used to reach the target value and
	returns a 0 if not
	'''
	# Check the base cases
	if target_value == 0:
		return 1
	elif target_value < 0:
		return 0

	# Check the recursive cases
	else:
		for bucket in bucket_sizes:
			if bucket_challenge(bucket_sizes, target_value - bucket):
				return 1
		return 0

# Run bucket_challenge at command line in terminal
if len(sys.argv) == 3:
	input_seq = sys.argv[1].split(",")
	bucket_sizes = []
	target_value = int(sys.argv[2])
	for num in input_seq:
		bucket_sizes.append(int(num))
	print " "
	print "buckets:", bucket_sizes
	print "target value:", target_value
	print "result:", bucket_challenge(bucket_sizes, target_value)
	print " "

## Test Cases

# print "Test 1"
# print "Expect: 1"
# print "Output:", bucket_challenge([5, 7], 5)

# print " "

# print "Test 2"
# print "Expect: 1"
# print "Output:", bucket_challenge([5, 7], 33)

# print " "

# print "Test 3"
# print "Expect: 0"
# print "Output:", bucket_challenge([5, 7], 9)

# print " "

# print "Test 4"
# print "Expect: 0"
# print "Output:", bucket_challenge([2, 11], 9)

# print " "

# print "Test 5"
# print "Expect: 1"
# print "Output:", bucket_challenge([2, 9, 17], 19)

# print " "

# print "Test 6"
# print "Expect: 1"
# print "Output:", bucket_challenge([3, 11, 21], 492)

	


