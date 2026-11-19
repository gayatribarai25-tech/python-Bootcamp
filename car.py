'''Create a class Car with brand and speed (default 0). Add accelerate(amount) and brake(amount) methods that change the speed and print it. Brake must never take the speed below 0.'''


class Car:
    def __init__(self,brand,speed=0):
        self.brand = brand
        self.speed=speed
        
    def accelerate(self, amount):
        self.speed += amount
        print(f"{self.brand} speed: {self.speed}")

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)
        print(f"{self.brand} speed: {self.speed}")

car1 = Car("BMW")
car1.accelerate(20)
car1.accelerate(10)
car1.brake(15)
car1.brake(50)

