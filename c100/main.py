class Car(object):
    def __init__(self, model, color, company, speed_limit):
        self.model = model
        self.color = color
        self.company = company
        self.speed_limit = speed_limit

    def start (self):
        print("Car is starting")
    
    def stop (self):
        print("Car is stopping")

    def accelerate (self):
        print("Car is accelerating")
    
    def change_gear (self, gear_type):
        print("Car is changing gear to " + gear_type)
        "Gear related funtionality here"


print('start')

audi = Car('A4', 'black', 'Audi', 120)

audi.start()
audi.accelerate()
audi.change_gear('D')
audi.stop()