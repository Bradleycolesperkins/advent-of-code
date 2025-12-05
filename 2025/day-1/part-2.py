#!/usr/bin/env python3
import math

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

def rotate_dial(command, dial_position, zero_count):
	# Get rotation
	running_dial_position = rotate(command, dial_position)
	
	print(f"The dial is rotated {command} to point at {running_dial_position}. Zero Count = {zero_count}")
	
	# check if we passed zero, ie from 90 to 10
	direction = command[0]
	rotation_amount = int(command[1:])
	
	# did we land on zero? But only if we didnt start on a zero, because our full rotation catches this
	if ( rotation_amount % 100 ) != 0:
		zero_count = is_zero(running_dial_position, zero_count)
	
	# How many full rotations do we have? ie 551 rotations, = 5 full rotations. Take 51 off and divide by 100.
	full_rotations = math.floor( ( rotation_amount - ( rotation_amount % 100 ) ) / 100)
	
	# Add full rotations to zero
	zero_count += full_rotations
	
	# now count if the 51 takes us passed zero for a final check
	remainder_rotations = ( rotation_amount % 100 )
	
	if direction.lower() == "r":
		amount_till_zero = 100 - dial_position
	else:
		amount_till_zero = dial_position
		
	# if the attempted rotation was 551, we've calculated full rotations, now check if the 51 is greater than the amount till zero
	# ie. if the dial is on 90. we've done 5 full rotations, (551 % 100) = 51, we check if 51 is greater than the distance from 90 to 100.
	# If it is we increment count
	if remainder_rotations > amount_till_zero and amount_till_zero != 0:
		zero_count += 1
		
	return running_dial_position, zero_count


with open('input.txt') as file:
	running_dial_position = 50
	zero_count = 0
	
	print(f"The dial starts by pointing at {running_dial_position}.")
	
	for line in file:
		command = line.strip()		
		running_dial_position, zero_count = rotate_dial(command, running_dial_position, zero_count)
		
	# Output value
	print("\n\n--------------\n\n")
	print(f"The dial is position ended at: {running_dial_position}.")
	print(f"Time the dial landed on zeros: {zero_count}.")
	print("\n\n--------------")

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


# Test rotate dial function
assertion_test(rotate_dial('R0', 50, 0), (50, 0)) # Should be no movement and no increment
assertion_test(rotate_dial('R1', 50, 0), (51, 0)) # Should be 1 movement and no increment
assertion_test(rotate_dial('L1', 50, 0), (49, 0)) # Should be 1 movement and no increment

# Test Increment within function
assertion_test(rotate_dial('R50', 50, 0), (0, 1)) # Should be 1 movement and no increment
assertion_test(rotate_dial('L50', 50, 0), (0, 1)) # Should be 1 movement and no increment

# Test passing zero should increment 
assertion_test(rotate_dial('R20', 90, 0), (10, 1)) # Should be 1 movement and no increment
assertion_test(rotate_dial('L20', 10, 0), (90, 1)) # Should be 1 movement and no increment

# Test passing zero in large amounts
assertion_test(rotate_dial('R100', 50, 0), (50, 1)) 
assertion_test(rotate_dial('R1000', 50, 0), (50, 10)) 
assertion_test(rotate_dial('R10000', 50, 0), (50, 100)) 
assertion_test(rotate_dial('L100', 50, 0), (50, 1)) 
assertion_test(rotate_dial('L1000', 50, 0), (50, 10)) 
assertion_test(rotate_dial('L10000', 50, 0), (50, 100)) 

# Test Landing on zero also increments
assertion_test(rotate_dial('R49', 50, 0), (99, 0)) 
assertion_test(rotate_dial('R50', 50, 0), (0, 1)) 
assertion_test(rotate_dial('R51', 50, 0), (1, 1)) 
assertion_test(rotate_dial('R51', 50, 0), (1, 1)) 
assertion_test(rotate_dial('R151', 50, 0), (1, 2))
assertion_test(rotate_dial('R1051', 50, 0), (1, 11))
assertion_test(rotate_dial('R10051', 50, 0), (1, 101))
assertion_test(rotate_dial('R100051', 50, 0), (1, 1001))

assertion_test(rotate_dial('L49', 50, 0), (1, 0)) 
assertion_test(rotate_dial('L50', 50, 0), (0, 1)) 
assertion_test(rotate_dial('L51', 50, 0), (99, 1)) 
assertion_test(rotate_dial('L51', 50, 0), (99, 1)) 
assertion_test(rotate_dial('L151', 50, 0), (99, 2))
assertion_test(rotate_dial('L1051', 50, 0), (99, 11))
assertion_test(rotate_dial('L10051', 50, 0), (99, 101))
assertion_test(rotate_dial('L100051', 50, 0), (99, 1001))


# Test being on zero and moving
assertion_test(rotate_dial('R5', 0, 0), (5, 0))
assertion_test(rotate_dial('R50', 0, 0), (50, 0))
assertion_test(rotate_dial('R100', 0, 0), (0, 1))
assertion_test(rotate_dial('R101', 0, 0), (1, 1))

assertion_test(rotate_dial('L5', 0, 0), (95, 0))
assertion_test(rotate_dial('L50', 0, 0), (50, 0))
assertion_test(rotate_dial('L100', 0, 0), (0, 1))
assertion_test(rotate_dial('L101', 0, 0), (99, 1))


# Run through example
start = 50
zero_count = 0

start, zero_count = rotate_dial('L68', start, zero_count)
assertion_test(start, 82) 
assertion_test(zero_count, 1)


start, zero_count = rotate_dial('L30', start, zero_count)
assertion_test(start, 52) 
assertion_test(zero_count, 1)

start, zero_count = rotate_dial('R48', start, zero_count)
assertion_test(start, 0) 
assertion_test(zero_count, 2)


start, zero_count = rotate_dial('L5', start, zero_count)
assertion_test(start, 95) 
assertion_test(zero_count, 2)

start, zero_count = rotate_dial('R60', start, zero_count)
assertion_test(start, 55) 
assertion_test(zero_count, 3)

start, zero_count = rotate_dial('L55', start, zero_count)
assertion_test(start, 0) 
assertion_test(zero_count, 4)

start, zero_count = rotate_dial('L1', start, zero_count)
assertion_test(start, 99) 
assertion_test(zero_count, 4)

start, zero_count = rotate_dial('L99', start, zero_count)
assertion_test(start, 0) 
assertion_test(zero_count, 5)

start, zero_count = rotate_dial('R14', start, zero_count)
assertion_test(start, 14) 
assertion_test(zero_count, 5)

start, zero_count = rotate_dial('L82', start, zero_count)
assertion_test(start, 32) 
assertion_test(zero_count, 6)
