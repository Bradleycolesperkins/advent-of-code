#!/usr/bin/env python3
import math

def get_ranges(string):
	# get ranges from string based on commas
	return string.split(",");

def get_start_and_end_of_ranges(string):
	# Break up range with hyphen
	range_values = string.split("-");
	return int(range_values[0]), int(range_values[1])


def find_invalid_ids(start, end):
	# Loop through start to finish 
	results = []
	for value in list(range(start, end + 1)):
		is_value_valid = is_valid_id(value)
		if is_value_valid == False:
			results.append(value)
	return results

def split_string_into_x(string, amount):
	# Get length
	string_length = len(str(string))
	
	# get chunks
	chunks = int( string_length / amount )
	result = []
	
	for val in list(range(0, amount)):
		start = val * chunks
		end = start + chunks
		
		# loop through, and get string in chunks, starting with 0 * the chunk size. The ending start plus chunk size
		result.append(str(string)[start:end])
	
	return result

def is_valid_id(number):
	# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. 
	# So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
	
	# if its empty, its got to be valid
	if len(str(number)) == 0: 
		return True

	#	12341234 == 1234
	#	123123123 == 123
	#	1212121212 == 12
	#	1111111 ==	   1
	
	# Maximum patterns is equal to the size of the string, ie 12341234 would be 8 possible patterns (even though 
	max_potential_pattern = len(str(number))
	
	# try every pattern from length of string to max
	for potential_pattern_length in list(range(2, max_potential_pattern + 1)):
		
		# if its divisible by the potential_pattern_length, lets check if they are a pattern
		# ie. if the string is 12341234, 7 doesnt go in to 8 and therefore cant be a pattern
		if len(str(number)) % potential_pattern_length == 0:
			split_string = split_string_into_x(number, potential_pattern_length)
			
			# now check if they are a pattern
			result = is_array_all_the_same(split_string)
			if result == True:
				return False
			
	return True


def is_array_all_the_same(array):
	
	# Loop through array, and check they are all the same
	result = True
	for indexx, x in enumerate(array):
		for indexy, y in enumerate(array):
			if x != y and indexx != indexy:
				return False
	return result;
	
def get_invalid_ids_from_string(string):
	results = []
	ranges = get_ranges(string)
	for range in ranges:
		# Get start and ends from range
		start, end = get_start_and_end_of_ranges(range)
		
		# get invalid ids from start and end values
		invalid_ids = find_invalid_ids(start, end)
		
		# add to results array
		results.extend(invalid_ids)
	
	return results
		
		
def solve_puzzle(string):
	invalid_ids = get_invalid_ids_from_string(string)
	
	running_result = 0
	for value in invalid_ids:
		running_result += value
		
	return running_result
	
	
'''
with open('input.txt') as file:
	result = 0
	for line in file:
		line = line.strip()
		result = solve_puzzle(line)

	# Output value
	print(f"Adding up all the invalid IDs in this example produces {result}.")
'''

########################################################################

# Test Cases:

def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# Base Range Tests
assertion_test(get_ranges(""),[''])
assertion_test(get_ranges("11-22,95-115"),["11-22", "95-115"])

# Base Start and End ranges
assertion_test(get_start_and_end_of_ranges("11-22"), (11, 22))
assertion_test(get_start_and_end_of_ranges("95-115"), (95, 115))

# Base find invalid IDS
assertion_test(find_invalid_ids(1, 2), [])
assertion_test(find_invalid_ids(1, 3), [])	
assertion_test(find_invalid_ids(11, 22), [11, 22])
assertion_test(find_invalid_ids(95, 115), [99, 111])
assertion_test(find_invalid_ids(998, 1012), [999, 1010])
assertion_test(find_invalid_ids(1188511880, 1188511890), [1188511885])
assertion_test(find_invalid_ids(222220, 222224), [222222])
assertion_test(find_invalid_ids(1698522, 1698528), [])
assertion_test(find_invalid_ids(446443, 446449), [446446])
assertion_test(find_invalid_ids(38593856, 38593862), [38593859.])

# Base invalid pattern
assertion_test(is_valid_id(95), True)
assertion_test(is_valid_id(954), True)
assertion_test(is_valid_id(1212), False)
assertion_test(is_valid_id(99), False)
assertion_test(is_valid_id(1010), False)
assertion_test(is_valid_id(1188511885), False)
assertion_test(is_valid_id(222222), False)
assertion_test(is_valid_id(446446), False)
assertion_test(is_valid_id(38593859), False)

# Invalid ids tests
assertion_test(get_invalid_ids_from_string("0-0"),[])
assertion_test(get_invalid_ids_from_string("11-11"),[11])
assertion_test(get_invalid_ids_from_string("11-22"),[11,22])
assertion_test(get_invalid_ids_from_string("95-115"),[99,111])
assertion_test(get_invalid_ids_from_string("998-1012"),[999,1010])
assertion_test(get_invalid_ids_from_string("1188511880-1188511890"),[1188511885])
assertion_test(get_invalid_ids_from_string("222220-222224"),[222222])
assertion_test(get_invalid_ids_from_string("1698522-1698528"),[])
assertion_test(get_invalid_ids_from_string("446443-446449"),[446446])
assertion_test(get_invalid_ids_from_string("38593856-38593862"),[38593859])
assertion_test(get_invalid_ids_from_string("565653-565659"),[565656])
assertion_test(get_invalid_ids_from_string("824824821-824824827"),[824824824])
assertion_test(get_invalid_ids_from_string("2121212118-2121212124"),[2121212121])
assertion_test(get_invalid_ids_from_string("95-115,998-1012"),[99,111,999,1010])
assertion_test(get_invalid_ids_from_string("95-115,998-1012,1188511880-1188511890"),[99,111,999,1010,1188511885])
assertion_test(get_invalid_ids_from_string("95-115,998-1012,1188511880-1188511890,222220-222224"),[99,111,999,1010,1188511885,222222])
assertion_test(
	get_invalid_ids_from_string(
		"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
	),
	[11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656, 824824824, 2121212121]
)


# Solve puzzle tests
assertion_test(solve_puzzle("0-0"),0)
assertion_test(solve_puzzle("11-11"),11)
assertion_test(solve_puzzle("11-22"),33)
assertion_test(
	solve_puzzle(
		"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
	),
	4174379265
	
)		
		
assertion_test(split_string_into_x(12341234, 2), ["1234", "1234"])
assertion_test(split_string_into_x(123123123, 3), ["123", "123", "123"])
assertion_test(split_string_into_x(1212121212, 5), ["12", "12", "12", "12", "12"])
assertion_test(split_string_into_x(12345678, 2), ["1234", "5678"])


assertion_test(is_array_all_the_same([12, 34]), False)
assertion_test(is_array_all_the_same([12, 12, 12]), True)
