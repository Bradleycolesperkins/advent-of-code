#!/usr/bin/env python3
def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# ------------------------------------

def insertNewRange(ingredient_ranges, range_to_insert):
	if len(range_to_insert) == 0:
		return ingredient_ranges
	
	position = len(ingredient_ranges)
	
	if len(ingredient_ranges) == 0:
		ingredient_ranges.insert(0, range_to_insert)
		return ingredient_ranges
	
	
	# Sort by lowest
	val_1 = range_to_insert[0]
	val_2 = range_to_insert[1]	
	range_to_insert_start = val_2 if (val_1 > val_2) else val_1

	
	# Loop though and get the initial starting value position
	for cursor in range(0, len(ingredient_ranges)): 
		current_range_to_check = ingredient_ranges[cursor]
		current_start = current_range_to_check[0]
		
		# Sort by start only
		if range_to_insert_start < current_start:
			position = cursor
			break
		
	if position != None:
		ingredient_ranges.insert(position, range_to_insert)
			
	return ingredient_ranges
	
	
def mergeNewRange(ingredient_ranges):
	new_range = []
	index_cursor = 0
	
	for index in range(0, len(ingredient_ranges)):
		if index == index_cursor:
			
			range_start = ingredient_ranges[index][0]
			range_end = ingredient_ranges[index][1]
			
			# The last itteration, we can append this
			if index == len(ingredient_ranges) - 1:
				new_range.append([range_start, range_end])
				index_cursor += 1
				continue
			
			next_range_start = ingredient_ranges[index + 1][0]
			next_range_end = ingredient_ranges[index + 1][1]
			
			
			# A basic start is less than the next end, and the current end is less than the next start. just append
			if range_start < next_range_start and range_end < next_range_start:		
				new_range.append([range_start, range_end])
				index_cursor += 1
				continue
			
			tmp_start = range_start
			tmp_end = range_end
			for index_2 in range(index + 1, len(ingredient_ranges)):
				# loop though until the end is less than the new start
				
				find_next_itteration = ingredient_ranges[index_2]
				find_next_start = find_next_itteration[0]
				find_next_end = find_next_itteration[1]

				# Check if we have a running tmp end that is within the next itteration. if so this becomes the new end
				if tmp_end <= find_next_end and tmp_end >= find_next_start:					
					tmp_end = find_next_end
					index_cursor = index_2
					
					
				# Check if the start and end dates of the next are within our current range. We can just skip this one if so
				if find_next_itteration[0] >= tmp_start and find_next_itteration[1] <= tmp_end:
					index_cursor = index_2
					
			new_range.append([tmp_start, tmp_end])
			index_cursor += 1
		
	return new_range
	
def getIngredientIdRangesAndFreshIngredients(input):
	# Split on empty line
	split = input.split("\n\n")
	ranges = split[0].split("\n") 
	sorted_ranges = []
	
	# Convert to ints with start and end range
	for index, range in enumerate(ranges):
		range_split = range.split("-")
		val_1 = int(range_split[0])
		val_2 = int(range_split[1])
		
		
		min_val = val_2 if (val_1 > val_2) else val_1
		max_val = val_2 if (val_1 < val_2) else val_1
		
		ranges[index] = [min_val, max_val]
				
		
	
	ingredients = split[1].split("\n") 
	
	# Convert to ints
	for index, ingredient in enumerate(ingredients):
		ingredients[index] = int(ingredient)
	
	# Could potentially sort the starting ints for efficiency
	
	return ranges, ingredients

def isFresh(ingredientIDs, id):
	# Check if our Id is inbetween any of the ingredient Ids
	
	for range in ingredientIDs:
		if id >= range[0] and id <= range[1]:
			return True
		
	return False


def countFreshIngredients(ingredientIDs, ids):
	result = 0
	
	for id in ids:
		is_fresh = isFresh(ingredientIDs, id)
		if is_fresh:
			result += 1
	
	return result

def solvePuzzle(data):
	ranges, ids = getIngredientIdRangesAndFreshIngredients(data)

	running_range = []
	for range_to_insert in ranges:
		running_range = insertNewRange(running_range, range_to_insert)

	merged_ranges = mergeNewRange(running_range)

	result = 0

	for merged_range in merged_ranges:
		ans = (merged_range[1] - merged_range[0]) + 1
		result += ans
		
	return result

	
def run_tests():
	# Tests to return ID ranges and Ingredient ranges
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n\n1"),([[1,2]], [1]))
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n\n1\n2\n3"),([[1,2]], [1, 2, 3]))
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n3-4\n\n1"),([[1,2], [3,4]], [1]))
	
	# Test inserting a new range, with the sorted method
	assertion_test(insertNewRange([], []), []) # Base case
	assertion_test(insertNewRange([], [1,2]), [[1,2]]) # Simple insert
	assertion_test(insertNewRange([[1,2]], [3,4]), [[1,2],[3,4]]) # Add to end
	assertion_test(insertNewRange([[3,4]], [1,2]), [[1,2],[3,4]]) # Add to start 
	assertion_test(insertNewRange([[1,2], [5,6]], [3,4]), [[1,2],[3,4],[5,6]]) # Add to middle
	assertion_test(insertNewRange([[3,4], [5,6]], [1,2]), [[1,2],[3,4],[5,6]]) # Add to start
	assertion_test(insertNewRange([[1,2], [3,4]], [5,6]), [[1,2],[3,4],[5,6]]) # Add to end
	assertion_test(insertNewRange([[1,2], [3,4], [7,8], [9,10]], [5,6]), [[1,2],[3,4],[5,6],[7,8],[9,10]]) # Add to middle 
	assertion_test(insertNewRange([[1,3], [3,45], [7,8], [9,1110]], [5,111]), [[1,3],[3,45],[5,111],[7,8],[9,1110]]) # Add to middle 
	
	# Test inserting a new range, with the merge method
	assertion_test(mergeNewRange([]), [])
	assertion_test(mergeNewRange([[1,2]]), [[1,2]])
	assertion_test(mergeNewRange([[1,2],[3,4]]), [[1,2],[3,4]])
	assertion_test(mergeNewRange([[1,2],[3,4],[5,6]]), [[1,2],[3,4],[5,6]])
	assertion_test(mergeNewRange([[1,3],[3,6]]), [[1,6]])
	assertion_test(mergeNewRange([[1,3],[3,4]]), [[1,4]])
	assertion_test(mergeNewRange([[1,2],[2,3]]), [[1,3]])
	assertion_test(mergeNewRange([[1,2],[2,3],[3,4]]), [[1,4]])
	assertion_test(mergeNewRange([[1,2],[2,3],[3,4],[4,5]]), [[1,5]])

	
	# Test example data
	assertion_test(insertNewRange([], [3,5]), [[3,5]])
	assertion_test(insertNewRange([[3,5]], [10,14]), [[3,5],[10,14]])
	assertion_test(insertNewRange([[3,5],[10,14]], [16,20]), [[3,5],[10,14],[16,20]])
	assertion_test(insertNewRange([[3,5],[10,14],[16,20]], [12, 18]), [[3,5],[10,14],[12,18],[16,20]])
	
	assertion_test(mergeNewRange([[3,5],[10,14],[12,18],[16,20]]), [[3,5],[10,20]])
	
	# Check min and max wrong way round
	assertion_test(getIngredientIdRangesAndFreshIngredients("2-1\n4-3\n\n1"),([[1,2], [3,4]], [1]))
	
	
	assertion_test(insertNewRange([], [1,3]), [[1,3]])
	assertion_test(insertNewRange([[1,3]], [2,10]), [[1,3],[2,10]])
	assertion_test(insertNewRange([[1,3],[2,10]], [15,20]), [[1,3],[2,10],[15,20]])
	assertion_test(mergeNewRange([[1,3],[2,10],[15,20]]), [[1,10],[15,20]])
	
	assertion_test(solvePuzzle("1-3\n2-10\n15-20\n\n1"), 16)

	assertion_test(mergeNewRange([[1,10], [3,5]]), [[1,10]])
	assertion_test(solvePuzzle("1-10\n3-5\n\n1"), 10)
	

def main():
	with open('input.txt') as file:
		data = file.read()
		result = solvePuzzle(data)
		print(f"{result} of the available ingredient IDs are fresh")
	
if __name__ == "__main__":
	main()
	run_tests()