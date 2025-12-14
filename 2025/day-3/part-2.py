#!/usr/bin/env python3




	
def get_banks(string):
	return string.split("\n")
	

def largest_voltage_in_bank(string, n):
	# Get the default result, based on the n size
	result = string[0:n]
	# print("Start", result)
	
	# Start from index 1, cycle through each number
	for val in list(range(1, len(string))):
		# print(result, "--", val, string[val])
		
		# For each char, we cycle through the size of n
		for result_val in list(range(0, n)):
			new_string = string[val + result_val: val + n]
			old_string = result[0: result_val]
			
			updated_num = old_string + "" + new_string
			# print("running num", updated_num)
			
			# check we only ever set to result the size of n
			if updated_num > result and len(updated_num) == n:
				result = updated_num
				
				# stop, as we dont need to check anymore numbers
				continue
			
	# print("result:", result)
	return int(result)

def sum_voltages(array):
	return sum(array)

def solve_puzzle(input):
	banks = get_banks(input)
	highest_bank_voltages = []
	for bank in banks:
		largest = largest_voltage_in_bank(bank, 12)
		highest_bank_voltages.append(largest)
		
	return sum_voltages(highest_bank_voltages)
	

with open('input.txt') as file:
	result = 0
	bank = []
	for line in file:
		largest = largest_voltage_in_bank(line.strip(), 12)
		
		print(line.strip(), ", highest voltage in this bank: ", largest)
		
		bank.append(largest)

	result = sum_voltages(bank)
	
	# Output value
	print(f"The total output joltage is {result}.")
########################################################################

# Test Cases:

def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"
	
# Test spltting strings in to banks
assertion_test(
	get_banks("1\n1"),
	["1","1"]
)

assertion_test(
	get_banks(
		"987654321111111\n811111111111119\n234234234234278\n818181911112111",
	),
	[
		"987654321111111",
		"811111111111119",
		"234234234234278",
		"818181911112111"
	]
)


# Test finding largest possible joltage

assertion_test(largest_voltage_in_bank("11", 1), 1)
assertion_test(largest_voltage_in_bank("91", 1), 9)
assertion_test(largest_voltage_in_bank("91", 1), 9)
assertion_test(largest_voltage_in_bank("123454321", 1), 5)
assertion_test(largest_voltage_in_bank("11", 2), 11)
assertion_test(largest_voltage_in_bank("191", 2), 91)
assertion_test(largest_voltage_in_bank("91000", 2), 91)
assertion_test(largest_voltage_in_bank("191111119", 2), 99)
assertion_test(largest_voltage_in_bank("111", 3), 111)
assertion_test(largest_voltage_in_bank("111000", 3), 111)
assertion_test(largest_voltage_in_bank("1110009", 3), 119)
assertion_test(largest_voltage_in_bank("911911999", 3), 999)
assertion_test(largest_voltage_in_bank("111111", 6), 111111)
assertion_test(largest_voltage_in_bank("9119111019999", 6), 999999)
assertion_test(largest_voltage_in_bank("111111111111", 12), 111111111111)
assertion_test(largest_voltage_in_bank("91919191919191919191919", 12), 999999999999)

assertion_test(largest_voltage_in_bank("987654321111111", 12), 987654321111)
assertion_test(largest_voltage_in_bank("811111111111119", 12), 811111111119)
assertion_test(largest_voltage_in_bank("234234234234278", 12), 434234234278)
assertion_test(largest_voltage_in_bank("818181911112111", 12), 888911112111)

# Test sum voltages
assertion_test(sum_voltages([11]), 11)
assertion_test(sum_voltages([11, 22]), 33)
assertion_test(sum_voltages([98, 89, 78, 92]), 357)


# Test example data
assertion_test(solve_puzzle("11"), 11)
assertion_test(solve_puzzle("11\n22"), 33)
assertion_test(solve_puzzle("11\n22\n33"), 66)
assertion_test(solve_puzzle("123\n123"), 246)
assertion_test(solve_puzzle("123\n234\n345"), 702)
assertion_test(solve_puzzle("987654321111\n811111111119\n434234234278\n888911112111"), 3121910778619)