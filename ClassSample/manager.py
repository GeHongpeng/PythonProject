from person import Person

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, "Manager")
    
    def giveRaise(self, percent, bonus=0.1):
        Person.giveRaise(self, percent + bonus)

if __name__ == "__main__":
    bob = Person("Bob Smith", 44)
    sue = Person("Sue Jones", 47, 40000, "hardware")
    tom = Manager(name="Tom Doe", age=50, pay=50000)

    print(sue, sue.pay, sue.lastName())

    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)
