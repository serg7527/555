import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Выполнение SQL запроса
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()

# Вывод результатов
for row in rows:
    print(row)

# Закрытие соединения
conn.close()