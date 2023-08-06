from collections import UserList
from datetime import datetime
import pickle
from colorama import init
from colorama import Fore, Back
init()
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


class NoteBook(UserList):
    def __init__(self):
        self.data = []

    def generator(self):
        for it in self.data:
            yield it

    def list_names(self):
        return {str(it.name) for it in self.data}
    
    def list_tags(self):
        list_tags = set()
        for it in self.data:
            for item in it.tags.value:
                list_tags.add(item)
        return list_tags  
    
    def iterator(self, value):
        value = value
        gen = self.generator()
        while value > 0:
            try:
                if self.data == []:
                    print("    > Your notebook is empty(")
                print(next(gen))
                value -= 1
            except StopIteration:
                return ""
        print("    > Thats all!") 

    def add(self, rec):
        self.data.append(rec)
        print(f"    > You have added a note: {rec.name}")
        print(f"    > {rec}")


    def remove(self, name):
        for it in self.data:

            if str(it.name) == name.title():
                print(f"  > You have deleted the note {name}")
                self.data.remove(it)
                return
        print(Fore.WHITE + Back.RED +"  > Note with this name was not found.")


    def edit(self, name):
        for it in self.data:
            if str(it.name) == name.title():  
                while True:
                    comm_list = WordCompleter(["Name", "Tags", "Note"], ignore_case = True)
                    value = prompt("    > Choose what to edit. Name/Tags/Note: ", completer = comm_list, complete_while_typing = True).title()
                    if value == "Name":
                        it.name = NoteName()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    elif value == "Tags":
                        it.tags = Tag()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    elif value == "Note":
                        it.note = Note()
                        it.time = TimeRec()
                        print(f"  > {it}")
                        break
                    else:

                        print("  > I don't know what it is(")
                        break
        print(Fore.WHITE + Back.RED +"  > Note with this name was not found.")

    def search(self, value):
        if value == "Name":
            comm_list = WordCompleter(self.list_names(), ignore_case = True)
            name = prompt("    > Enter the name of the note: ", completer = comm_list, complete_while_typing = True)
            for it in self.data:
                if str(it.name) == name.title():
                    print(it)
            print("  > Thats all!")

        elif value == "Tags":
            comm_list = WordCompleter(self.list_tags(), ignore_case = True)
            tag = prompt("    > Enter the tag of the note: ", completer = comm_list, complete_while_typing = True)
            for it in self.data:
                for item in it.tags.value:   
                    if item == tag:
                        print(it)
            print("  > Thats all!")


        elif value == "Note":
            note = input("    > Enter the note: ")
            for it in self.data:
                if (it.note.value.find(note[1:]) > 0) or (it.note.value.find(note) > 0):
                    print(it)
            print("  > Thats all!")



    def save(self):
        with open("nbsave.bin", "wb") as fl:
            print("    > Information saved.")
            pickle.dump(self.data, fl)

    def load(self):
        try:
            with open("nbsave.bin", "rb") as fl:
                self.data = pickle.load(fl)
                print("    > Information is loaded.")
           
        except FileNotFoundError:
            print(Fore.WHITE + Back.RED +"  > Save file not found.")


######################################

class NoteName:
    def __init__(self):
        while True:
            self.inp = input("    > Name of the note: ")
            if len(self.inp.replace(" ", "")) > 20:
                print(Fore.WHITE + Back.RED +"  > The title is too long......... Must be less than 20.")
            elif self.inp == "":
                print("    > Please enter the name of the note.")
            else:
                self.value = self.inp.title()
                break
                

    def __repr__(self):
        return f"{self.value}"
    

class Tag:
    def __init__(self):
        while True:
            self.inp = (input("    > Enter tags separated by a space: ")).split(" ")
            if len(self.inp) < 10:
                self.value = self.inp
                break
            else:
                print(Fore.WHITE + Back.RED +"  > Too long......... Must be less than 10.")

    def __repr__(self):
        return f"#{' #'.join(self.value)}"


class Note:
    def __init__(self):
        while True:
            self.inp = input("    > Note: ")
            if len(self.inp.replace(" ", "")) < 500:
                self.value = self.inp
                break
            else:
                print(Fore.WHITE + Back.RED +"  > Too long......... Must be less than 500.")

    def __repr__(self):
        return f"{self.value}"


class TimeRec:
    def __init__(self):
        self.value = datetime.today()

    def __repr__(self):
        return f"{self.value.strftime('%d %b %Y, %H:%M')}"


######################################

class Record:

    def __init__(self, name="", tags="", note="", time=""):

        self.name = name
        self.tags = tags
        self.note = note
        self.time = time

    def __repr__(self):
        return f"\n  > {self.name}     {self.time}\n{self.tags}\n{self.note}"

######################################

class Bot:
    def __init__(self):
        self.book = NoteBook()
        self.book.load()

    def handle(self, comand):
        if comand == 'add':
            name = NoteName()
            tags = Tag()
            note = Note()
            time = TimeRec()
            record = Record(name, tags, note, time)
            return self.book.add(record)
        elif comand == "show":
            while True:
                try:
                    num = int(input("    > How much: "))
                    return self.book.iterator(num)
                except ValueError:
                    print("    > Enter a number")
        elif comand == "remove":
            comm_list = WordCompleter(self.book.list_names(), ignore_case = True)
            name = prompt("    > Enter the name of the note you want to delete: ", completer = comm_list, complete_while_typing = True)
            return self.book.remove(name)
        elif comand == "edit":
            comm_list = WordCompleter(self.book.list_names(), ignore_case = True)
            name = prompt("    > Enter the name of the note you want to edit: ", completer = comm_list, complete_while_typing = True)
            return self.book.edit(name)
        elif comand == "search":
            comm_list = WordCompleter(["Name", "Tags", "Note"], ignore_case = True)
            value = prompt("    > Choose what to look for. Name/Tags/Note: ", completer = comm_list, complete_while_typing = True).title()
            return self.book.search(value)
        elif comand == "save":
            return self.book.save()
        elif comand == "load":
            return self.book.load()
        else:
            print(Fore.WHITE + Back.RED +f"  > I don't know such a command(")



######################################
            
def main(): 
    bot = Bot()

    comm_list = WordCompleter(["add", "show", "remove", "edit", "search", "save", "load", "exit"], ignore_case = True)
    print("    > Hello. I am a notebook assistant. Shall we add a note?")

    while True:
        comand = prompt("    > Your command: ", completer = comm_list, complete_while_typing = True).lower().strip()
        if comand in ["exit", "close"]:
            print("    > Save data?")
            comm_list = WordCompleter(["YES", "NO"], ignore_case = True)
            comand = prompt("    > If YES press 'Y' and 'N' if NO: ", completer = comm_list, complete_while_typing = True)
            if comand in ["YES", "Y"]:
                print("    > Bye!")

                return bot.book.save()
            else:
                print("    > Bye!")
                return
        else:
            bot.handle(comand)

######################################
    
if __name__ == "__main__":
    main()