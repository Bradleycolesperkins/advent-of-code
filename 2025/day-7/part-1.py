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
	
	
def countBeamsSplit(beams):
	count = 0
	for row_index in range(1, len(beams)):
		row = beams[row_index]
		for char_index in range(1, len(row) - 1):
			# check row above contains a | too
			value = row[char_index]
			left_value = row[char_index - 1]
			right_value = row[char_index + 1]
			above_value = beams[row_index - 1][char_index]
			
			if left_value == "|" and right_value == "|" and above_value == "|" and value == "^":
				count += 1
				
				
	return count
	
def solve(data):
	result = 0
	beams = drawTachyonBeams(data)
	result = countBeamsSplit(beams) 
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
	
	
	
	
	# Test solve
	assertion_test(solve("..."), 0)
	assertion_test(solve(".S."), 0)
	assertion_test(solve(".S.\n..."), 0)
	assertion_test(solve(".S.\n.^."), 0)
	assertion_test(solve(".S.\n...\n.^."), 1)
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
		3
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
		21
	)
	
	
	
	
		
	
def main():
	with open('input.txt') as file:
		data = file.read()
		result = solve(data)
		
		# Output value
		print(f"a tachyon beam is split a total of {result} times.")
	
if __name__ == "__main__":
	main()
#	run_tests()