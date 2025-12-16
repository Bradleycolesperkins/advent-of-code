#!/usr/bin/env python3
def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# ------------------------------------
	
def getColumns(data):
	# Convert rows
	rows = data.split("\n");
	if len(rows) <= 1:
		return []
	
	results = []
	
	# Workout how many columns we have by the calculations row
	calculations_row = rows[len(rows) - 1]
	calculation_columns = list(filter(None, calculations_row.split(" ")))
	
	
	# Initialise blank array of sizes set to 0
	size_of_column_chars = []
	for i in range(0, len(calculation_columns)):
		size_of_column_chars.append(0)
	
	# Get the size of the numbers, trailing or prepending zeros, and store size in an array
	char_counter = 0
	col_counter = 0
	for index, char in enumerate(rows[0]):
		
		if char == " ":
			# Loop down to check we all have empty zeros
			full_column_of_zeros = True
			for row in rows:
				# check if there is a char at this position in every row				
				if row[index] != " ":
					full_column_of_zeros = False
					break
				
				
			if full_column_of_zeros == False:
				char_counter += 1
				continue

			size_of_column_chars[col_counter] = char_counter
			
			char_counter = 0
			col_counter += 1			
		else:
			char_counter += 1

	# Incase we finish loop and not set it
	if char_counter != 0:
		size_of_column_chars[col_counter] = char_counter
	
	
	results = []
	
	for row in rows:
		updated_columns = []

		# insert in chunks of the size of the column chars
		start = 0
		
		for index, column in enumerate(size_of_column_chars):
			# Att columns based on the char val
			end = start + column
			
			# get stubstring
			substring = row[ start : end ]
			
			# Push on by 1 with the whitespace
			start = int(( end + 1))
			
			updated_columns.append(substring)
			

		results.append(updated_columns)	
		
		
	return results


def sumColumns(array):
	calculation_row = len(array) - 1
	
	result = 0
	# Loop each calculation value
	for calculation_index in range(0, len(array[calculation_row])):
		
		column_result = 0
		nth_numbers = []
		
		
		for column_index in range(0, len(array) - 1):
			val = array[column_index][calculation_index];
			
			for char_index in range(0, len(val)):
				if char_index >= len(nth_numbers):
					nth_numbers.append("")
				
				char_val = val[char_index]
				
				if char_val.strip() != "":
					# Concat and it to our nth numbers
					previous_nth_val = nth_numbers[char_index]
					new_val = previous_nth_val + char_val
					nth_numbers[char_index] = new_val
		
		# Now loop each column to get the values
		for index, val in enumerate(nth_numbers):
			# Check if its + or * in the col
			if "+" in array[calculation_row][calculation_index].strip(""):
				column_result = column_result + int(val)
			else:
				# could be zero, and thus a multiple of zero is always zero
				if index == 0:
					column_result = 1

				column_result = column_result * int(val)
				
		result += column_result

	return result
	
def solve(data):
	columns = getColumns(data)
	result = sumColumns(columns)
	return result
	
def run_tests():
	# Tests to return ID ranges and Ingredient ranges
	assertion_test(getColumns(""), [])
	assertion_test(getColumns("123\n*"), [["123"],["*"]])
	assertion_test(getColumns("123 123\n  *   *"), [["123", "123"],["  *", "  *"]])
	assertion_test(getColumns("123 123\n123 123\n  *   *"), [["123", "123"],["123", "123"],["  *", "  *"]])
	
	# Test with whitespaces
	assertion_test(getColumns("1 2 \n3 4 \n5 6 \n7 8 \n9 10\n*  *"), [["1","2 "],["3","4 "],["5","6 "],["7","8 "],["9","10"],["*", " *"]])
	assertion_test(getColumns(" 1 2 \n 3 4 \n 5 6 \n 7 8 \n90 10\n *  *"), [[" 1","2 "],[" 3","4 "],[" 5","6 "],[" 7","8 "],["90","10"],[" *", " *"]])
	assertion_test(getColumns("  1  2 \n  3  4 \n  5  6 \n  7  8 \n999 111\n  *   *"), [['  1', ' 2 '], ['  3', ' 4 '], ['  5', ' 6 '], ['  7', ' 8 '], ['999', '111'], ['  *', '  *']])
	
	# Assert addition
	assertion_test(sumColumns([["1"],["+"]]), 1)
	assertion_test(sumColumns([["1"],["2"],["3"],["+"]]), 123)
	assertion_test(sumColumns([["1", "1"],["2", "2"],["3", "3"],["+", "+"]]), 246)
	assertion_test(sumColumns([["1", "1", "1"],["2", "2", "2"],["3", "3", "3"],["+", "+", "+"]]), 369)
	assertion_test(sumColumns([["1", "", ""],["4", "3", "1"],["6", "2", "3"],["+", "+", "+"]]), 191)
	
	# Assert multiplication
	assertion_test(sumColumns([["1"],["*"]]), 1)
	assertion_test(sumColumns([["1"],["2"],["3"],["*"]]), 123)
	assertion_test(sumColumns([["1", "1"],["2", "2"],["3", "3"],["*", "*"]]), 246)
	assertion_test(sumColumns([["1", "1", "1"],["2", "2", "2"],["3", "3", "3"],["*", "*", "*"]]), 369)
	assertion_test(sumColumns([["2", "2", "2"],["2", "2", "2"],["3", "3", "3"],["*", "*", "*"]]), 669)
	
	
	assertion_test(solve("123 328  51 64\n 45 64  387 23\n6 98  215 314\n*   +   *   + "), 1484)
	
	
	
	assertion_test(getColumns("123\n*"), [["123"],["*"]])
	assertion_test(getColumns("123 123\n  *   *"), [["123", "123"],["  *", "  *"]])
	assertion_test(getColumns("123 123\n123 123\n  *   *"), [["123", "123"],["123", "123"],["  *", "  *"]])
	
def main():
	with open('input.txt') as file:
		data = file.read()
		result = solve(data)
		
		# Output value
		print(f"the grand total is {result}.")
	
if __name__ == "__main__":
	main()
#	run_tests()