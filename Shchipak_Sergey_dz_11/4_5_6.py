class OwnDigitError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Store:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start_capacity = capacity
        self.stored_equipment = []
        self.equipment_to_store = []

    def place_to_store(self, equipment):
        volume = 0
        for i in range(len(equipment)):
            volume += equipment[i].volume
            self.equipment_to_store.append(equipment[i])
        if volume > self.capacity:
            print(f"Нет достаточного места для размещения оргтехники")
            self.equipment_to_store.clear()
            volume = 0
        else:
            for item in self.equipment_to_store:
                self.stored_equipment.append(item)
                print(f"На складе размещен {item.name} марки {item.model} объемом {item.volume}")
            self.capacity -= volume
            print(f"Оставшееся место на складе: {self.capacity}")
            print(f"Количество объектов на складе: {len(self.stored_equipment)}, "
                  f"общим объемом {(self.start_capacity - self.capacity)}")
            self.equipment_to_store.clear()

    def move_to_div(self, division, type_equipment, quantity):
        quantity_to_move = 0
        try:
            if type(quantity) == int:
                quantity_to_move = quantity
            else:
                raise OwnDigitError("Веденное значение количества для перемещения не является числом")
        except OwnDigitError as err:
            print(err)
        volume_to_move = 0
        equipment_to_move = []
        while quantity_to_move > 0:
            for i in range(len(self.stored_equipment)):
                if (self.stored_equipment[i]).name == type_equipment:
                    volume_to_move += (self.stored_equipment[i]).volume
                    equipment_to_move.append(self.stored_equipment[i])
                    quantity_to_move -= 1
                    if quantity_to_move == 0:
                        break
                if i == (len(self.stored_equipment) - 1) and quantity_to_move > 0:
                    print(f"На складе нет запрошенного количества ({quantity}шт) позиций типа {type_equipment}. "
                          f"Будет отгружено {quantity - quantity_to_move} шт.")
                    quantity_to_move = 0
        if volume_to_move > division.div_capacity:
            print(f"Нет достаточного места для размещения оргтехники в подразделении")
        else:

            for item in equipment_to_move:
                division.stored_equipment.append(item)
                self.stored_equipment.remove(item)
                print(f"Со склада перемещен {item.name} марки {item.model} объемом {item.volume}.")
                print(f"В подразделении {division.name} размещен {item.name} "
                      f"марки {item.model} "
                      f"объемом {item.volume}.")
            self.capacity += volume_to_move
            division.div_capacity -= volume_to_move
            print(f"Количество объектов на складе: {len(self.stored_equipment)}, "
                  f"общим объемом {(self.start_capacity - self.capacity)}. "
                  f"Оставшееся место на складе: {self.capacity}."
                  f"Оставшееся место в подразделении {division.name}: {division.div_capacity}")
            equipment_to_move.clear()


class Division(Store):
    def __init__(self, name, div_capacity):
        Store.__init__(self, capacity=0)
        self.name = name
        self.div_capacity = div_capacity
        self.start_capacity = div_capacity
        self.div_stored_equipment = []


class OfficeEquipment:
    def __init__(self):
        self.volume = 0
        self.name = ''


class Printer(OfficeEquipment):
    def __init__(self, model):
        OfficeEquipment.__init__(self)
        self.model = model
        self.name = 'Принтер'
        if self.model == 'OKI':
            self.volume = 40
        elif self.model == 'HP':
            self.volume = 35
        else:
            self.volume = 45


class Scaner(OfficeEquipment):
    def __init__(self, model):
        OfficeEquipment.__init__(self)
        self.model = model
        self.name = 'Сканер'
        if self.model == 'Kyosera':
            self.volume = 10
        elif self.model == 'ScanJet':
            self.volume = 5
        else:
            self.volume = 15


class Copier(OfficeEquipment):
    def __init__(self, model):
        OfficeEquipment.__init__(self)
        self.model = model
        self.name = 'Копир'
        if self.model == 'Canon':
            self.volume = 20
        elif self.model == 'Xerox':
            self.volume = 15
        else:
            self.volume = 25


store1 = Store(250)
div1 = Division('Бухгалтерия', 150)
prin1 = Printer("OKI")
prin2 = Printer("HP")
cop1 = Copier("Xerox")
sca1 = Scaner("Kyosera")

Store.place_to_store(store1, [prin1, prin2])
print("\n")
Store.place_to_store(store1, [cop1, sca1])
print("\n")
Store.move_to_div(store1, div1, "Принтер", "nnns")
print("\n")
Store.move_to_div(store1, div1, "Принтер", 2)
