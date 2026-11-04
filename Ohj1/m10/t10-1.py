class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.floor = bottom_floor

    def floor_up (self):
        if self.floor < self.top_floor:
            self.floor += 1
            print ("Floor:", self.floor)

    def floor_down (self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print ("Floor:", self.floor)

    def go_to_floor (self, target):
        if target < self.bottom_floor or target > self.top_floor:
            print ("That floor does not exist")
            return

        while self.floor < target:
            self.floor_up()

        while self.floor > target:
            self.floor_down()


lazy_lift = Elevator(1, 6)
lazy_lift.go_to_floor(5)
lazy_lift.go_to_floor(1)