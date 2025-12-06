#!/usr/bin/env python3




	
def get_banks(string):
	return string.split("\n")
	

def voltages_to_integer(low, high):
	return int(f"{low}{high}")

def largest_voltage_in_bank(string):
	if len(string) == 2:
		return voltages_to_integer(int(string[0]), int(string[1]))
	
	# Loop through string, and keep track of highest running tenth and oneth value. ie 5 and 4 is 54.
	tenth_value = int(string[0])
	oneth_value = int(string[1])
	
	# get the next value starting from 2nd value (1st index) onwards.
	for count in list(range(1, len(string))):
		value = int(string[count])
		
		# if the value is greater than the tenth, and we have another value in the range, this autoamtically means
		# we have a new highest value
		if value > tenth_value and count + 1 < len(string):
			tenth_value = value # we have a new higest 10th value
			oneth_value = 0 # reset so the next count will update
			
		# check the oneth value, if we have a new one. ie we have 
		# tenth = 5 and oneth = 3. if the value us 4. then 4 > 3, inferring 54 is higher than 53
		elif value > oneth_value:
			oneth_value = value
		
	
	return voltages_to_integer(tenth_value, oneth_value)

def sum_voltages(array):
	return sum(array)

def solve_puzzle(input):
	banks = get_banks(input)
	highest_bank_voltages = []
	for bank in banks:
		largest = largest_voltage_in_bank(bank)
		highest_bank_voltages.append(largest)
		
	return sum_voltages(highest_bank_voltages)
	


with open('input.txt') as file:
	result = 0
	bank = []
	for line in file:
		largest = largest_voltage_in_bank(line.strip())
		
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


# Test high and low numbers to integer value
assertion_test(voltages_to_integer(1,1), 11)
assertion_test(voltages_to_integer(1,2), 12)
assertion_test(voltages_to_integer(9,9), 99)

# Test finding largest possible joltage
assertion_test(largest_voltage_in_bank("11"), 11)
assertion_test(largest_voltage_in_bank("23"), 23)
assertion_test(largest_voltage_in_bank("123"), 23)
assertion_test(largest_voltage_in_bank("1234"), 34)
assertion_test(largest_voltage_in_bank("12344"), 44)
assertion_test(largest_voltage_in_bank("44321"), 44)
assertion_test(largest_voltage_in_bank("54321"), 54)
assertion_test(largest_voltage_in_bank("987654321111111"), 98)
assertion_test(largest_voltage_in_bank("1819"), 89)
assertion_test(largest_voltage_in_bank("3511135"), 55)
assertion_test(largest_voltage_in_bank("11145"), 45)
assertion_test(largest_voltage_in_bank("811111111111119"), 89)

# Test sum voltages
assertion_test(sum_voltages([11]), 11)
assertion_test(sum_voltages([11, 22]), 33)
assertion_test(sum_voltages([98, 89, 78, 92]), 357)


# Test example data
assertion_test(solve_puzzle("11"), 11)
assertion_test(solve_puzzle("11\n22"), 33)
assertion_test(solve_puzzle("11\n22\n33"), 66)
assertion_test(solve_puzzle("123\n123"), 46)
assertion_test(solve_puzzle("123\n234\n345"), 102)
assertion_test(solve_puzzle("987654321111111\n811111111111119\n234234234234278\n818181911112111"), 357)