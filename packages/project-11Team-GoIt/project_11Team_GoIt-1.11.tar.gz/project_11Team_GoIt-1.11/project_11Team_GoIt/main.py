import pickle
import re
from datetime import datetime, timedelta

from colorit import *
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import yes_no_dialog

from Notepad import *
from addressbook import *
from greeting import greeting
from help import *
from sort import *

colorit.init_colorit()

class Error(Exception):
    pass

STOPLIST =[".", "end", "close","exit","bye","good bye"]
users = []



def verificate_email(text:str):
    email_re = re.findall(r"[\w+3\@{1}\w+\.\w+]", text)
    email = "".join(email_re)
    if bool(email) == True:
        return email
    else:
        raise Error

def verificate_birthday(text:str): 
    date_re = re.findall(r"\d{4}\.\d{2}\.\d{2}", text)
    date = "".join(date_re)
    if bool(date) == True:
        return date
    else:
        raise Error

def verificate_number(num): #Done
    flag = True
    try:
        number = re.sub(r"[\+\(\)A-Za-z\ ]", "", num)
        if len(number) == 12:
            number = "+" + number

        elif len(number) == 10:
            number = "+38" + number

        elif len(number) == 9:
            number = "+380" + number

        else:
            flag = False
            raise Error
    except Error:
        print(color(f"This number dont correct {number}",Colors.red))

    return number if flag else ""

def add_user(text:str):  #Done
    text = text.split()
    name = text[0]
    phone = text[1]

    if name in ad:
        return "this user already exist"
    else:
        name = Name(name)
        phone = Phone(phone)
        rec = Record(name, phone)
        ad.add_record(rec)

    return color("Done",Colors.blue)

def show_all(nothing= ""):  # Done
    if len(ad) == 0:
        return (color("AddressBook is empty", Colors.red))
    else:
        number = len(ad)
        ad.iterator(number)
        return color("Done",Colors.blue)

def add_phone(text:str):
    text = text.split()
    name = text[0]
    phone = text[1]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        phone = Phone(phone)
        adding.add_phone(phone)
    
    return color("Done",Colors.blue)

def add_email(text:str):
    text = text.split()
    name = text[0]
    email = text[1]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        email = Email(email)
        adding.add_email(email)

    return color("Done",Colors.blue)

def add_birthday(text:str):
    text = text.split()
    name = text[0]
    birthday = text[1]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        birthday = Birthday(birthday)
        adding.add_birthday(birthday)

    return color("Done",Colors.blue)

def add_tags(text:str):
    text = text.split()
    name = text[0]
    tags = " ".join(text[1:])
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        tags = Tags(tags)
        adding.add_tags(tags)

    return color("Done",Colors.blue)

def add_adress(text:str):
    text = text.split()
    name = text[0]
    adress = " ".join(text[1:])
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adress = Adress(adress)
        adding.add_adress(adress)
        
    return color("Done",Colors.blue)

def change_adress(text:str):
    text = text.split()
    name = text[0]
    adress = " ".join(text[1:])
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adress = Adress(adress)
        adding.change_adress(adress)
        
    return color("Done",Colors.blue)

def change_phone(text:str):
    text = text.split()
    name = text[0]
    oldphone = text[1]
    newphone = text[2]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        # oldphone = Phone(oldphone)
        # newphone = Phone(newphone)
        adding.change_phone(oldphone,newphone)

    return color("Done",Colors.blue)

def change_email(text:str):
    text = text.split()
    name = text[0]
    newemail = text[1]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        newemail = Email(newemail)
        adding.change_email(newemail)

    return color("Done",Colors.blue)

def change_birthday(text:str):
    text = text.split()
    name = text[0]
    birthday = text[1]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        birthday = Birthday(birthday)
        adding.change_birthday(birthday)

    return color("Done",Colors.blue)
    

def remove_phone(text:str):
    text = text.split()
    name = text[0]
    phone = text[1]
    
    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    
    if phone == "-":
        adding = ad[name]
        adding.remove_phone(phone)
    elif name in ad:
        adding = ad[name]
        phone = Phone(phone)
        adding.remove_phone(phone)

    return color("Done",Colors.blue)

def remove_email(text:str):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adding.remove_email()
    
    return color("Done",Colors.blue)

def remove_birthday(text:str):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adding.remove_birthday()
    
    return color("Done",Colors.blue)

def remove_tags(text:str):
    text = text.split()
    name = text[0]
    tags = " ".join(text[1:]).strip()

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adding.remove_tags(tags)
    return color("Done",Colors.blue)

def remove_user(text:str):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        del ad[name]
    return color("Done",Colors.blue)

def remove_adress(text:str):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    elif name in ad:
        adding = ad[name]
        adding.remove_adress()
    return color("Done",Colors.blue)
    
def find_name(text):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    
    elif name in ad:
        print(ad.find_name(name))



    return color("Done",Colors.blue)

def find_tags(text:str):
    text = text.split()
    tags = text[0:]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    
    print(ad.find_tags(tags))
    
    return color("Done",Colors.blue)

def find_phone(text:str):
    text = text.split()
    phone = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    
    print(ad.find_phone(phone))

    return color("Done",Colors.blue)

def when_birthday(text:str):
    text = text.split()
    name = text[0]

    if len(ad) == 0:
        return color("Addressbook is empty", Colors.red)
    if name not in ad:
        return color("This user dont exist in addressbook", Colors.red)
    
    elif name in ad:
        adding = ad[name]
        print(adding.days_to_birthday())
    return color("Done",Colors.blue)

def birthdays_within(text:str):
    days = int(text.split()[0])
    flag = False
    current = datetime.now()
    future = current + timedelta(days=days)

    for name, record in ad.items():
        if record.get_birthday() is None:
            pass
        else:
            userdate = datetime.strptime(record.get_birthday(), "%Y.%m.%d").date()
            userdate = userdate.replace(year=current.year)
            if current.date() < userdate < future.date():
                flag = True
                print(color(f"\n{name.title()} has birthday {record.get_birthday()}",Colors.yellow))
    
    return color("Done",Colors.blue) if flag == True else color("Nobody have birthday in this period",Colors.red)
            

def help(tst=""):
    instruction = color("""
    \nCOMMANDS\n
    show all
    add user <FirstName_LastName> <phone>
    add phone <user> <phone>
    add email <user> <email>
    add birthday <user> <date>
    add tags <user> <tags>
    add adress <user> <adress>
    change adress <user> <new_adress>
    change email <user> <newEmail>
    change birthday <user> <newBirthday>
    remove phone <user> <phone>
    remove email <user> <email>
    remove birthday <user>
    remove phone <user> <phone>
    remove email <user> <email>
    remove tags <user> <tags>
    remove user <user>
    remove adress <user>
    find name <name>
    find tags <tags>
    find phone <phone>
    sort directory <path to folder>
    when birthday <name>
    birthdays within <days-must be integer>
    """,Colors.orange)
    return instruction


commands = {
    "help": pers_assistant_help,
    "add phone": add_phone,
    "add user": add_user,
    "show all": show_all,
    "add email": add_email,
    "add birthday": add_birthday,
    "add tags": add_tags,
    "add adress": add_adress,
    "change adress": change_adress,
    "change phone": change_phone,
    "change email": change_email,
    "change birthday": change_birthday,
    "remove phone": remove_phone,
    "remove email" :remove_email,
    "remove birthday": remove_birthday,
    "remove tags": remove_tags,
    "remove user": remove_user,
    "remove adress": remove_adress,
    "find name": find_name,
    "find tags": find_tags,
    "find phone": find_phone,
    "sort directory": sorting,
    "when birthday": when_birthday,
    "birthdays within": birthdays_within,
}

word_completer = WordCompleter([comm for comm in commands.keys()])

def parser(userInput:str):
    if len(userInput.split()) == 2:
        return commands[userInput.strip()], "None"

    for command in commands.keys():
        if userInput.startswith(str(command)):
            text = userInput.replace(command, "")
            command = commands[command]
            # print(text.strip().split())
            return command, text.strip()
        

def main():
    print(color(greeting,Colors.green))
    print(background(color("WRITE HELP TO SEE ALL COMMANDS                                      ",Colors.yellow),Colors.blue))
    print(background(color("WRITE 'exit', 'close' or 'bye' for close bot                        ",Colors.blue),Colors.yellow))
    ad.load_contacts_from_file()
    while True:
        # user_input = input(color("Enter your command: ",Colors.green)).strip().lower()
        user_input = prompt('Enter your command: ', completer=word_completer)
        if user_input in STOPLIST:
            exit = yes_no_dialog(
                    title='EXIT',
                    text='Do you want to close the bot?').run()
            if exit:
                print(color("Bye,see tou soon...",Colors.yellow))
                break
            else:
                continue

        elif user_input.startswith("help"):
            print(color(pers_assistant_help(),Colors.green))
            continue

        elif (len(user_input.split())) == 1:
            print(color("Please write full command", Colors.red))
            continue
        else:
            try:
                command, text = parser(user_input)
                print(command(text))
                ad.save_contacts_to_file()
            except KeyError:
                print(color("You enter wrong command", Colors.red))
            except Error:
                print(color("You enter wrong command Error", Colors.red))
            except TypeError:
                print(color("You enter wrong command TypeError", Colors.red))
            except IndexError:
                print(color("You enter wrong command or name", Colors.red))
            except ValueError:
                print(color("You enter wrong information", Colors.red))



if __name__ == "__main__":
    choice = input(color(f"SELECT WHICH BOT YOU WANT TO USE \nEnter 'notes' for use Notes\nEnter 'contacts' for use AdressBook\nEnter >>>  ",Colors.green))
    if choice == "notes":
        main_notes()
    elif choice == "contacts":
        main()
    else:
        user_error = input(color("You choose wrong name push enter to close the bot",Colors.red))


        


