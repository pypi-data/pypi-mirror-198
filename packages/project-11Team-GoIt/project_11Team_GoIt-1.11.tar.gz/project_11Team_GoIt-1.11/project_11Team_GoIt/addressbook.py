import pickle
import re
from collections import UserDict
from datetime import datetime

from colorit import *

colorit.init_colorit()


class Error(Exception):  #власне виключення
     pass
    #  def __str__(self) -> str:
    #       return "\n \nSomething went wrong\n Try again!\n"



class Field:
    
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return self._value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):   #клас для створення поля name

    def __str__(self) -> str:
        self._value : str
        return self._value.title()
    

class Phone(Field):   #клас для створення поля phone
    
    @staticmethod   #метод який не звязаний з класом
    def verify(number):  #перевирка номеру телефона
        number = re.sub(r"[\-\(\)\+\ a-zA-Zа-яА-я]", "", number)
        try:
            if len(number) == 12:
                number = "+" + number
            elif len(number) == 10:
                number = "+38" + number
            elif len(number) == 9:
                number = "+380" + number
            else:
                number = False
                raise Error
        except Error:
            print(color("\nYou enter wrong number\n Try again!\n", Colors.red))
        
        if number:
            return number
        else:
            return "-"


    def __init__(self, value) -> None:
        self._value = Phone.verify(value)

    @Field.value.setter
    def value(self, value):
        self._value =Phone.verify(value)

    def __repr__(self) -> str:
        return self._value
    
    def __str__(self) -> str:
        return self._value

class Birthday:

    @staticmethod   #метод який не звязаний з класом
    def verify_date(birth_date: str):
        try:
            birthdate = re.findall(r"\d{4}\.\d{2}\.\d{2}", birth_date)
            if bool(birthdate) == False:
                raise Error
        except Error:
            print(color("\nYou enter wrong date.\nUse this format - YYYY.MM.DD \nTry again!\n", Colors.red))

        if birthdate:
            return birthdate[0]
        else:
            return "-"

    def __init__(self, birthday) -> None:
        self.__birthday = self.verify_date(birthday)

    @property
    def birthday(self):
        return self.__birthday
    
    @birthday.setter
    def birthday(self,birthday):
        self.__birthday = self.verify_date(birthday)

    def __repr__(self) -> str:
        return self.__birthday
    
    def __str__(self) -> str:
        return self.__birthday
    

class Email:

    @staticmethod   #метод який не звязаний з класом
    def verificate_email(text:str):
        email_re = re.findall(r"\w+3\@{1}\w+\.\w+", text)
        email = "".join(email_re)
        try:
            if bool(email) == True:
                return email
            else:
                raise Error
        except Error:
            print(color("\nYou enter wrong email\n Try again!\n", Colors.red))
            return "-"


    def __init__(self, email) -> None:
        self.__email = self.verificate_email(email)

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email = self.verificate_email(email)

    def __repr__(self) -> str:
        return self.__email
    
    def __str__(self) -> str:
        return self.__email


class Adress:

    def __init__(self, adress) -> None:
        self.__adress = adress

    @property
    def adress(self):
        return self.__adress
    
    @adress.setter
    def adress(self,adress):
        self.__adress = self.adress

    def __repr__(self) -> str:
        return self.__adress
    
    def __str__(self) -> str:
        return self.__adress
    

class Tags:

    def __init__(self, tags) -> None:
        self.__tags = tags

    @property
    def tags(self):
        return self.__tags
    
    @tags.setter
    def tags(self,tags):
        self.__tags = self.tags

    def __repr__(self) -> str:
        return self.__tags
    
    def __str__(self) -> str:
        return self.__tags



class Record:   #клас для запису инфи
    def __init__ (self, name : Name, phone: Phone = None, birthday: Birthday = None, email: Email = None, adress: Adress = None, tags :Tags = None):
        self.name = name
        self.phone = phone
        self.birthday = birthday
        self.email = email
        self.adress = adress
        self.tags = []
        self.phones = []
        if phone:
            self.phones.append(phone)

    def get_birthday(self):
        if self.birthday is None:
            return None
        else:
            return str(self.birthday)

    def get_tags(self):
        return self.tags
    
    def get_phone(self):
        return self.phones

    def add_phone(self, phone: Phone):  # додати телефон
        self.phones.append(phone)

    def add_birthday(self, birthday: Birthday):  # додати телефон
        if self.birthday is None:
            self.birthday = birthday
        else:
            print(color("This user already have birthday date",Colors.red))
    
    def add_email(self, email:Email):  # додати телефон
        if self.email is None:
            self.email = email
        else:
            print(color("This user already have email",Colors.red))

    def add_tags(self, tags:Tags):  # додати телефон
        self.tags.append(tags)

    def add_adress(self, adress):
        if self.adress is None:
            self.adress = adress
        else:
            print(color("This user already have adress",Colors.red))

    def change_adress(self,adress):
        # adress = Adress(adress)
        if self.adress is None:
            print(color("This user doesnt have adress", Colors.red))
        else:
            self.adress = adress

    def change_email(self,email):
        # email = Email(email)
        if self.email is None:
            print(color("This user doesnt have adress", Colors.red))
        else:
            self.email = email

    def change_birthday(self,birthday):
        # birthday = Birthday(birthday)
        if self.birthday is None:
            print(color("This user doesnt have birthday", Colors.red))
        else:
            self.birthday = birthday

    def remove_email(self):
        if self.email is None:
            print(color("This user doesnt have email",Colors.red))
        else:
            self.email = None

    def remove_birthday(self):
        if self.birthday is None:
            print(color("This user doesnt have birthday date",Colors.red))
        else:
            self.birthday = None

    def remove_phone(self, phone):  # видалити телефон
        # phone = Phone(phone)
        for ph in self.phones:
            if str(ph) == str(phone):
                self.phones.remove(ph)
            else:
                print(color("This user doesnt have this phone",Colors.red))

    def remove_tags(self, tags):
        for tag in self.tags:
            if str(tag) == str(tags):
                self.tags.remove(tag)
            else:
                print(color("This user doesnt have tags which you want to remove",Colors.red))


    def remove_adress(self):
        if self.adress is None:
            print(color("This user doesnt have adress",Colors.red))
        else:
            self.adress = None


    def change_phone(self, oldphone, newphone): # зминити телефон користувача 
        oldphone = Phone(oldphone)
        newphone = Phone(newphone)
        for phone in self.phones:
            if str(phone) == str(oldphone):
                self.phones.remove(phone)
                self.phones.append(newphone)
            else:
                print(color("This user doesnt have oldphone which you want to change",Colors.red))

    def days_to_birthday(self):   #функция яка показуе скильки днив до наступного др
                                  # потрибно допрацювати
        try:
                
            if str(self.birthday) == None:
                return None
            
            current = datetime.now().date()
            current : datetime
            user_date = datetime.strptime(str(self.birthday), "%Y.%m.%d")
            user_date: datetime
            user_date = user_date.replace(year=current.year).date()

            if user_date < current:
                user_date = user_date.replace(year= current.year +1)
                res = user_date - current

                return color(f"{res.days} days before next birthday", Colors.purple)
            else:
                res = user_date - current
                return color(f"{res.days} days before next birthday", Colors.purple)
        except ValueError:
            return (color("You set wrong date or user doesnt have birthday date\nTry again set new date in format YYYY.MM.DD", Colors.red))
        
    def __repr__(self) -> str:
        return f"\nPhone - {[str(i) for i in self.phones]},\nBirthday - {self.birthday},\nEmail - {self.email},\nAdress - {self.adress},\nTags - {self.tags}"

separator = "___________________________________________________________" 

class AdressBook(UserDict): #адресна книга

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def generator(self): # генератор з yield
        for name, info in self.data.items():
            print(color(separator,Colors.purple))
            yield color(f"Name - {name.title()} : ",Colors.blue)+ color(f"{info}",Colors.yellow)
            print(color(separator,Colors.purple))

    
    def iterator(self, value):  # функция яка показуе килькисть контактив яку введе користувач
        value = value
        gen = self.generator()
        try:
            if value > len(self.data):
                raise Error
        except:
            print(color("You set big value, list has less users. Try again.\n", Colors.red))

        while value > 0:
            try:
                print(next(gen))
                value -= 1
            except StopIteration:
                print(color(f"Try enter value less on {value}. Dict has {len(self.data)} contacts",Colors.purple))
                return ""
        return color("Thats all!",Colors.orange)
    
    
    # def save(self):     #функция збереження даних адресбук у csv файл
    #     if len(self.data) == 0:
    #         print(color("Your AddressBook is empty",Colors.red))
        
    #     with open("savebook.csv", "w", newline="") as file:
    #         fields = ["Name", "Info"]
    #         writer = csv.DictWriter(file, fields)
    #         writer.writeheader()
    #         for name, info in self.data.items():
    #             name :str
    #             writer.writerow({"Name": name.title(), "Info": str(info)})
    #         return color("Succesfull save your AddressBook",Colors.green)



    # def load(self):  # функция яка завантажуе контакти з збереженого csv файлу, якшо такого нема буде про це повидомлено
    #     try: 
    #         with open("savebook.csv", "r", newline="") as file:
    #             reader = csv.DictReader(file)
    #             for row in reader:
    #                 saved = {row["Name"]: row["Info"]}
    #                 self.data.update(saved)

    #             print(color("\nSuccesfull load saved AddressBook", Colors.purple))
    #     except:
    #         print(color("\nDont exist file with saving contacts",Colors.blue))
    #     return ""
        
    def find_tags(self,tags):
        res = ""
        finder = False
        tags = tags[0]
        for user, info in self.data.items():
            for tag in info.get_tags():
                if str(tag) == str(tags):
                    finder = True
                    print(color(f"\nFind tags\nUser - {user.title()}{info}",Colors.purple))
        return color("Found users",Colors.green) if finder == True else color("Dont find any user",Colors.green)



    def find_name(self, name: str):     #функция для пошуку по имя або телефону
        res= ""
        fail = color("Finder not find any matches in AddressBook",Colors.red)
        for user, info in self.data.items():
            if str(user) == name:
                res += color(f"Find similar contacts:\n\nUser - {user.title()}{info}\n",Colors.purple)
        return res if len(res)>0 else fail

    def find_phone(self,phone):
        finder = False
        phone = Phone(phone)
        for user, info in self.data.items():
            for ph in info.get_phone():
                if str(ph) == str(phone):
                    finder = True
                    print(color(f"\nFind phone\nUser - {user.title()}{info}",Colors.purple))
        return color("Found users",Colors.green) if finder == True else color("Dont find any user",Colors.green)

    
    def save_contacts_to_file(self):
        with open('contacts.pickle', 'wb') as file:
            pickle.dump(self.data, file)

    def load_contacts_from_file(self):
        try:
            with open('contacts.pickle', 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            pass
                    




ad = AdressBook()


# ПЕРЕВИРКА СКРИПТА
# name = Name("Dima")
# phone = Phone("0993796625")
# birth = Birthday("2001.08.12")
# rec = Record(name, phone, birth)
# ad = AdressBook()
# ad.add_record(rec)
# #=============================================================================
# name1 = Name("Benderovec")
# phone1 = Phone("0993790447")
# birth1 = Birthday("2001.08.12")
# rec1 = Record(name1, phone1, birth1)
# ad.add_record(rec1)
# #=============================================================================
# # print(rec.days_to_birthday())
# #=============================================================================
# name2 = Name("Diana")
# phone2 = Phone("099797484")
# birth2 = Birthday("2003.04.01")
# rec2 = Record(name2, phone2, birth2)
# #============================================================================
# ad.add_record(rec2)
# print(ad.data)

# print(ad.iterator(6))
# print(ad.find("test"))






# НА ВСЕ ЩО НИЖЧЕ НЕ ЗВЕРТАТИ УВАГИ!!!!!!!!!!!!!!!!!

# result = button_dialog(
#     title='Button dialog example',
#     text='Do you want to confirm?',
#     buttons=[
#         ('Yes', True),
#         ('No', False),
#         ('Maybe...', None)
#     ],
# ).run()

# print(result)

# html_completer = WordCompleter(['add user', 'add phone', 'add email', 'add adress'])
# text = prompt('Enter command: ', completer=html_completer)
# print('You said: %s' % text)

# my_completer = WordCompleter(['add phone', 'add user', 'add email', 'add adress'])

# text = prompt('Enter HTML: ', completer=my_completer, complete_while_typing=True,)
# print(text.split())

# for i in my_completer:
#     print(i)


"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

html_completer = WordCompleter(['<html>', '<body>', '<head>', '<title>'])
text = prompt('Enter HTML: ', completer=html_completer)
print('You said: %s' % text)


from prompt_toolkit.shortcuts import yes_no_dialog

result = yes_no_dialog(
    title='Yes/No dialog example',
    text='Do you want to confirm?').run()




"""