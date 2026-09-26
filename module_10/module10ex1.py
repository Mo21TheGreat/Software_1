class Elevator:
    def __init__(self, bottom, top):
        self.bottom_floor = bottom
        self.top_floor = top
        self.floor = bottom

    def floor_up(self):
        if self.floor < self.top_floor:
            self.floor += 1
            print("Elevator is now at floor", self.floor)

    def floor_down(self):
        if self.floor > self.bottom_floor:
            self.floor -= 1
            print("Elevator is now at floor", self.floor)

    def go_to_floor(self, target):
        while self.floor < target:
            self.floor_up()

        while self.floor > target:
            self.floor_down()