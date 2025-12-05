#!/usr/bin/env python3

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



def is_valid_id(number):
	# looking for any ID which is made only of some sequence of digits repeated twice
	# So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs
	
	# if its empty, its got to be valid
	if len(str(number)) == 0: 
		return True
	
	# if its odd length, it cant have a pattern therefore its valid
	if ( len(str(number)) % 2 ) == 1:
		return True
	
	# Split string in half, if the first equals the second then we have a pattern (palindrone)
	string_size = len(str(number))
	half_string_size = int(string_size / 2)
	
	# Get first and second half of the numbers
	first_half_of_string = str(number)[0:half_string_size]
	second_half_of_string = str(number)[half_string_size:string_size]
	
	# Check if they equal the same thing, if they do then its an invalid id
	return first_half_of_string != second_half_of_string
	
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
	
	

with open('input.txt') as file:
	result = 0
	for line in file:
		line = line.strip()
		result = solve_puzzle(line)

	# Output value
	print(f"Adding up all the invalid IDs in this example produces {result}.")


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
assertion_test(find_invalid_ids(95, 115), [99])
assertion_test(find_invalid_ids(998, 1012), [1010])
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
assertion_test(
	get_invalid_ids_from_string(
		"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
	),
	[11, 22, 99, 1010, 1188511885, 222222, 446446, 38593859]
)

# Solve puzzle tests
assertion_test(solve_puzzle("0-0"),0)
assertion_test(solve_puzzle("11-11"),11)
assertion_test(solve_puzzle("11-22"),33)
assertion_test(
	solve_puzzle(
		"11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
	),
	1227775554
)







		