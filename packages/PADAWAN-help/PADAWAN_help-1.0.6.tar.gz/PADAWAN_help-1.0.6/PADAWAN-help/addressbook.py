from collections import UserDict
import re
from datetime import datetime
import sys
# from json import dump, load, JSONEncoder
import pickle
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import init
from colorama import Fore, Back
init()


class Field:
    def __init__(self):
        self._value = None


class Name(Field):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'^\+?3?8?(0[\s\.-]?\d{2}[\s\.-]?\d{3}[\s\.-]?\d{2}[\s\.-]?\d{2})$', value):
            self._value = value
        else:
            raise PhoneError(Fore.WHITE + Back.RED +
                             "  > Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38")


class Address(Field):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Email(Field):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', value):
            self._value = value
        else:
            raise EmailError(Fore.WHITE + Back.RED +
                             "  > Email must have format (string1)@(string2).(2+characters)")


class Birthday(Field):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if re.search(r'\d{2}\.\d{2}\.\d{4}', value):
            self._value = value
        else:
            raise BirthdayError(Fore.WHITE + Back.RED +
                                "  > Birthday must have format 'DD.MM.YYYY' and consist only from numbers")


class Record:
    def __init__(self, name: Name, phone: Phone = None, address: Address = None, email: Email = None,  birthday: Birthday = None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
        self.address = address
        self.email = email

    def __repr__(self) -> str:
        return f'Name: {self.name}, Phones: {self.phones}, Address: {self.address}, Email: {self.email}, Birthday: {self.birthday}'

    def add_phones(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def change_phones(self, phone, phone_new: Phone):
        for count, ele in enumerate(self.phones):
            if ele.value == phone:
                self.phones[count] = phone_new
                break

    def change_email(self, email, email_new: Email):
        for count, ele in enumerate(self.phones):
            if ele.value == email:
                self.phones[count] = email_new
                break

    def change_address(self, address, address_new: Address):
        for count, ele in enumerate(self.address):
            if ele.value == address:
                self.phones[count] = address_new
                break

    def change_birthday(self, birthday, birthday_new: Birthday):
        for count, ele in enumerate(self.birthday):
            if ele.value == birthday:
                self.phones[count] = birthday_new
                break

    def remove_phones(self, phone):
        for count, ele in enumerate(self.phones):
            if ele.value == phone:
                self.phones.remove(ele)
                break

    def list_phones(self):
        return self.phones

    def add_birthday(self, birthday: Birthday):
        self.birthday = birthday

    def add_email(self, email: Email):
        self.email = email

    def add_address(self, address: Address):
        self.address = address

    def days_to_birthday(self):
        if self.birthday is None:
            return None
        birthday = datetime.strptime(self.birthday.value, '%d.%m.%Y')
        now = datetime.now()
        delta1 = datetime(now.year, birthday.month, birthday.day)
        delta2 = datetime(now.year+1, birthday.month, birthday.day)
        return ((delta1 if delta1 > now else delta2) - now).days + 1

    def sub_find_name_phone(self, value):
        if self.name.value.lower().find(value.lower()) != -1:
            print(self)
        else:
            for i in self.phones:
                if i.value.find(value) != -1:
                    print(self)
                    break


class AddressBook(UserDict):

        

    def __repr__(self):
        return f'{self.data}'

    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return self.data

    def iterator(self, n=2):
        index = 0
        lst_temp = []
        for k, v in self.data.items():
            lst_temp.append(v)
            index = index + 1
            if index >= n:
                yield lst_temp
                lst_temp.clear()
                index = 0
        if lst_temp:
            yield lst_temp

    def show_all_limit(self, n=2):
        step = self.iterator(n)
        for i in range(len(self.data)):
            try:
                result = next(step)
                print(result)
                input('    > Press enter for next page: ')
            except StopIteration:
                break

    def save_to_file(self):
        with open("absave.bin", "wb") as fl:
            print("    > Information saved.")
            pickle.dump(self.data, fl)

    def read_from_file(self):
        try:
            with open("absave.bin", "rb") as fl:
                self.data = pickle.load(fl)
                print("    > Information is loaded.")
                return self.data
        except FileNotFoundError:
            print(Fore.WHITE + Back.RED + "  > Save file not found.")


# class MyEncoder(JSONEncoder):
#   def default(self, obj):
#        return obj.__dict__


class PhoneError(Exception):
    """Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38"""
    pass


class EmailError(Exception):
    """Email must have format (string1)@(string2).(2+characters)"""
    pass


class BirthdayError(Exception):
    """Birthday must have format 'DD.MM.YYYY' and consist only from numbers"""
    pass


# command  - command value
# name - first value after command (name)
# phone - second value after command (phone)
# phone_new - third value after command (phone_new for changing phones)
# birthday - birthday of person, econd value after command in func add_name_birthday
# n - quantity of viewes in adress book
# filename - the name of file to save instance of class Adress Book
# value - sub of name or phone
# days_in - number of days before birthday
# *other - possible value in the end of command string, that user can input


def input_error_name_phone(func):
    def wrapper(output_list, address_book):
        try:
            name, phone, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED +
                  '  > Give me name and phone please. Format of phone must be +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX')
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_name_birthday(func):
    def wrapper(output_list, address_book):
        try:
            name, birthday, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED +
                  "  > Give me name and birthday please. Birthday must have format 'DD.MM.YYYY' and consist only from numbers")
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_name_email(func):
    def wrapper(output_list, address_book):
        try:
            name, email, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED +
                  "  > Give me name and email please. Email must have format (string1)@(string2).(2+characters)")
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_name_address(func):
    def wrapper(output_list, address_book):
        try:
            name, address, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED + "  > Give me name and address please")
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_days_before_birthday(func):
    def wrapper(output_list, address_book):
        try:
            days_in, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED +
                  "  > Give integer number of days before birthday you want to check")
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_filename(func):
    def wrapper(output_list, address_book):
        try:
            filename = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED +
                  "  > Give me filename please")
        else:
            return func(output_list, address_book)
    return wrapper


def input_error_name_phone_phone_new(func):
    def wrapper(output_list, address_book):
        try:
            name, phone, phone_new, *other = output_list
        except ValueError:
            print(Fore.WHITE + Back.RED + '  > Give me name, phone and new phone please. Format new phone must be +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX')
        else:
            return func(output_list, address_book)
    return wrapper


def hello(output_list, address_book: AddressBook):
    print("    > How can I help you?")


@input_error_name_phone
def add_name_phone(output_list, address_book: AddressBook):
    name, phone, *other = output_list
    record = address_book.get(name)
    if record:
        try:
            record.add_phones(Phone(phone))
            # print(address_book)
            print(f'    > New phone {phone} of {name} is added')
        except PhoneError:
            print(Fore.WHITE + Back.RED + "  > Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38'")
    else:
        try:
            address_book.add_record(
                Record(name=Name(name), phone=Phone(phone)))
            # print(address_book)
            print(
                f'    > New contacts (name: {name}, phone: {phone}) are added')
        except PhoneError:
            print(Fore.WHITE + Back.RED + "  > Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38'")


@input_error_name_birthday
def add_name_birthday(output_list, address_book: AddressBook):
    name, birthday, *other = output_list
    record = address_book.get(name)
    if record:
        if record.birthday is None:
            try:
                record.add_birthday(Birthday(birthday))
                # print(address_book)
                print(f'    > Birthday of {name} is added')
            except BirthdayError:
                print(Fore.WHITE + Back.RED +
                      "  > Birthday must have format 'DD.MM.YYYY' and consist only from numbers")
        else:
            print("    > Choose command 'change birthday'")

    else:
        try:
            address_book.add_record(
                Record(name=Name(name), birthday=Birthday(birthday)))
            # print(address_book)
            print(
                f'    > New contacts (name: {name}, birthday: {birthday}) are added')
        except BirthdayError:
            print(Fore.WHITE + Back.RED +
                  "  > Birthday must have format 'DD.MM.YYYY' and consist only from numbers")


@input_error_name_address
def add_name_address(output_list, address_book: AddressBook):
    name = output_list[0]
    address = " ".join(output_list[1:])
    record = address_book.get(name)
    if record:
        if record.address is None:
            record.add_address(Address(address))
            # print(address_book)
            print(f'    > Address of {name} is added')
        else:
            print(f"    > Choose command 'change address'")
    else:
        address_book.add_record(
            Record(name=Name(name), address=Address(address)))
        # print(address_book)
        print(
            f'    > New contacts (name: {name}, address: {address}) are added')


@input_error_name_address
def change_address(output_list, address_book: AddressBook):
    name = output_list[0]
    address = " ".join(output_list[1:])
    record = address_book.get(name)
    if record:
        record.add_address(Address(address))
        # print(address_book)
        print(f'    > Address of {name} is changed')


@input_error_name_email
def change_email(output_list, address_book: AddressBook):
    name, email, *other = output_list
    record = address_book.get(name)
    if record:
        try:
            record.add_email(Email(email))
            # print(address_book)
            print(f'    > Email of {name} is changed')
        except EmailError:
            print(Fore.WHITE + Back.RED +
                  "  > Email must have format (string1)@(string2).(2+characters)")


@input_error_name_birthday
def change_birthday(output_list, address_book: AddressBook):
    name, birthday, *other = output_list
    record = address_book.get(name)
    if record:
        try:
            record.add_birthday(Birthday(birthday))
            # print(address_book)
            print(f'    > Birthday of {name} is changed')
        except BirthdayError:
            print(Fore.WHITE + Back.RED +
                  "  > Birthday must have format 'DD.MM.YYYY' and consist only from numbers")


@input_error_name_email
def add_name_email(output_list, address_book: AddressBook):
    name, email, *other = output_list
    record = address_book.get(name)
    if record:
        if record.email is None:
            try:
                record.add_email(Email(email))
                # print(address_book)
                print(f'    > Email of {name} is added')
            except EmailError:
                print(Fore.WHITE + Back.RED +
                      "  > Email must have format (string1)@(string2).(2+characters)")
        else:
            print("    > Choose command 'change email'")
    else:
        try:
            address_book.add_record(
                Record(name=Name(name), email=Email(email)))
            # print(address_book)
            print(
                f'    > New contacts (name: {name}, email: {email}) are added')
        except EmailError:
            print(Fore.WHITE + Back.RED +
                  "  > Email must have format (string1)@(string2).(2+characters)")


@input_error_days_before_birthday
def birthday_in_days(output_list, address_book: AddressBook):
    days_in, *other = output_list
    days_in = int(days_in)
    for k, v in address_book.items():
        record = address_book.get(k)
        if days_in == record.days_to_birthday():
            print("  > Don't forget to congratulate with birthday:")
            print(record)


@input_error_name_phone_phone_new
def change_phone(output_list, address_book: AddressBook):
    name, phone, phone_new, *other = output_list
    record = address_book.get(name)
    if record:
        try:
            record.change_phones(phone, Phone(phone_new))
            # print(address_book)
            print(
                f'    > Phone {phone} of {name} is changed. New phone is {phone_new} ')
        except PhoneError:
            print(Fore.WHITE + Back.RED + "  > Phone number must consist only from numbers and have format: +380 XX XXX XX XX, +380-XX-XXX-XX-XX, +380.XX.XXX.XX.XX or without '+38'")


@input_error_name_phone
def remove_phone(output_list, address_book: AddressBook):
    name, phone, *other = output_list
    record = address_book.get(name)
    if record:
        record.remove_phones(phone)
        # print(address_book)
        print(f'    > Phone {phone} of {name} is removed')


def remove_contact(output_list, address_book: AddressBook):
    name, *extra = output_list
    record = address_book.get(name)
    if record:
        address_book.pop(name)
        # print(address_book)
        print(f'    > Contact: {name} has been removed')


def find_name_phone(output_list, address_book: AddressBook):
    value, *other = output_list
    for k, v in address_book.items():
        record = address_book.get(k)
        record.sub_find_name_phone(value)


def show_all(output_list, address_book: AddressBook):
    if output_list:
        n, *other = output_list
        address_book.show_all_limit(int(n))
    else:
        address_book.show_all_limit()


def exit_from_chat():
    print('    > Exit from AddressBook')


# @input_error_filename
# def write_contacts_to_file(output_list, address_book: AddressBook):
#     filename, *other = output_list
#     address_book.save_to_file(filename)
#     print('    > File is saved')

def write_contacts_to_file(output_list, address_book: AddressBook):
    address_book.save_to_file()
    print('    > File is saved')

# @input_error_filename
# def read_contacts_from_file(output_list, address_book: AddressBook):
#     filename, *other = output_list
#     address_book.read_from_file(filename)
#     print('    > File is read')


def read_contacts_from_file(output_list, address_book: AddressBook):
    address_book.read_from_file()
    print('    > File is read')

def main():
    address_book = AddressBook()
    # address_book.read_from_file()

    COMMANDS = {'hello': hello,  'add phone': add_name_phone, 'add birthday': add_name_birthday, 'add email': add_name_email, 'add address': add_name_address, 'change phone': change_phone,
                'change address': change_address, 'change email': change_email, 'change birthday': change_birthday,
                'remove phone': remove_phone, 'remove contact': remove_contact, 'show all': show_all, 'find': find_name_phone, 'exit': exit_from_chat, 'save': write_contacts_to_file, 'load': read_contacts_from_file, 'birthday in days': birthday_in_days}

    while True:
        command_completer = WordCompleter(COMMANDS.keys(), ignore_case=True)
        commands_string = prompt(
            '    > Enter your command:', completer=command_completer, complete_while_typing=False).lstrip()
        if commands_string.lower().startswith('exit'):
            print("    > Save data?")
            comm_list = WordCompleter(["YES", "NO"], ignore_case = True)
            comand = prompt("    >If YES press 'Y' and 'N' if NO: ", completer = comm_list, complete_while_typing = True)
            if comand in ["YES", "Y"]:
                print("    > Bye!")
                return write_contacts_to_file(address_book,address_book)
            exit_from_chat()
            break

        for i in COMMANDS.keys():
            if commands_string.lower().startswith(i):
                command = commands_string[:len(i)].lower()
                command_parametres_list = commands_string[len(
                    i)+1:].capitalize().split()
                COMMANDS[command](command_parametres_list, address_book)
                break


if __name__ == '__main__':
    main()
