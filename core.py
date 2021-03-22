import sqlite3


def show_all():

	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("SELECT rowid, * FROM usuario")

	customers = cursor.fetchall()

	for customer in customers:
		print(customer)

	connection.commit()
	connection.close()

def add_one(first, last):

	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("INSERT INTO usuario VALUES (?, ?)", (first, last))

	connection.commit()
	connection.close()

def add_many(user):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.executemany("INSERT INTO usuario VALUES (?, ?)", (user))

	connection.commit()
	connection.close()

def delete_one(id):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("DELETE from usuario WHERE rowid=(?)", id)

	connection.commit()
	connection.close()

# Apellido with where
def apellido(apellido):
	connection = sqlite3.connect('customer.db')
	cursor = connection.cursor()

	cursor.execute("SELECT rowid, * FROM usuario WHERE apellido=(?)", (apellido,))
	
	customers = cursor.fetchall()

	for customer in customers:
		print(customer)

	connection.commit()
	connection.close()

# cursor.execute("UPDATE customers SET first_name='felipe' WHERE rowid=13")
# cursor.execute("DELETE from customers WHERE rowid=13")

# cursor.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'c%' OR rowid=10")
# cursor.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
# cursor.execute("SELECT rowid, * FROM customers LIMIT 3")

# cursor.execute("DROP TABLE customers")
# connection.commit()


# customer_2 = cursor.fetchall()

# print(customer)
# print(customer_2)
