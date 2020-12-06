# --- Day 2: Password Philosophy ---
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we
# can't log in!" You ask if you can take a look. Their password database seems to be a little corrupted: some of the
# passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were
# chosen. To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the
# corrupted database) and the corporate policy when that password was set.
#
# For example, suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc

# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must
# contain a at least 1 time and at most 3 times. In the above example, 2 passwords are valid. The middle password,
# cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they
# contain one a or nine c, both within the limits of their respective policies.
# How many passwords are valid according to their policies?

from aocd import data
password_policy = data.split("\n")
# print(password_policy)

valid_password_count = 0
for password in range(0, len(password_policy)):
    password_policy[password] = password_policy[password].split(": ")

# print(password_policy)

for password in password_policy:
    rule = password[0]
    password = password[1]

    # separate numbers and letter
    rule = rule.split()
    # seperate min and max

    print(rule)
    letter = rule[1]
    min_and_max = rule[0].split('-')
    min_num = int(min_and_max[0])
    max_num = int(min_and_max[1])
    print(min_num, max_num)

    # check for letter in word
    count = 0
    for char in password:

        if char == letter:
            count += 1
    if count >= min_num and count <= max_num:
        valid_password_count += 1
print(valid_password_count)

#
# --- Part Two ---
#
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate
# Authentication System is expecting.
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the
# sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second
# character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these
# positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy
# enforcement. Given the same example list from above:
#     1-3 a: abcde is valid: position 1 contains a and position 3 does not.
#     1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
#     2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?
count_two = 0
for password in password_policy:
    rule = password[0]
    password = password[1]

    # separate numbers and letter
    rule = rule.split()
    # seperate min and max

    print(rule)
    letter = rule[1]
    two_positions = rule[0].split('-')
    first_pos = int(two_positions[0]) - 1
    second_pos = int(two_positions[1]) - 1
    print(first_pos, second_pos)

    # check for letter in word


    if (password[first_pos] == letter and password[second_pos] != letter) or \
            (password[first_pos] != letter and password[second_pos] == letter):
        count_two += 1
print(count_two)