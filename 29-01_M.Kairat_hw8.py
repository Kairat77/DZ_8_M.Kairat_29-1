import sqlite3


conn = sqlite3.connect('sample.db')
conn.execute('''CREATE TABLE countries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL);''')


conn.execute("INSERT INTO countries(title) VALUES('USA'), ('Russia'), ('China')")


conn.execute('''CREATE TABLE cities
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  title TEXT NOT NULL, 
                  area REAL DEFAULT 0, 
                  country_id INTEGER REFERENCES countries(id));''')


conn.execute("INSERT INTO cities(title, area, country_id) VALUES('New York', 468.9, 1), ('Moscow', 2511, 2), ('Beijing', 16410.54, 3), ('Tokyo', 2191.90, 4), ('Mumbai', 603.4, 5), ('Sao Paulo', 1522.986, 6), ('Istanbul', 1839.77, 7)")


conn.execute('''CREATE TABLE employees 
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 first_name TEXT NOT NULL, 
                 last_name TEXT NOT NULL, 
                 city_id INTEGER REFERENCES cities(id));''')


conn.execute("INSERT INTO employees(first_name, last_name, city_id) VALUES('John', 'Smith', 1), ('Anna', 'Lee', 2), ('Ivan', 'Ivanov', 3), ('Yun', 'Chen', 4), ('Ravi', 'Kumar', 5), ('Carlos', 'Silva', 6), ('Ali', 'Kaya', 7), ('Maria', 'Garcia', 1), ('Bob', 'Jones', 2), ('Yuri', 'Petrov', 3), ('Xin', 'Wang', 4), ('Sonia', 'Singh', 5), ('Pedro', 'Santos', 6), ('Ahmet', 'Aslan', 7), ('Olga', 'Ivanova', 1)")


cursor = conn.execute('SELECT id, title FROM cities')
cities = cursor.fetchall()

print("Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
for city in cities:
    print(f"{city[0]}. {city[1]}")

city_id = int(input())

if city_id == 0:
    exit(0)


cursor = conn.execute(f'SELECT employees.first_name, employees.last_name, countries.title, cities.title FROM employees JOIN cities ON employees.city_id = cities.id JOIN countries ON cities.country_id = countries.id WHERE cities.id = {city_id}')
employees = cursor.fetchall()

for employee in employees:
    print(f"Имя: {employee[0]}, Фамилия: {employee[1]}, Страна: {employee[2]}, Город: {employee[3]}")

conn.close()
