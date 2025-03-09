class PhoneBook:
    def __init__(self):
        self.__phones = list()

    def add_phone(self, phone):
        self.__phones.append(phone)

    def remove_phone(self, indx):
        self.__phones.remove(indx)

    def get_phone_list(self):
        return self.__phones


class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio
