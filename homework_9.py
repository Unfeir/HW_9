import pathlib


directory = r"D:\study\GoIT\cours\python_core\module_9\homework_9\work_dir"
path = pathlib.Path(directory)

my_dict = {}

def input_error(func):
    """Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
       Цей декоратор відповідає за повернення користувачеві повідомлень виду:
       "Enter user name", "Give me name and phone please" і т.п. 
       Декоратор input_error обробляє вийнятки
       що виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві."""
       
    def wraper(*args):
        
        try:
            result = func(*args)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Wrong phone number" 
        except IndexError:
            return "Give me name and phone please"
        except:
            return "So,ething going wrong" 
        else:
            return result
        
    return wraper


def parser(text):
    if text:
        a = text.replace("good bye", "good_bye").replace("show all", "show_all")
        return a.split()[0], a.split()[1:] # формуємо кортеж із назви функції і аргументів для неї
    
              

@input_error
def hello(*args):
    """ відповідає у консоль "How can I help you?"""
    
    return "How can I help you?"

@input_error    
def good_bye(*args):
    ''' "good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".'''
    
    
    return "Good bye!"
    
@input_error
def add_func(args):
    """За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл."""
    name = args[0].capitalize()
    phone = int(args[1])
    my_dict[name] = phone
    return f"{name} was added" 


@input_error
def change_func(args):
    """За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл."""
    name = args[0].capitalize()
    phone = int(args[1])
    old_walue = my_dict[name]
    my_dict[name] = phone
    return f"{name}`s phone was changed from {old_walue} to {phone}"
    
       
@input_error
def phone_func(args):
    """За цією командою бот виводить у консоль номер телефону для зазначеного контакту. 
    Замість ... користувач вводить ім'я контакту, чий номер треба показати."""
    name = args[0].capitalize()
    value = my_dict[name]
    return f"{name}`s phone number is {value}"



@input_error
def show_all_func(*args):
    """За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль."""
    contacts = ""
    for k, v in my_dict.items():
        contacts += f"{k} - {v}\n"
    
    return contacts
        


def fun_name(fun):
    fun_dict = {
        "hello": hello,
        "good_bye": good_bye,
        "close": good_bye,
        "exit": good_bye,
        "add": add_func,
        "change": change_func,
        "phone": phone_func,
        "show_all": show_all_func    
    }
    
    return fun_dict.get(fun)


def main():
       
    go_on = True
    while go_on:
        user_input = input("Listen You: ").lower()
        fun, args = parser(user_input)
        call_fun = fun_name(fun)
        
        if call_fun:
            
            text = call_fun(args)
            print(text)
            if text == "Good bye!":
                go_on = False
            
        
        else:
            print("No such command, try: add, change, show all")
            continue
        
        


main()
