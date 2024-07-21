import sqlite3
conexion = sqlite3.connect('stocks_database.db')
cursor = conexion.cursor()

cursor.execute("SELECT * FROM stocks")

valores = cursor.fetchall()


for valor in valores:
    print(valor)
    
conexion.commit()
conexion.close()