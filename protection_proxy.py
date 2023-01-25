


class Driver:
    def __init__(self, name: str,aga:int):
        self.aga = aga
        self.name = name

class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"the car is driven by {self.driver.name}")

class CarProxy:
    def __init__(self, driver:Driver):
        self._car=Car(driver)
        self._driver=driver

    def drive(self):
        if self._driver.aga >=16:
            self._car.drive()
        else:
            print("the driver is too young")

if __name__ == '__main__':
    driver=Driver("John", 16)
    car= CarProxy(driver)
    car.drive()
