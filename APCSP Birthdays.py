students = []
class Student:

    gender = 0
    firstName = ""
    lastName = ""
    dayOfBirth = ""
    monthOfBirth = ""
    yearOfBirth = ""

    def __init__(self, gen, first, last, day, month, year):
        self.gender = gen
        self.firstName = first
        self.lastName = last
        self.dayOfBirth = day
        self.monthOfBirth = month
        self.yearOfBirth = year

    def getName(self):
        return self.firstName

    def printTraits(self):
        #guy
        if self.gender == 1:
            return "This student's name is " + self.firstName + " " + self.lastName + ". He was born on " + self.monthOfBirth + " " + self.dayOfBirth + ", " + self.yearOfBirth + "."
        #girl
        elif self.gender == 2:
            return "This student's name is " + self.firstName + " " + self.lastName + ". She was born on "  + self.monthOfBirth + " " + self.dayOfBirth + ", " + self.yearOfBirth + "."

while "spicybois" is "spicybois":
    choice = input("Input 1) to add a person or 2) to search for a person.")
    #add
    if choice is 1:
        gen = input("Input 1) if you are a guy or input 2) if you are a girl.")
        first = raw_input("Input your first name.")
        last = raw_input("Input your last name.")
        day = raw_input("Input your day of birth.")
        month = raw_input("Input your month of birth.")
        year = raw_input("Input your year of birth.")

        print("\nCreating your person...\n")

        tempStudent = Student(gen, first, last, day, month, year)
        students.append(tempStudent)
        print("Printing traits...")
        print(tempStudent.printTraits()+"\n\n1")

    #search
    elif choice is 2:
        searchNam = raw_input("Please input the name you would like to search for: ")
        for x in range(len(students)):
            if students[x].getName() == searchNam:
                print(students[x].printTraits() + "\n\n")
                break