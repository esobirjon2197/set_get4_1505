
# 7-m
class University:
    def __init__(self, name, students_count):
        self.name = name
        self.__students_count = students_count

    def get_students_count(self):
        return self.__students_count

    def set_students_count(self, new_count):
        if new_count > self.__students_count:
            self.__students_count = new_count
            print("Talabalar soni yangilandi")
        else:
            print("Talabalar soni kamaymaydi")


u1 = University("TATU", 12000)
print(u1.name)
print(u1.get_students_count())

u1.set_students_count(13000)
print(u1.get_students_count())

u1.set_students_count(10000)
print(u1.get_students_count())


# 8-m
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def get_age(self):
    return self.__age


    def set_age(self, new_age):
    if new_age >= 0:
        self.__age = new_age
        print("Yosh yangilandi")
        else:
        print("Yosh xato")


a1 = Animal("Sher", 5)
print(a1.name)
print(a1.get_age())

a1.set_age(7)
print(a1.get_age())

a1.set_age(-1)
print(a1.get_age())
