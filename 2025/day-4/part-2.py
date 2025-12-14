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


def count_and_update_rolls(array, min_rolls, running_count):
	new_array = []
	
	for x, row in enumerate(array):
		new_array.append(row)
		for y, val in enumerate(row):
			accessible_rolls = count_surrounding_rolls(array, x, y)
			
			# can we take this roll?
			if val == "@" and accessible_rolls < min_rolls:
				tmp_row = new_array[ x ]
				tmp_row = tmp_row[:y] + "x" + tmp_row[y + 1:]
				new_array[ x ] = tmp_row
				
				running_count += 1

	
			# Clean up x's from before
			if val == "x":
				tmp_row = new_array[ x ]
				tmp_row = tmp_row[:y] + "." + tmp_row[y + 1:]
				new_array[ x ] = tmp_row
				
	
	return new_array, running_count


def solve_puzzle(array, min_rolls):
	result = 0
	
	while True:
		new_array, new_result = count_and_update_rolls(array, min_rolls, result)
		
		# No updated rolls.
		if new_result == result:
			break
		
		# update new values to put back into function
		result = new_result
		array = new_array
			
		print("new_array", new_array, new_result)
		
	return new_result


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


assertion_test(count_and_update_rolls(['@@@', '@@@', '@@@'], 9, 0), ( ['xxx', 'xxx', 'xxx'], 9)) # base test
assertion_test(count_and_update_rolls(['@@@', '@@@', '@@@'], 8, 0), ( ['xxx', 'x@x', 'xxx'], 8)) # First Loop
assertion_test(count_and_update_rolls(['xxx', 'x@x', 'xxx'], 8, 8), ( ['...', '.x.', '...'], 9)) # Seccond Loop

# Test Example Loop 1
test_start = [
	"..@@.@@@@.",
	"@@@.@.@.@@",
	"@@@@@.@.@@",
	"@.@@@@..@.",
	"@@.@@@@.@@",
	".@@@@@@@.@",
	".@.@.@.@@@",
	"@.@@@.@@@@",
	".@@@@@@@@.",
	"@.@.@@@.@.",
]

test_loop_1 = [
	'..xx.xx@x.', 
	'x@@.@.@.@@', 
	'@@@@@.x.@@', 
	'@.@@@@..@.', 
	'x@.@@@@.@x', 
	'.@@@@@@@.@', 
	'.@.@.@.@@@', 
	'x.@@@.@@@@', 
	'.@@@@@@@@.', 
	'x.x.@@@.x.'
]

test_loop_2 = [
	".......x..",
	".@@.x.x.@x",
	"x@@@@...@@",
	"x.@@@@..x.",
	".@.@@@@.x.",
	".x@@@@@@.x",
	".x.@.@.@@@",
	"..@@@.@@@@",
	".x@@@@@@@.",
	"....@@@...",
]

test_loop_3 = [
	"..........",
	".x@.....x.",
	".@@@@...xx",
	"..@@@@....",
	".x.@@@@...",
	"..@@@@@@..",
	"...@.@.@@x",
	"..@@@.@@@@",
	"..x@@@@@@.",
	"....@@@...",
]

test_loop_4 = [
	"..........",
	"..x.......",
	".x@@@.....",
	"..@@@@....",
	"...@@@@...",
	"..x@@@@@..",
	"...@.@.@@.",
	"..x@@.@@@x",
	"...@@@@@@.",
	"....@@@...",
]

test_loop_5 = [
	"..........",
	"..........",
	"..x@@.....",
	"..@@@@....",
	"...@@@@...",
	"...@@@@@..",
	"...@.@.@@.",
	"...@@.@@@.",
	"...@@@@@x.",
	"....@@@...",
]

test_loop_6 = [
	"..........",
	"..........",
	"...@@.....",
	"..x@@@....",
	"...@@@@...",
	"...@@@@@..",
	"...@.@.@@.",
	"...@@.@@@.",
	"...@@@@@..",
	"....@@@...",
]

test_loop_7 = [
	"..........",
	"..........",
	"...x@.....",
	"...@@@....",
	"...@@@@...",
	"...@@@@@..",
	"...@.@.@@.",
	"...@@.@@@.",
	"...@@@@@..",
	"....@@@...",
]

test_loop_8 = [
	"..........",
	"..........",
	"....x.....",
	"...@@@....",
	"...@@@@...",
	"...@@@@@..",
	"...@.@.@@.",
	"...@@.@@@.",
	"...@@@@@..",
	"....@@@...",
]

test_loop_9 = [
	"..........",
	"..........",
	"..........",
	"...x@@....",
	"...@@@@...",
	"...@@@@@..",
	"...@.@.@@.",
	"...@@.@@@.",
	"...@@@@@..",
	"....@@@...",
]


# Loop 1
assertion_test(count_and_update_rolls(test_start, 4, 0), (test_loop_1, 13))
# Loop 2
assertion_test(count_and_update_rolls(test_loop_1, 4, 13), (test_loop_2, 25))
# Loop 3
assertion_test(count_and_update_rolls(test_loop_2, 4, 25), (test_loop_3, 32))
# Loop 4
assertion_test(count_and_update_rolls(test_loop_3, 4, 32), (test_loop_4, 37))
# Loop 5
assertion_test(count_and_update_rolls(test_loop_4, 4, 37), (test_loop_5, 39))
# Loop 6
assertion_test(count_and_update_rolls(test_loop_5, 4, 39), (test_loop_6, 40))
# Loop 7
assertion_test(count_and_update_rolls(test_loop_6, 4, 40), (test_loop_7, 41))
# Loop 8
assertion_test(count_and_update_rolls(test_loop_7, 4, 41), (test_loop_8, 42))
# Loop 9
assertion_test(count_and_update_rolls(test_loop_8, 4, 42), (test_loop_9, 43))




# Test solve
assertion_test(solve_puzzle(['@@@', '@@@', '@@@'], 9), 9) # base test
assertion_test(solve_puzzle(['@@@', '@@@', '@@@'], 8), 9) # base test
assertion_test(solve_puzzle(['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.'], 9), 71) # base all
assertion_test(solve_puzzle(['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.'], 8), 71) # base all
assertion_test(solve_puzzle(['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.'], 4), 43)