class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def floor_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print ("Floor:", self.floor)

    def floor_down(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print ("Floor:", self.floor)

    def go_to_floor(self, target):
        if target < self.bottom_floor or target > self.top_floor:
            print ("That floor does not exist")
            return

        while self.floor < target:
            self.floor_up()

        while self.floor > target:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.elevators = []

        for i in range(elevator_count):
            lift = Elevator(bottom_floor, top_floor)
            self.elevators.append(lift)

    def run_elevator (self, number, target):
        if number < 1 or number > len(self.elevators):
            print("Wrong elevator number")
            return

        print ("Elevator", number)
        self.elevators[number - 1].go_to_floor(target)
 

lazy_hotel = Building (1, 6, 2)
lazy_hotel.run_elevator ( 1, 5)
lazy_hotel.run_elevator (2, 3)