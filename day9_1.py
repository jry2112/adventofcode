# --- Day 9: Encoding Error ---
#
# With your neighbor happily enjoying their video game, you turn your attention to an open data port on the little
# screen in the seat in front of you.
#
# Though the port is non-standard, you manage to connect it to your computer through the clever use of several
# paperclips. Upon connection, the port outputs a series of numbers (your puzzle input).
#
# The data appears to be encrypted with the eXchange-Masking Addition System (XMAS) which, conveniently for you,
# is an old cypher with an important weakness.
#
# XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be the sum of any two
# of the 25 immediately previous numbers. The two numbers will have different values, and there might be more than
# one such pair.
#
# For example, suppose your preamble consists of the numbers 1 through 25 in a random order. To be valid, the next
# number must be the sum of two of those numbers:
#
#     26 would be a valid next number, as it could be 1 plus 25 (or many other pairs, like 2 and 24).
#     49 would be a valid next number, as it is the sum of 24 and 25.
#     100 would not be valid; no two of the previous 25 numbers sum to 100.
#     50 would also not be valid; although 25 appears in the previous 25 numbers, the two numbers in the pair must
#     be different.
#
# Suppose the 26th number is 45, and the first number (no longer an option, as it is more than 25 numbers ago) was 20.
# Now, for the next number to be valid, there needs to be some pair of numbers among 1-19, 21-25, or 45 that add up to
# it:
#
#     26 would still be a valid next number, as 1 and 25 are still within the previous 25 numbers.
#     65 would not be valid, as no two of the available numbers sum to it.
#     64 and 66 would both be valid, as they are the result of 19+45 and 21+45 respectively.
#
# Here is a larger example which only considers the previous 5 numbers (and has a preamble of length 5):
#
# 35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
#
# In this example, after the 5-number preamble, almost every number is the sum of two of the previous 5 numbers;
# the only number that does not follow this rule is 127.
#
# The first step of attacking the weakness in the XMAS data is to find the first number in the list (after the preamble)
# which is not the sum of two of the 25 numbers before it. What is the first number that does not have this property?

def get_preamble(preamble_length,input):
    # returns preamble of list
    preamble_list = []
    for x in range(0, preamble_length):
        preamble_list.append(input[x])
    return preamble_list

def get_set(input, start, stop):
    current_set = []
    for x in range(start, stop):
        current_set.append(input[x])
    return current_set

def update_set(input, start, stop):
    next_set = []
    for x in range(start, stop):
        next_set.append(input[x])
    return next_set

def possible_sums(current_set):
    possible_sums_set = set()
    for i in range(0, len(current_set)-1):
        for j in range(i+1, len(current_set)):
            possible_sums_set.add(current_set[i] + current_set[j])
            # print(current_set[i], current_set[j], current_set[i] + current_set[j])

    return possible_sums_set

def check_sums(possible_sums, next_num):
    number = next_num
    sums = possible_sums
    if number in sums:
        return True
    else:
        return False

# Test
test_list = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
test_preamble_length = 5

start = 0
stop = 5
next_num = test_list[stop + 1]
preamble = get_preamble(test_preamble_length, test_list)
current_set = get_set(test_list, start, stop)
next_set = update_set(test_list, start + 1, stop + 1)
possible_sums_set = possible_sums(current_set)
check_flag = False
while check_flag == False:
    if check_sums(possible_sums_set, next_num) == False:
        print(f"next num is invalid: {next_num}")
        check_flag = True
    else:
        start += 1
        stop += 1
        next_num = test_list[stop + 1]
        current_set = next_set
        next_set = update_set(test_list, start + 1, stop + 1)
        possible_sums_set = possible_sums(current_set)
        print(f"checking {current_set}")
#print(f"preamble: {preamble} '\n' current set: {current_set} \n next set: {next_set}")
#print(f" possible sums: {possible_sums}")

# Actual
numbers_list = []
raw = open('/Users/jadab/PycharmProjects/adventofcode/day9', "r")
line = raw.readline()
for line in raw:
    number = int(line)
    numbers_list.append(number)


preamble_length = 25

start = 0
stop = 25
next_num = numbers_list[stop + 1]
preamble = get_preamble(preamble_length, numbers_list)
current_set = get_set(numbers_list, start, stop)
next_set = update_set(numbers_list, start + 1, stop + 1)
possible_sums_set = possible_sums(current_set)
check_flag = False
print(current_set)
while check_flag == False:
    if check_sums(possible_sums_set, next_num) == False:
        print(f"next num is invalid: {next_num}\n {current_set}")
        check_flag = True
    else:
        start += 1
        stop += 1
        next_num = numbers_list[stop + 1]
        current_set = update_set(numbers_list, start + 1, stop + 1)

        possible_sums_set = possible_sums(current_set)
        print(f"checking {current_set}, next num: {next_num}")

#Part 2: What 2+ contiguous numbers in the list sum to the broken number?
target = next_num
sum_list = []
sum = 0
start = 0

while sum < target:
