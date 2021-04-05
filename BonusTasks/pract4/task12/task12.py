class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.__surname = surname
        self.__age = age

    def get_info(self):
        return 'Name: {} {}\nAge: {}'.format(str(self.name),
                                             str(self.__surname),
                                             str(self.__age))


def task1():
    """
    Напишите код, который выведет на экране все переменные объекта
    произвольного пользовательского класса.
    :return:
    """
    print('Task 1')
    p1 = Person('Rod', 'Plug', 20)
    print(dir(p1))
    print(vars(p1))
    print(p1.__dict__)


def task2():
    """
    Напишите код, который по имени метода, заданному строкой, вызовет этот
    метод в некотором пользовательском классе.
    :return:
    """
    print('\nTask 2')
    p1 = Person('Rod', 'Plug', 20)
    method_to_invoke = getattr(p1, 'get_info')
    print(method_to_invoke())



if __name__ == '__main__':
    task1()
    task2()