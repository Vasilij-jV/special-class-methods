# -*- config: utf-8 -*-

class House:

    def __init__(self):
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print('Этаж номер:', floors)


house = House()
house.setNewNumberOfFloors(floors=67)

