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
	
	for row in rows:
		columns = row.split(" ");
		# Remove empty strings from array
		columns2 = list(filter(None, columns))
		
		results.append(columns2)
	
	return results


def sumColumns(array):
	calculation_row = len(array) - 1
	
	result = 0
	# Loop each calculation value
	for calculation_index in range(0, len(array[calculation_row])):
		
		column_result = 0
		
		# Now loop each column to get the values
		for column_index in range(0, len(array) - 1):

			val = int(array[column_index][calculation_index].strip())

			if array[calculation_row][calculation_index] == "+":
				column_result = column_result + val
			else:
				# could be zero, and thus a multiple of zero is always zero
				if column_index == 0:
					column_result = 1
					
				column_result = column_result * val
		
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
	assertion_test(getColumns("123 123\n* *"), [["123", "123"],["*", "*"]])
	assertion_test(getColumns("123 123\n123 123\n* *"), [["123", "123"],["123", "123"],["*", "*"]])
	assertion_test(getColumns("1 2\n3 4\n5 6\n7 8\n9 10\n* *"), [["1","2"],["3","4"],["5","6"],["7","8"],["9","10"],["*", "*"]])
	
	
	# Assert addition
	assertion_test(sumColumns([["1"],["+"]]), 1)
	assertion_test(sumColumns([["1"],["2"],["3"],["+"]]), 6)
	assertion_test(sumColumns([["1", "1"],["2", "2"],["3", "3"],["+", "+"]]), 12)
	assertion_test(sumColumns([["1", "1", "1"],["2", "2", "2"],["3", "3", "3"],["+", "+", "+"]]), 18)
	
	# Assert multiplication
	assertion_test(sumColumns([["1"],["*"]]), 1)
	assertion_test(sumColumns([["1"],["2"],["3"],["*"]]), 6)
	assertion_test(sumColumns([["1", "1"],["2", "2"],["3", "3"],["*", "*"]]), 12)
	assertion_test(sumColumns([["1", "1", "1"],["2", "2", "2"],["3", "3", "3"],["*", "*", "*"]]), 18)
	assertion_test(sumColumns([["2", "2", "2"],["2", "2", "2"],["3", "3", "3"],["*", "*", "*"]]), 36)
	
	
	assertion_test(solve("123 328  51 64\n 45 64  387 23\n6 98  215 314\n*   +   *   + "), 4277556)
	
def main():
	with open('input.txt') as file:
		data = file.read()
		result = solve(data)
		
		# Output value
		print(f"the grand total is {result}.")
	
if __name__ == "__main__":
	main()
	run_tests()