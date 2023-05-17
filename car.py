class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def state(self):
        print("Im going {} kph!".format(self.speed))

    def accelerate(self):
        self.speed = self.speed + 5

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed = self.speed - 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


if __name__ == '__main__':
    my_car = Car()
    print("Car is started.")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake,"
                       "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("Unable to perform request")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} miles".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} mph".format(my_car.average_speed()))
        my_car.step()
        my_car.state()
