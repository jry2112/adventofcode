import copy

def parse(file):
    with open(file) as f:
        input_list = [line.rstrip('\n') for line in f]
    clean_list = []
    for row in range(0, len(input_list)):
        row_of_seats = []
        for column in range(0, len(input_list[row])):
            char = input_list[row][column]
            row_of_seats.append(char)
            if len(row_of_seats) == len(input_list[row]):
                clean_list.append(row_of_seats)
    return clean_list



class SeatingSystem:

    def __init__(self, input):
        self.empty_seat = "L"
        self.occupied_seat = "#"
        self.floor = "."
        self.original_seat_list = parse(input)
        self.seat_list = copy.deepcopy(self.original_seat_list)
        self.row = 0
        self.column = 0



    def display_original_seat_layout(self):
        for row in range(0, len(self.original_seat_list)):
            print(self.original_seat_list[row])

    def display_clean_seat_layout(self):
        for row in range(0, len(self.seat_list)):
            print(self.seat_list[row])

    def get_current_seat_layout(self):
        return self.seat_list

    def update_seat(self, row, column):
        seat = self.seat_list[row][column]
        if seat == self.floor:
            seat = seat
        elif seat == self.occupied_seat:
            #check adjacent
            neighboring_seats = self.find_adjacent_seats(row, column)
            seat = self.occupied_seat_update(seat, neighboring_seats)

        elif seat == self.empty_seat:
            neighboring_seats = self.find_adjacent_seats(row, column)
            seat = self.empty_seat_update(seat, neighboring_seats)
        return seat

    def find_adjacent_seats(self, row, column):
        adjacent_list = []
        for row_index in range(row-1, row + 2):
            for column_index in range(column-1, column+2):
                if row_index >= 0 and row_index < len(self.original_seat_list):
                    if column_index >= 0 and column_index < len(self.original_seat_list[row_index]):
                        adjacent_list.append(self.seat_list[row_index][column_index])
        return adjacent_list

    def empty_seat_update(self, seat, adjacency_list):
        if seat == self.empty_seat:
            if self.occupied_seat not in adjacency_list:
                seat = self.occupied_seat
        return seat

    def occupied_seat_update(self, seat, adjacency_list):
        if seat == self.occupied_seat:
            count = 0
            for spot in adjacency_list:
                if spot == self.occupied_seat:
                    count += 1
            if count >= 4:
                seat = self.empty_seat
        return seat

    def find_seat_changes(self):
        previous_seat_layout = copy.deepcopy(self.seat_list)
        new_layout = self.seat_list
        for row in range(0, len(self.seat_list)):
            for column in range(0, len(self.seat_list[row])):
                new_layout[row][column] = self.update_seat(row, column)
                self.seat_list = new_layout
        return previous_seat_layout == new_layout

test = SeatingSystem('day11')
original_list = test.original_seat_list
test.display_original_seat_layout()
print()
test.display_clean_seat_layout()

new_layout = test.seat_list
for row in range(0, len(test.seat_list)):
    for column in range(0, len(test.seat_list[row])):
        new_layout[row][column] = test.update_seat(row, column)
test.seat_list = new_layout

print()
test.display_clean_seat_layout()

print()
for x in range(0, 100):
    if test.find_seat_changes() == True:
        count = 0
        for row in range(0, len(test.seat_list)):
            for column in range(0, len(test.seat_list[row])):
                if test.seat_list[row][column] == test.occupied_seat:
                    count += 1
    print(count)
print(test.seat_list)