#!/usr/bin/env python3
def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# ------------------------------------
	
def draw(string, index, char):
	new_string = string[0:index] + char + string[index + 1:]
	return new_string

def drawLineBelow(row_index, char_index, rows):
	# Check row below exists
	if row_index + 1 >= len(rows):
		return rows
	
	char_to_update = rows[row_index + 1][char_index]
	row = rows[row_index + 1]
	
	if char_to_update == "^":
		# Splitter found, add left and right instead
		drawLineBelow(row_index, char_index - 1, rows)
		drawLineBelow(row_index, char_index + 1, rows)
		
	
	if char_to_update == ".":
		updated_row = draw(rows[row_index + 1], char_index, "|")
		rows[row_index + 1] = updated_row
	
	
	return rows

def drawTachyonBeams(data):
	result = []
	rows = data.split("\n")
	
	
	for row_index in range(0, len(rows)):
		row = rows[row_index]
		charArray = []
		
		for char_index in range(0, len(row)):
			char = row[char_index]
			# check row below isnt a splitter
			
			if char == "S":
				drawLineBelow(row_index, char_index, rows)
			
			if char == "|":
				drawLineBelow(row_index, char_index, rows)
				
			
			charArray.append(char)
		result.append(charArray)
	
	return result
	

def countPermutations(beams):
	
	# start from the top, and keep a hash map of the total splits, to reference the permutations
	mapper = []
	mapper.append([]) # blank first index	
	
	# Create my hash map
	for row_index in range(1, len(beams)):
		row = beams[row_index]
		mapper.append([])
		
		for char_index in range(0, len(row)):
			mapper[row_index].append(0)
			
			
	for row_index in range(1, len(beams)):
		row = beams[row_index]
		for char_index in range(0, len(row)):
			
			# check row above contains a | too
			value = row[char_index]
			
			if char_index == 0:
				left_value = 0
			else:
				left_value = row[char_index - 1]
				
			if char_index == len(row) - 1:
				right_value = 0
			else:
				right_value = row[char_index + 1]

			above_value = beams[row_index - 1][char_index]
			
			
			if left_value == "|" and right_value == "|" and above_value == "|" and value == "^":
				# Spliiter found, grab the count above. and add 1 to left and right
				
				value_from_mapper_above = mapper[row_index - 1][char_index]
				
				# set left
				left_value_from_mapper = mapper[row_index][char_index - 1]
				mapper[row_index][char_index - 1] = left_value_from_mapper + value_from_mapper_above
				
				# set right
				right_value_from_mapper = mapper[row_index][char_index + 1]
				mapper[row_index][char_index + 1] = right_value_from_mapper + value_from_mapper_above

				
			else:
				if value == "|" :
					# take aboves value
					
					if row_index == 1:
						# First row. set to 1
						mapper[row_index][char_index] = 1
					else:
						# Add current value, to one from above
						mapper[row_index][char_index] = ( mapper[row_index - 1][char_index] + mapper[row_index][char_index] ) 
						
			
	# Print mapped variations for debugging
	#	for row in mapper:
	#	print(row)
		
			
	# Count the total values in the last row of our mapper
	count_permutations = 0
	for index in range(0, len(mapper[len(mapper) - 1])):
		count_permutations = count_permutations + mapper[len(mapper) - 1][index]
		
	return count_permutations
	
def solve(data):
	beams = drawTachyonBeams(data)
	result = countPermutations(beams) 
	return result


# Test functions
def convertToArray(data):
	result = []
	for row in data:
		row_array = []
		for string in row:
			row_array.append(string)
			
		result.append(row_array)
	return result

def convertToString(data):
	results = ""
	
	for row_index in range(0, len(data)):
		if row_index > 0:
			results += "\n"
			
		results += data[row_index]
	
	return results

def run_tests():
	
	# Tests to return ID ranges and Ingredient ranges
	assertion_test(drawTachyonBeams("..."), [[".",".","."]])
	assertion_test(drawTachyonBeams(".S."), [[".","S","."]])
	assertion_test(drawTachyonBeams(".S.\n..."), [[".","S","."],[".","|","."]])
	assertion_test(drawTachyonBeams(".S.\n.^."), [[".","S","."],["|","^","|"]])
	
	# Test Fake Splitters
	assertion_test(drawTachyonBeams("..S..\n^.^.^"), [[".",".","S",".","."],["^", "|","^","|", "^"]])
	assertion_test(drawTachyonBeams("...S...\n.^.^.^."), [[".",".",".","S",".",".","."],[".", "^", "|","^","|", "^", "."]])
	
	# Test Example
	assertion_test(
		drawTachyonBeams(
			convertToString([
				".......S.......",
				"...............",
				".......^.......",
				"...............",
				"......^.^......",
			])
		),
		convertToArray([
			".......S.......",
			".......|.......",
			"......|^|......",
			"......|.|......",
			".....|^|^|.....",
		])
	)
	
	assertion_test(
		drawTachyonBeams(
			convertToString([
				".......S.......",
				"...............",
				".......^.......",
				"...............",
				"......^.^......",
				"...............",
				".....^.^.^.....",
				"...............",
				"....^.^...^....",
				"...............",
				"...^.^...^.^...",
				"...............",
				"..^...^.....^..",
				"...............",
				".^.^.^.^.^...^.",
				"..............."
			])
		),
		convertToArray([
			".......S.......",
			".......|.......",
			"......|^|......",
			"......|.|......",
			".....|^|^|.....",
			".....|.|.|.....",
			"....|^|^|^|....",
			"....|.|.|.|....",
			"...|^|^|||^|...",
			"...|.|.|||.|...",
			"..|^|^|||^|^|..",
			"..|.|.|||.|.|..",
			".|^|||^||.||^|.",
			".|.|||.||.||.|.",
			"|^|^|^|^|^|||^|",
			"|.|.|.|.|.|||.|",
		])
	)
	
	
	assertion_test(solve(
		convertToString([
			"..S..",
			"..|..",
		])
	), 1)

	assertion_test(solve(
		convertToString([
			"..S..",
			"..|..",
			".|^|.",
		])
	), 2)

	
	assertion_test(solve(
		convertToString([
			"...S...",
			"...|...",
			"..|^|..",
			"..|.|..",
		])
	), 2)

	
	assertion_test(solve(
		convertToString([
			"...S...",
			"...|...",
			"..|^|..",
			"..|.|..",
			".|^|^|.",
		])
	), 4)


	assertion_test(solve(
		convertToString([
			".......S.......",
			".......|.......",
			"......|^|......",
			"......|.|......",
			".....|^|^|.....",
			".....|.|.|.....",
		])
	), 4)
	
	assertion_test(solve(
		convertToString([
			".......S.......",
			".......|.......",
			"......|^|......",
			"......|.|......",
			".....|^|^|.....",
			".....|.|.|.....",
			"....|^|^|^|....",
		])
	), 8)


	
	assertion_test(solve(
		convertToString([
		".......S.......",
		".......|.......",
		"......|^|......",
		"......|.|......",
		".....|^|^|.....",
		".....|.|.|.....",
		"....|^|^|^|....",
		"....|.|.|.|....",
		"...|^|^|||^|...",
		"...|.|.|||.|...",
		"..|^|^|||^|^|..",
		"..|.|.|||.|.|..",
		".|^|||^||.||^|.",
		".|.|||.||.||.|.",
		"|^|^|^|^|^|||^|",
		"|.|.|.|.|.|||.|",
		])
	), 40)

	


	
	
	# Test solve permutations
	assertion_test(solve("..."), 0)
	assertion_test(solve(".S.\n..."), 1)
	assertion_test(solve(".S.\n...\n.^."), 2)
	assertion_test(
		solve(
			convertToString([
				".......S.......",
				"...............",
				".......^.......",
				"...............",
				"......^.^......",
			])
		),
		4
	)
	
	assertion_test(
		solve(
			convertToString([
				".......S.......",
				"...............",
				".......^.......",
				"...............",
				"......^.^......",
				"...............",
				".....^.^.^.....",
				"...............",
				"....^.^...^....",
				"...............",
				"...^.^...^.^...",
				"...............",
				"..^...^.....^..",
				"...............",
				".^.^.^.^.^...^.",
				"..............."
			])
		),
		40
	)
	
		
	
def main():
	with open('input.txt') as file:
		data = file.read()
		result = solve(data)
		
		# Output value
		print(f"in total, the particle ends up on {result} different timelines.")
	
if __name__ == "__main__":
	main()
#	run_tests()