# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, num_room, population):
        self.num_room = num_room
        self.population = population

    def get_person_room(self):
        return self.num_room

    def get_city_population(self):
        return self.population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.
person1 = Person(42, 522000)

print(person1.get_person_room())