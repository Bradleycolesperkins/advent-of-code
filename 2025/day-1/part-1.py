#!/usr/bin/env python3

def rotate(command, dial_position):
	
	# Get first char as the direction
	direction = command[0]
	
	# Get rotation amount by removing first char from command
	rotation_amount = int(command[1:])
	
	# Larger than 100 rotations we can simplify, and just get the remainder divisible by 100
	if rotation_amount > 100:
		rotation_amount = rotation_amount % 100
	
	
	# add rotation amount to current dial position
	if direction.lower() == "r":
		dial_position += rotation_amount
	else: 
		dial_position -= rotation_amount
		
	# dial positionn only goes to 99 then starts back at 0
	if dial_position > 99:
		dial_position = dial_position - 100
		
	if dial_position < 0:
		dial_position = dial_position + 100
	
	# return updated dial
	return dial_position


def is_zero(dial_position, counter):
	if dial_position == 0:
		counter += 1
	
	return counter


with open('input.txt') as file:
	running_dial_position = 50
	zero_count = 0
	
	print(f"The dial starts by pointing at {running_dial_position}.")
	
	for line in file:
		command = line.strip()
		running_dial_position = rotate(command, running_dial_position)
		print(f"The dial is rotated {command} to point at {running_dial_position}.")
	
		zero_count = is_zero(running_dial_position, zero_count)
		
	# Output value
	print("\n\n--------------")
	print(f"The dial is position ended at: {running_dial_position}.")
	print(f"Time the dial landed on zeros: {zero_count}.")


########################################################################

# Test Cases:

def assertion_test(a, b):
	assert a == b, f"Test failed {a} != {b}"

# Base tests
assertion_test(rotate('R0', 0), 0)
assertion_test(rotate('R0', 50), 50)
assertion_test(rotate('L0', 50), 50)

# test left and right increments
assertion_test(rotate('R1', 50), 51)
assertion_test(rotate('L1', 50), 49)

# Test full rotations
assertion_test(rotate('R100', 50), 50)
assertion_test(rotate('L100', 50), 50)

# Test land on zeros
assertion_test(rotate('R50', 50), 0)
assertion_test(rotate('L50', 50), 0)

# Test large rotations
assertion_test(rotate('R1000', 50), 50)
assertion_test(rotate('L1000', 50), 50)

# Test large rotation landing on zero
assertion_test(rotate('R1050', 50), 0)
assertion_test(rotate('R1050', 50), 0)

# Test keeping track
test_val = 50
test_val = rotate('R10', test_val) # should be 60
test_val = rotate('R10', test_val) # should be 70
test_val = rotate('L5', test_val) # should be 65
test_val = rotate('L5', test_val) # should be 60
assertion_test(test_val, 60)

# Test zero incrementer
assertion_test(is_zero(50, 0), 0)
assertion_test(is_zero(0, 0), 1)
assertion_test(is_zero(0, 1), 2)


