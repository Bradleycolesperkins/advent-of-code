#!/usr/bin/env python3




	
def count_surrounding_rolls(array, x, y):
	surrounding_rolls = 0
	
	# Loop though a 3 by 3 grid around the x, y co-ords
	for rows in list(range(-1, 2, 1)): 
		# get row from array
		row_x = x + rows
		
		# in top or bottom row, skip
		if row_x < 0 or row_x >= len(array): 
			continue
		
		row = array[ row_x ]
		for cols in list(range(-1, 2, 1)): 
			# get col from row in array
			col_y = y + cols
			
			# in top or bottom row, skip
			if col_y < 0 or col_y >= len(row): 
				continue
			
			val = row[col_y: col_y + 1]
			
			# skip middle
			if rows == 0 and cols == 0:
				continue
			
			# Check if we have a roll
			if val == "@": 
				# Increment
				surrounding_rolls += 1
			
	return surrounding_rolls
	
def diagram_to_array(diagram):
	return diagram.split("\n")


def solve_puzzle(array, min_rolls):
	result = 0
	for x, row in enumerate(array):
		for y, val in enumerate(row):
			accessible_rolls = count_surrounding_rolls(array, x, y)
			
			# can we take this roll?
			if val == "@" and accessible_rolls < min_rolls:
				
				result += 1
				
	return result

with open('input.txt') as file:
	result = 0
	array = []
	for line in file:
		array.append(line.strip())
	
	removable_rolls = solve_puzzle(array, 4)
	result += removable_rolls

	
	# Output value
	print(f"There are {result} rolls of paper that can be accessed by a forklift.")

########################################################################

# Test Cases:

def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"
	

# Test high and low numbers to integer value
	
diagram = "@@@\n@@@\n@@@"
array = diagram_to_array(diagram)

assertion_test(count_surrounding_rolls(array, 1, 1), 8) # Test Center
assertion_test(count_surrounding_rolls(array, 0, 0), 3) # Test Top Left
assertion_test(count_surrounding_rolls(array, 0, 2), 3) # Test Top Right
assertion_test(count_surrounding_rolls(array, 2, 0), 3) # Test Bottom Left 
assertion_test(count_surrounding_rolls(array, 2, 2), 3) # Test Bottom Right

assertion_test(
	count_surrounding_rolls([
	"..@@.@@@@.",
	"@@@.@.@.@@"
	], 0, 2)
, 3)

assertion_test(
	count_surrounding_rolls([
	"..@@.@@@@.",
	"@@@.@.@.@@"
	], 1, 0)
, 1)


# Test solve
assertion_test(solve_puzzle(['@@@', '@@@', '@@@'], 9), 9) # base test
assertion_test(solve_puzzle(['@@@', '@@@', '@@@'], 8), 8) # base test
assertion_test(solve_puzzle(['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.'], 8), 70) # base all
assertion_test(solve_puzzle(['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.'], 4), 13)