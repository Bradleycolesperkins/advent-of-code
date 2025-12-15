#!/usr/bin/env python3
def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# ------------------------------------
	
	
def getIngredientIdRangesAndFreshIngredients(input):
	# Split on empty line
	split = input.split("\n\n")
	ranges = split[0].split("\n") 
	
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
	
def run_tests():
	
	# Tests to return ID ranges and Ingredient ranges
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n\n1"),([[1,2]], [1]))
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n\n1\n2\n3"),([[1,2]], [1, 2, 3]))
	assertion_test(getIngredientIdRangesAndFreshIngredients("1-2\n3-4\n\n1"),([[1,2], [3,4]], [1]))
	
	# Check min and max wrong way round
	assertion_test(getIngredientIdRangesAndFreshIngredients("2-1\n4-3\n\n1"),([[1,2], [3,4]], [1]))
	
	# Test is fresh
	assertion_test(isFresh([[1,3]], 3),True)
	assertion_test(isFresh([[1,3]], 8),False)
	assertion_test(isFresh([[1,3], [7,8]], 8),True)
	assertion_test(isFresh([[1,3], [7,8], [97,98]], 99),False)


	# Test fresh counts
	assertion_test(countFreshIngredients([[]], []), 0)
	assertion_test(countFreshIngredients([[1,3]], []), 0)
	assertion_test(countFreshIngredients([[1,3]], [2]), 1)
	assertion_test(countFreshIngredients([[1,3]], [1, 2, 3]), 3)
	assertion_test(countFreshIngredients([[1,3], [4,5], [5,6]], [1, 2, 3, 4, 5, 6]), 6)
	assertion_test(countFreshIngredients([[1,3], [4,5], [1,6]], [1, 2, 3, 4, 5, 6]), 6)
	assertion_test(countFreshIngredients([[1,3], [4,5], [1,6]], [1, 2, 3, 4, 5, 6, 7, 9, 10]), 6)
	

def main():
	with open('input.txt') as file:

		data = file.read()
		ranges, ids = getIngredientIdRangesAndFreshIngredients(data)
		result = countFreshIngredients(ranges, ids)
		
		# Output value
		print(f"{result} of the available ingredient IDs are fresh")
	
if __name__ == "__main__":
	main()
	run_tests()