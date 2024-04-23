import sqlite3

database = sqlite3.connect('ahahaha.db')
a = database.cursor()
a.execute('''CREATE TABLE IF NOT EXISTS countries
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)''')

countries_data = [
    ('Russia',),
    ('Germany',),
    ('Italy',)
]
a.executemany('INSERT INTO countries (title) VALUES (?)', countries_data)

a.execute('''CREATE TABLE IF NOT EXISTS cities
             (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL,
             area REAL DEFAULT 0, country_id INTEGER,
             FOREIGN KEY (country_id) REFERENCES countries(id))''')

cities_data = [
    ('Bishkek', 128, 1),
    ('Berlin', 89, 2),
    ('Beijing', 16414, 3),
    ('Osh', 182, 1),
    ('Moscow', 755, 2),
    ('Tokio', 6340, 3),
    ('Chupapimunyanya', 310, 2)
]
a.executemany('INSERT INTO cities (title, area, country_id) VALUES (?,?,?)', cities_data)

a.execute('''CREATE TABLE IF NOT EXISTS students
             (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL,
             last_name TEXT NOT NULL, city_id INTEGER,
             FOREIGN KEY (city_id) REFERENCES cities(id))''')

studentdata = [
    ("Андрей", "Соколов", 1),
    ("Гей", "Голубой", 3),
    ("Вова", "Путин", 4),
    ("Иосиф", "Сталин", 5),
    ("Гений","Негений", 1),
    ("Джозеф", "Байден", 3),
    ("Джотаро", "Куджо", 2),
    ("Омар", "Бредли", 3),
    ("Алексей", "Навальный", 4),
    ("Олаф", "Шольц", 1),
    ("Ырка", "Иванов", 4),
    ("Айсулуу","Тыныбекова", 7)
]
a.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?,?,?)', studentdata)
database.commit()

def display():
    database = sqlite3.connect('ahahaha.db')
    a = database.cursor()

    a.execute('SELECT id, title FROM cities')
    cities = a.fetchall()
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}. {city[1]}")
    city_id = int(input("Введите id города: "))
    a.execute('''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                 FROM students
                 INNER JOIN cities ON students.city_id = cities.id
                 INNER JOIN countries ON cities.country_id = countries.id
                 WHERE cities.id = ?''', (city_id,))
    students = a.fetchall()
    print("\nУченики в выбранном городе:")
    for student in students:
        print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")

    database.close()

display()
