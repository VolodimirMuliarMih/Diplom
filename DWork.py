# DiplomPRJ
import pandas as pd
import openpyxl


df = pd.DataFrame(columns=(['surname', 'name','patronymic', 'birt_year', 'birth_month', 'birth_day','live', 'death_year', 'death_month', 'death_day']))
writer = pd.ExcelWriter('base_main.xlsx',engine='openpyxl' )
df.to_excel(writer, 'marks')
writer.save()
writer.close()

def import_to_main_base_csv(path_file):
    """функция импортирует из файла csv данные и записывает из в excel файл"""
    data_csv = pd.read_csv(path_file)
    writer = pd.ExcelWriter('base_main.xlsx', engine='openpyxl')
    data_csv.to_excel(writer,'marks')
    writer.save()
    writer.close()

def import_to_main_base_json(path_file):
    """функция импортирует из файла json данные и записывает из в excel файл"""
    data_json = pd.read_json(path_file)
    writer = pd.ExcelWriter('base_main.xlsx', engine='openpyxl')
    data_json.to_excel(writer,'marks')
    writer.save()
    writer.close()

def import_to_main_base_excel(path_file):
    """функция импортирует из файла excel данные и записывает из в excel файл"""
    data_json = pd.read_excel(path_file)
    writer = pd.ExcelWriter('base_main.xlsx', engine='openpyxl')
    data_json.to_excel(writer,'marks')
    writer.save()
    writer.close()

def enter_data_from_keyboard (list):
        df = pd.DataFrame(list, index=[0])
        print(df)
        excel_data_df = pd.read_excel('base_main.xlsx', index_col=0, sheet_name='marks')
        df_unit = pd.concat([excel_data_df , df], ignore_index=True)
        print(df_unit)
        writer = pd.ExcelWriter('base_main.xlsx', mode="a",  engine='openpyxl',if_sheet_exists='overlay')
        df_unit.to_excel(writer, 'marks')
        writer.save()
        writer.close()



class Person_edit():
    # surname = None
    # name = None
    # patronymic = None
    # birt_year = int()
    # birth_month = int()
    # birth_day = int()
    # live = True
    # death_year = int()
    # death_month = int()
    # death_day = int()
    def __init__(self,surname, name,patronymic,birt_year,birth_month,birth_day,live,death_year,death_month,death_day):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birt_year = int(birt_year)
        self.birth_month = int(birth_month)
        self.birth_day = int(birth_day)
        self.live= live
        self.death_year = int(death_year)
        self.death_month = int(death_month)
        self.death_day = int(death_day)
        if self.live == 1:
            self.death_year = None
            self.death_month = None
            self.death_day = None

"""Создание базы данных в excel"""
while True:
    base_ask = int(input("Вас приветствует программа обработки персональных данных\n Для ввода данных нажмите 1 \n Для обработки персональных данных нажмите 2\n"))
    if base_ask == 1:
        while True:
            choice = int(input(
                "Приветствую Вас в программе обработки персональных данных. Для продолжения выберите пункт из меню \n Ввод или загрузка данных нажмите 1 \n Ввод вручную нажмите 2\n"))
            if choice == 1:
                while True:
                    """выполнение загрузки данных вызов функци вып загрузку данных"""
                    type_import_file = int(input("Введите тип файла загрузжаеиого в базу \n 1 файл scv \n 2 файл join\n 3 файл excel\n"))
                    if type_import_file == 1: # тип csv
                        path_file_scv = input("Введите путь к данному файлу \n")
                        import_to_main_base_csv(path_file_scv)
                    if type_import_file == 2: # тип json
                        path_file_json = input("Введите путь к данному файлу \n")
                        import_to_main_base_json(path_file_json)
                    if type_import_file == 3: # тип excel
                        path_file_excel = input("Введите путь к данному файлу \n")
                        import_to_main_base_excel(path_file_excel)
                    else:
                        print("Вы не сделали выбор, повторите")
                    continue
            if choice == 2:
                """выполнение ввода данных руками"""
                while True:
                    live_inp = input("Человек на данный момент жив? \n Веедите Да или Нет\n")
                    if live_inp == "Нет":
                        death_year_inp = int(input("Введите год смерти \n"))
                        death_month_inp = int(input("Введите месяц кончины \n"))
                        death_day_inp = int(input("Введите день в какой приставился\n"))
                    if live_inp == "Да":
                        death_year_inp = None
                        death_month_inp = None
                        death_day_inp = None
                    else:
                        print("Повторите ввод, вы ввели некоректный ответ \n")
                        continue
                    surname_inp = input(("Введите фамилию \n").title())
                    name_inp = input(("Введите имя \n").title())
                    patronymic_inp = input(("Введите отчество \n").title())
                    birt_year_inp = int(input("Введите год рождения \n"))
                    birth_month_inp = int(input("Введите месяц рождения \n"))
                    birth_day_inp = int(input("Введите день рождения \n"))
                    n = ({"surname": surname_inp, "name": name_inp, "patronymic": patronymic_inp,"birt_year": birt_year_inp,"birth_month": birth_month_inp,"birth_day": birth_day_inp, "live": live_inp, "death_year":death_year_inp,"death_month":death_month_inp,"death_day":death_day_inp})
                    enter_data_from_keyboard(n)
                    ask = input('Продолжить ввод данных\n')
                    if ask =="Да":
                        continue
                    if ask == "Нет":
                        break
    if base_ask == 2:
        print("dfgfdg")
    else:
        print("Сделайте свой выбор, вы ввели некоректное значение")
