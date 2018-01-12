class Car:

    #variables to be assigned per each instance of Car
    carType = ""
    licensePlate = ""
    serialNumber  = ""
    fuel = 0
    distance = 0

    cars = ["Ferrari", "Toyota", "Mazda"]

    #This assigns numbers/variables to each specific trait of different instances of each Car
    def __init__(self, typeOfCar, licenseNum, serNum, fuelNum):
        self.carType = self.cars[typeOfCar]
        self.licensePlate = licenseNum
        self.serialNumber = serNum
        self.fuel = fuelNum

    def getGas(self):
        return self.fuel
    def getCarType(self):
        return self.carType
    def getSerNum(self):
        return self.serialNumber
    def getDistance(self):
        return self.distance

    def getTraits(self):
        print("On your " + self.carType +", you've travelled " + str(self.distance) + " miles with " + str(self.fuel) + " gallons of gas left.")


    def go(self):
        if self.fuel is not 0:
            if self.carType is "Ferrari":
                self.fuel -= 1
                self.distance += 17

            elif self.carType is "Toyota":
                self.fuel -= 1
                self.distance += 42

            elif self.carType is "Mazda":
                self.fuel -= 1
                self.distance += 38

            self.getTraits()

        elif self.fuel is 0:
            print("Your car has no fuel :(")


print("Hello and welcome to this car creation program.")
carType = input("Please input the following:\n"
                  "1) For a Ferrari\n"
                  "2) For a Toyota\n"
                  "3) For a Mazda")
licenseNum = raw_input("Please input your license number: ")
serNum = raw_input("Please input the serial number: ")
fuelNum = input("Now, finally, input how much your car has.\n")
print("Creating car...\n\n")

testCar = Car(carType,licenseNum,serNum,fuelNum)

print("Voila! Your car is created.")

while (1 is 1):
    choice = input("Please input the following.\n"
                       "1) To travel\n"
                       "2) To print traits\n"
                       "3) To exit.")
    if choice is 1:
        testCar.go()
    elif choice is 2:
        testCar.getTraits()
    elif choice is 3:
        break
    else:
        print("Try again.")






