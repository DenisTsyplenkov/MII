from pathlib import Path

import matplotlib.pyplot as plt
import numpy
import pandas
import csv
import random

male_last_name = ['Азизов', 'Александров', 'Андреев', 'Баграмян', 'Булавочкин', 'Васильев',
                  'Глушков', 'Дементьев', 'Денисов', 'Ефимов', 'Иванов', 'Кадеев',
                  'Лапин', 'Макаров', 'Новиков', 'Орлов', 'Петров', 'Рандин', 'Самборский',
                  'Табаков', 'Федоров', 'Харьков', 'Цветов', 'Цыпленков', 'Шамшев', 'Юренков']

male_first_name = ['Юрий', 'Михаил', 'Олег', 'Марат', 'Иван'
                                                      'Руслан', 'Вячеслав', 'Алексей', 'Денис', 'Павел',
                   'Виталий', 'Руслан', 'Анатолий', 'Андрей', 'Глеб',
                   'Александр', 'Сергей' 'Дмитрий', 'Семён', 'Игорь']

male_patronymic = ['Юрьевич', 'Алексеевич', 'Михайлович', 'Глебович', 'Сергеевич',
                   'Аркадьевич', 'Владимирович', 'Борисович', 'Вадимович', 'Валентинович',
                   'Викторович', 'Васильевич', 'Данилович', 'Петрович', 'Дмитриевич',
                   'Евгеньевич', 'Георгиевич', 'Геннадиевич', 'Николаевич', 'Иванович']

female_last_name = ['Алексеева', 'Аристова', 'Баладнина', 'Бенько', 'Ваганова', 'Вершинина',
                    'Глухова', 'Гришенкова', 'Давыдова', 'Деева', 'Денисова', 'Емельянова',
                    'Ерофеева', 'Жукова', 'Захарова', 'Измайлова', 'Кадырова', 'Капустина', 'Михеева',
                    'Макарова', 'Манусова', 'Новикова', 'Обрезкова', 'Овсянникова', 'Сабурова', 'Цыпленкова']

female_first_name = ['Екатерина', 'Марина', 'Арина', 'Светлана', 'Ольга', 'Надежда',
                     'Юлия', 'Ева', 'Лилит', 'Алсу', 'Дарья', 'Алиса',
                     'Алиса', 'Галина', 'Аксиния', 'Гузель', 'Наталья', 'Адалат',
                     'Елена', 'Татьяна', 'Валентина', 'Ирина', ' Татьяна']

female_patronymic = ['Львовна', 'Николаевна', 'Иванова', 'Олеговна', 'Владимировна',
                     'Раисовна', 'Витальевна', 'Андреевна', 'Евгеньевна', 'Валерьевна',
                     'Виктровна', 'Алексеевна', 'Камилевна', 'Петровна', 'Григорьевна',
                     'Сергеевна', 'Денисовна', 'Ярославовна', 'Шамильевна', 'Николаевна']

gender = ['Мужской', 'Женский']

subdivisions = ['Отдел монтажа электронных компонентов', 'Администрация', 'Отдел разработки ПО',
                'Лаборатория', 'Отдел фрезерования', 'Отдел сборки']
job_titles = ['Куратор', 'Стажер', 'Инженер', 'Разработчик']


def generate_data(path: Path) -> None:
    employees_len: int = random.randint(1000, 1999)
    with open(path, 'w', encoding='utf-16', newline='') as file:
        titles = [
            'Табельный номер',
            'Фамилия И.О.',
            'Пол',
            'Год рождения',
            'Год начала работы в компании',
            'Подразделение',
            'Должность',
            'Оклад',
            'Количество выполненных проектов'
        ]
        file_writer = csv.DictWriter(file, fieldnames=titles)
        file_writer.writeheader()

        for i in range(1, employees_len + 1):
            gen: str = random.choice(gender)
            if gen == 'Мужской':
                full_name = random.choice(male_last_name) + ' ' + random.choice(male_first_name) + ' ' + random.choice(
                    male_patronymic)
            else:
                full_name = random.choice(female_last_name) + ' ' + random.choice(female_first_name) + ' ' + \
                            random.choice(female_patronymic)

            year_of_birth: int = random.randint(1978, 2001)
            year_of_start_working: int = random.randint(2019, 2022)
            subdivision: str = random.choice(subdivisions)
            job_title: str = random.choice(job_titles)
            pay: int = random.randrange(22000, 55000, 500)
            project_amounts: int = random.randint(1, 4)
            file_writer.writerow({
                'Табельный номер': i,
                'Фамилия И.О.': full_name,
                'Пол': gen,
                'Год рождения': year_of_birth,
                'Год начала работы в компании': year_of_start_working,
                'Подразделение': subdivision,
                'Должность': job_title,
                'Оклад': pay,
                'Количество выполненных проектов': project_amounts
            })


def statistic_numpy(path: Path) -> None:
    with open(path, 'r', encoding='utf-16') as file:
        file_reader = csv.DictReader(file)
        gen = []
        years_of_birth: list[int] = []
        years_of_start_working: list[int] = []
        sub: list[str] = []
        pay = []
        project_amounts = []

        for line in file_reader:
            project_amounts.append(int(line['Количество выполненных проектов']))
            pay.append(int(line['Оклад']))
            years_of_birth.append(int(line['Год рождения']))
            years_of_start_working.append(int(line['Год начала работы в компании']))
            sub.append(line['Подразделение'])
            gen.append(line['Пол'])

        work_experience: list[int] = [2022 - years_of_start_working[i]
                                      for i in range(len(years_of_birth))]

        print('Numpy статистика:')
        print('')

        print('Сотрудники:')
        print(f'Количество сотрудников: {numpy.count_nonzero(work_experience)}')
        print(f'Женщины: {numpy.count_nonzero(numpy.array(gen) == "Женский")}')
        print(f'Мужчины: {numpy.count_nonzero(numpy.array(gen) == "Мужской")}')
        print('')

        print('Опыт работы:')
        print('')
        print(f'Максимальный стаж (лет): {numpy.max(work_experience)}')
        print(f'Минимальный стаж (лет): {numpy.min(work_experience)}')
        print(f'Средний стаж (лет): {round(numpy.average(work_experience), 2)}')
        print('')

        print('Отделы:')
        print(f'Количество отделов: {len(numpy.unique(subdivisions))}')
        print(f'Отдел монтажа электронных компонентов: {numpy.count_nonzero(numpy.array(sub) == "Отдел монтажа электронных компонентов")} сотрудников')
        print(f'Администрация: {numpy.count_nonzero(numpy.array(sub) == "Администрация")} сотрудников')
        print(f'Отдел разработки ПО: {numpy.count_nonzero(numpy.array(sub) == "Отдел разработки ПО")} сотрудников')
        print(f'Лаборатория: {numpy.count_nonzero(numpy.array(sub) == "Лаборатория")} сотрудников')
        print(f'Отдел фрезерования: {numpy.count_nonzero(numpy.array(sub) == "Отдел фрезерования")} сотрудников')
        print(f'Отдел сборки: {numpy.count_nonzero(numpy.array(sub) == "Отдел сборки")} сотрудников')
        print('')

        print('Бухгалтерия:')
        print(f'Максимальная зарплата (руб.): {numpy.max(pay)}')
        print(f'Минимальная зарплата (руб.): {numpy.min(pay)}')
        print(f'Средняя зарплата (руб.): {round(numpy.average(pay), 2)}')
        print(f'Сумма зарплат (руб.): {numpy.sum(pay)}')
        print(f'Среднее арифметическое значение зарплаты (руб.): {round(numpy.mean(pay), 2)}')
        print(f'Медианное значение зарплаты (руб.): {numpy.median(pay)}')
        print(f'Дисперсия зарплаты (руб.): {round(numpy.var(pay), 2)}')
        print(f'Стандартное отклонение зарплаты (руб.): {round(numpy.std(pay), 2)}')
        print('')

        print('Проекты:')
        print(f'Проектов всего: {numpy.sum(project_amounts)}')
        print(f'Минимальное количество проектов у сотрудника: {numpy.min(project_amounts)}')
        print(f'Максимальное количество проектов у сотрудника : {numpy.max(project_amounts)}')
        print(f'Среднее количество проектов на сотрудника: {round(numpy.average(project_amounts), 2)}')
        print('')


def statistic_pandas(path: Path) -> None:
    company = pandas.read_csv(path, encoding='utf-16')
    print('Pandas статистика:')
    print('')
    print(f'Количество сотрудников (чел.): {company["Табельный номер"].count()}')
    print(f'{company["Пол"].value_counts().to_frame()}')
    print('')

    print('Опыт работы:')
    print('')
    print(f'Максимальный стаж: {2022 - company["Год начала работы в компании"].min()} лет')
    print(f'Минимальный стаж: {2022 - company["Год начала работы в компании"].max()} лет')
    print(f'Средний стаж: {round(2022- company["Год начала работы в компании"].mean(), 2)} лет')
    print('')

    print('Отделы')
    print('')
    print(f'Количество подразделений: {company["Подразделение"].value_counts().sum()}')
    print(f'{company["Подразделение"].value_counts().to_frame()}')
    print('')

    print('Бухгалтерия:')
    print('')
    print(f'Максимальная зарплата (руб.): {company["Оклад"].max()}')
    print(f'Минимальная зарплата (руб.): {company["Оклад"].min()}')
    print(f'Средняя зарплата (руб.): {round(company["Оклад"].mean(), 2)}')
    print(f'Сумма зарплат (руб.): {company["Оклад"].sum()}')
    print(f'Среднее арифметическое значение зарплаты (руб.): {round(company["Оклад"].mean(), 2)}')
    print(f'Медианное значение зарплаты (руб.): {company["Оклад"].median()}')
    print(f'Дисперсия зарплаты (руб.): {round(company["Оклад"].var(), 2)}')
    print(f'Стандартное отклонение зарплаты (руб.): {round(company["Оклад"].std(), 2)}')
    print('')

    print('Проекты')
    print('')

    print(f'Проектов всего: {company["Количество выполненных проектов"].sum()}')
    print(f'Минимальное количество проектов у сотрудника : {company["Количество выполненных проектов"].min()}')
    print(f'Максимальное количество проектов у сотрудника: {company["Количество выполненных проектов"].max()}')
    print(f'Среднее количество проектов на сотрудника: {round(company["Количество выполненных проектов"].mean(), 2)}')


def graphics(path: Path) -> None:
    company = pandas.read_csv(path, encoding='utf-16')
    labels = [rf'Женский {round(company["Пол"].value_counts()["Женский"]/company["Табельный номер"].count()*100, 2)}%',
              rf'Мужской {round(company["Пол"].value_counts()["Мужской"]/company["Табельный номер"].count()*100, 2)}%']
    plt.pie([company["Пол"].value_counts()["Женский"], company["Пол"].value_counts()["Мужской"]])
    plt.legend(labels)
    plt.show()

    company["Должность"].value_counts().plot(rot=0)
    plt.show()

    company["Подразделение"].value_counts().plot.bar(rot=0)
    plt.show()


file_path = Path(Path.cwd(), 'company.csv')
generate_data(file_path)
statistic_numpy(file_path)
statistic_pandas(file_path)
graphics(file_path)