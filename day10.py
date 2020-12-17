# --- Day 10: Adapter Array ---
# Patched into the aircraft's data port, you discover weather forecasts of a massive tropical storm. Before you can
# figure out whether it will impact your vacation plans, however, your device suddenly turns off!
#
# Its battery is dead.
#
# You'll need to plug it in. There's only one problem: the charging outlet near your seat produces the wrong number of
# jolts. Always prepared, you make a list of all of the joltage adapters in your bag.
#
# Each of your joltage adapters is rated for a specific output joltage (your puzzle input). Any given adapter can take
# an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
#
# In addition, your device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter
# in your bag. (If your adapter list were 3, 9, and 6, your device's built-in adapter would be rated for 12 jolts.)
#
# Treat the charging outlet near your seat as having an effective joltage rating of 0.
#
# Since you have some time to kill, you might as well test all of your adapters. Wouldn't want to get to your resort
# and realize you can't even charge your device!
#
# If you use every adapter in your bag at once, what is the distribution of joltage differences between the charging
# outlet, the adapters, and your device?
#
# For example, suppose that in your bag, you have adapters with the following joltage ratings:
#
# 16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4
# With these adapters, your device's built-in joltage adapter would be rated for 19 + 3 = 22 jolts,
# 3 higher than the highest-rated adapter.
#
# Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter,
# you'd need to choose them like this:
#
# The charging outlet has an effective rating of 0 jolts, so the only adapters that could connect to it directly would
# need to have a joltage rating of 1, 2, or 3 jolts. Of these, only one you have is an adapter rated 1 jolt (difference of 1).
# From your 1-jolt rated adapter, the only choice is your 4-jolt rated adapter (difference of 3).
# From the 4-jolt rated adapter, the adapters rated 5, 6, or 7 are valid choices. However, in order to not skip any
# adapters, you have to pick the adapter rated 5 jolts (difference of 1).
# Similarly, the next choices would need to be the adapter rated 6 and then the adapter rated 7
# (with difference of 1 and 1).
# The only adapter that works with the 7-jolt rated adapter is the one rated 10 jolts (difference of 3).
# From 10, the choices are 11 or 12; choose 11 (difference of 1) and then 12 (difference of 1).
# After 12, only valid adapter has a rating of 15 (difference of 3), then 16 (difference of 1),
# then 19 (difference of 3).
# Finally, your device's built-in adapter is always 3 higher than the highest adapter,
# so its rating is 22 jolts (always a difference of 3).
# In this example, when using every adapter, there are 7 differences of 1 jolt and 5 differences of 3 jolts.
#
# Here is a larger example:
#
# 28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# In this larger example, in a chain that uses all of the adapters, there are 22 differences of
# 1 jolt and 10 differences of 3 jolts.
#
# Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in adapter and count
# the joltage differences between the charging outlet, the adapters, and your device. What is the number of 1-jolt
# differences multiplied by the number of 3-jolt differences?

def parse(file):
    with open(file) as f:
        input_list = [line.rstrip('\n') for line in f]
        for num in range(0, len(input_list)):
            input_list[num] = int(input_list[num])
        input_list.sort()
    return input_list

def check_charge_outlet(adapter_list, charging_outlet=0, max_difference=3):
    if adapter_list[0] - charging_outlet <= max_difference:
        return True

def chain_adapters(adapter_list):
    adapter_list_copy = adapter_list.copy()
    charging_outlet = 0
    chain_order = [charging_outlet]
    differences = {0: 0,
                   1: 0,
                   2: 0,
                   3: 0}

    for index in range(0, len(adapter_list)):
        current_adapter = adapter_list[index]
        try:
            previous_adapter = adapter_list[index-1]
            if current_adapter - previous_adapter <= 3:
                chain_order.append(current_adapter)
                differences[current_adapter - previous_adapter] += 1
        except:
            if index == 0:
                chain_order.append(current_adapter)
                differences[current_adapter - charging_outlet] += 1
            pass

    return chain_order, differences


#test_list = parse('day10test.txt')
#print(test_list)
#print(chain_adapters(test_list))

actual_list = parse('day10.txt')
print(actual_list)
print()
chain_order, differences = chain_adapters(actual_list)
print(chain_order)
print(differences)
# connection to device's adapter
differences[3] += 1
print()
print("product of 1 and 3: ", differences[1] * differences[3])