import pprint
import csv


def show_hierarchy() -> None:

    """
    This function creates a dict with a hierarchy of a teams and prints it
    """

    with open('Corp_Summary.csv', 'r') as data:
        data = csv.DictReader(data, delimiter=';')
        departaments = {} 
        for person in data:
            if person['Департамент'] in departaments:
                if person['Отдел'] not in departaments[person['Департамент']]:
                    departaments[person['Департамент']].append(person['Отдел'])
            else:
                departaments[person['Департамент']] = [person['Отдел']]
        pprint.pprint(departaments)

def create_report() -> dict():

    """
    This function creates dict with report about departaments
    """

    with open('Corp_Summary.csv', 'r') as data:
        data = csv.DictReader(data, delimiter=';')
        departaments = {}

        for person in data:
            if person['Департамент'] in departaments:
                departaments[person['Департамент']]['Численность'] += 1
                departaments[person['Департамент']]['Зарплатный фонд'] += int(person['Оклад'])
                departaments[person['Департамент']]['Средняя зарплата'] = departaments[person['Департамент']]['Зарплатный фонд'] / departaments[person['Департамент']]['Численность']
                if int(person['Оклад']) < departaments[person['Департамент']]['Минимальная зарплата']:
                    departaments[person['Департамент']]['Минимальная зарплата'] = int(person['Оклад'])
                if int(person['Оклад']) > departaments[person['Департамент']]['Максимальная зарплата']:
                    departaments[person['Департамент']]['Максимальная зарплата'] = int(person['Оклад'])
                departaments[person['Департамент']]['Вилка'] = departaments[person['Департамент']]['Максимальная зарплата'] - departaments[person['Департамент']]['Минимальная зарплата']
            if person['Департамент'] not in departaments:
                departaments[person['Департамент']] = {}
                departaments[person['Департамент']]['Численность'] = 1
                departaments[person['Департамент']]['Минимальная зарплата'] = int(person['Оклад'])
                departaments[person['Департамент']]['Максимальная зарплата'] = int(person['Оклад'])
                departaments[person['Департамент']]['Вилка'] = 0
                departaments[person['Департамент']]['Средняя зарплата'] = int(person['Оклад'])
                departaments[person['Департамент']]['Зарплатный фонд'] = int(person['Оклад'])



        return departaments

def print_repot() -> None:

    """
    This function prints dict with report
    """

    pprint.pprint(create_report())


def create_report_csv() -> None:

    """
    This function creates .csv file with information about departaments
    pretty_csv - list for creating pretty looking .csv
    """
    with open('report.csv', 'w') as data:
        dict_report = create_report()
        pretty_csv = []
        for departament in dict_report:
            current_departament = {}
            current_departament['Департамент'] = departament
            for chararacteristic in dict_report[departament]:
                if chararacteristic != 'Зарплатный фонд':
                    current_departament[chararacteristic] = dict_report[departament][chararacteristic]
            pretty_csv.append(current_departament)
        keys = pretty_csv[0].keys()
        report = csv.DictWriter(data, keys)

        
        report.writeheader()
        report.writerows(pretty_csv)


def menu() -> None:
    
    """
    This function prints a munu.
    User can choose to see hierarchy of departaments by pressing '1'
    Or see a report about departaments by pressing '2'
    Or create a .csv file by pressing '3'
    """

    print('To see hierarchy of departaments press "1"\n'
            'To see a report about departaments press "2"\n'
            'To crate a .csv file with a repot press "3"\n')
    answer = ''
    while answer not in ['1', '2', '3']:
        print('Please enter the command:\n')
        answer = input()
    
    if answer == '1':
        show_hierarchy()
    elif answer == '2':
        print_repot()
    elif answer == '3':
        create_report_csv()
        

if __name__ == '__main__':
    menu()
