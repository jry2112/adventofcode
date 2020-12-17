def parse(file):
    with open(file) as f:
        input_list = [line.rstrip('\n') for line in f]
    return input_list


class SeatingSystem:

    def __init__(self, input):
        self.occupied_seat = "L"
        self.floor = "."
        self.original_seat_list = parse(input)

    def display_original_seat_layout(self):
        for row in range(0, len(self.original_seat_list)):
            print(self.original_seat_list[row])

    def update_seats(self):

test_original = SeatingSystem('day11test')
test_original.display_original_seat_layout()