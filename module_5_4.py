class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
    def __init__(self, name, nbf):
        self.name=name
        self.number_of_floors=nbf
    def go_to(self, new_floor):
        if new_floor<1 or new_floor>self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        fl=self.__verify_floor__(other)
        return self.number_of_floors == fl
    def __lt__(self, other:int):
        fl=self.__verify_floor__(other)
        return self.number_of_floors < fl
    def __le__(self, other:int):
        fl=self.__verify_floor__(other)
        return self.number_of_floors <= fl
    def __gt__(self, other:int):
        fl=self.__verify_floor__(other)
        return self.number_of_floors > fl
    def __ge__(self, other:int):
        fl=self.__verify_floor__(other)
        return self.number_of_floors >= fl
    def __ne__(self, other:int):
        fl=self.__verify_floor__(other)
        return self.number_of_floors != fl
    def __add__(self, other):
        if not isinstance(other, (int,House)):
            raise TypeError("Этаж должен быть целым числом или объектом House")
        fl=other if isinstance(other,int) else other.number_of_floors
        return self.number_of_floors+fl
    def __iadd__(self, other:int):
        if not isinstance(other, (int,House)):
            raise TypeError("Этаж должен быть целым числом или объектом House")
        fl=other if isinstance(other,int) else other.number_of_floors
        self.number_of_floors+=fl
        return self
    def __radd__(self, other):
        return self+other

    @classmethod
    def __verify_floor__(cls, other):
        if not isinstance(other, (int, House)):
            raise TypeError("Этаж должен быть целым числом")
        return other if isinstance(other, int) else other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House ('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)