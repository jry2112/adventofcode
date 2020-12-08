# --- Day 4: Passport Processing ---
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While
# these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually
# valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport
# scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the same
# time.
#
# The automatic passport scanners are slow because they're having trouble detecting which passports have all required
# fields. The expected fields are as follows:
#
#     byr (Birth Year)
#     iyr (Issue Year)
#     eyr (Expiration Year)
#     hgt (Height)
#     hcl (Hair Color)
#     ecl (Eye Color)
#     pid (Passport ID)
#     cid (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value
# pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
#
# ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in
#
# The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt
# (the Height field).
#
# The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials,
# not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat
# this "passport" as valid.
#
# The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so
# this passport is invalid.
#
# According to the above rules, your improved system would report 2 valid passports.
#
# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file,
# how many passports are valid?

# My Solution
# passport_dict = dict()
# passport_list = []
import re

day4 =  open('/Users/jadab/PycharmProjects/adventofcode/day4')
data = day4.read()
# data_list = data.split("\n\n")
# print(data_list)
#
#
# requirement_list = ["iyr", 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid', 'byr'] # cid is optional
# check_list = []
#
#
# count = 0
# for data in data_list:
#    req_count = 0
#    for req in requirement_list:
#       if req in data:
#          req_count += 1
#    if req_count == 7 and "cid" not in data or req_count == 8:
#       check_list += data.split(" ")
#       count += 1
# print(count)
#
# print(check_list)

passports = data.split("\n\n")
for i in range(len(passports)):
    passports[i] = passports[i].replace("\n", " ").split(' ')

passportdic = {}
passportdictinlist = []

for x in range(len(passports)):
    for i in range(len(passports[x])-1):
        passportdic[passports[x][i].split(':')[0]] = passports[x][i].split(':')[1]
    passportdictinlist.append(passportdic.copy())
    passportdic = {}
#
# print(passportdictinlist)
# count = 0
# checked = 0
# print("checking", len(passportdictinlist), "passports")
# for passport in passportdictinlist:
#    print("checking", passport)
#    if (len(passport) == 7 and "cid" not in passport.keys()) or len(passport) == 8:
#       print("length is ok")
#       checked += 1
#       print(checked)
#       if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
#          print("byr is ok")
#          if int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
#             print("iyr is ok")
#             if int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
#                print("eyr is ok")
#                if ("cm" in passport['hgt'] and int(passport['hgt'][:-2]) >= 150 and int(passport['hgt'][:-2]) <= 193) or \
#                   ("in" in passport['hgt'] and int(passport['hgt'][:-2]) >= 59 and int(passport['hgt'][:-2]) <= 76):
#                   print("height is ok")
#                   if passport['hcl'][0] == '#' and len(passport['hcl']) == 7:
#                      allowed_letters = ['a', 'b', 'c', 'd', 'e', 'f']
#                      valid_alphanum = True
#                      for char in passport['hcl'][1:]:
#                         if char.isdigit() == True or char in allowed_letters:
#                            print(char)
#                         else:
#                            print("check here again")
#                            valid_alphanum = False
#                      if valid_alphanum:
#                         print("PID was valid")
#                         eye_color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
#                         if passport['ecl'] in eye_color_list:
#                            print('ecl ok')
#                            if len(passport['pid']) == 9 and passport['pid'].isdigit():
#                               print('pid ok')
#
#
#
#                               count += 1
# print(count)
# --- Part Two ---
#
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data
# are getting through. Better add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
# automatic validation:
#
#     byr (Birth Year) - four digits; at least 1920 and at most 2002.
#     iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#     eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#     hgt (Height) - a number followed by either cm or in:
#         If cm, the number must be at least 150 and at most 193.
#         If in, the number must be at least 59 and at most 76.
#     hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#     ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#     pid (Passport ID) - a nine-digit number, including leading zeroes.
#     cid (Country ID) - ignored, missing or not.
#
# Your job is to count the passports where all required fields are both present and valid according to the above rules.
# Here are some example values:
#
# byr valid:   2002
# byr invalid: 2003
#
# hgt valid:   60in
# hgt valid:   190cm
# hgt invalid: 190in
# hgt invalid: 190
#
# hcl valid:   #123abc
# hcl invalid: #123abz
# hcl invalid: 123abc
#
# ecl valid:   brn
# ecl invalid: wat
#
# pid valid:   000000001
# pid invalid: 0123456789
#
# Here are some invalid passports:
#
# eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
#
# Here are some valid passports:
#
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
#
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as
# optional. In your batch file, how many passports are valid?
#import re

f = open('/Users/jadab/PycharmProjects/adventofcode/day4', "r")
raw = str(f.read())
split1 = raw.split("\n\n")
raw_file = []

for num in split1:
	num1 = num.replace("\n", " ")
	raw_file.append(num1.split())

# Part 1
count_valid_1 = 0
new_file = []

for num in raw_file:
	num1 = sorted(num)
	if len(num) == 8:
		count_valid_1 += 1
		num1.pop(1)
		new_file.append(num1)
	elif len(num) == 7:
		is_cid = 0
		for i in num:
			if i[:3] == "cid":
				is_cid += 1
		if is_cid == 0:
			count_valid_1 +=1
			new_file.append(num1)

# Part 2
count_valid_2 = 0
for num in new_file:
	check = 0
	# Check BYR
	byr = str(num[0]).split(":")[1]
	if int(byr) >= 1920 and int(byr) <= 2002:
		check += 1
	# Check ECL
	ecl = str(num[1]).split(":")[1]
	if ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth':
		check += 1
	# Check EYR
	eyr = str(num[2]).split(":")[1]
	if int(eyr) >= 2020 and int(eyr) <= 2030:
		check += 1
	# Check HCL
	hcl = str(num[3]).split(":")[1]
	pattern = re.compile("[a-f0-9]+")
	if len(hcl) == 7 and hcl[0] == "#" and pattern.fullmatch(hcl[1:]) is not None:
		check += 1
	# Check HGT
	hgt = str(num[4]).split(":")[1]
	if hgt[-2:] == "cm" and (int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193):
		check += 1
	elif hgt[-2:] == "in" and (int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76):
		check += 1
	# Check IYR
	iyr = str(num[5]).split(":")[1]
	if int(iyr) >= 2010 and int(iyr) <= 2020:
		check += 1
	# Check PID
	pid = str(num[6]).split(":")[1]
	pattern = re.compile("[0-9]+")
	if len(pid) == 9 and pattern.fullmatch(pid) is not None:
		check += 1
	#Check if valid
	if check == 7:
		count_valid_2 += 1

print(count_valid_1)
print(count_valid_2)