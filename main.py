import sqlite3

"""
# Formas de insertar datos
insert = "INSERT INTO customers VALUES ('albert', 'robby', 'robby@gmail.com')"
cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# Insert data in a table
cursor.execute(insert)
"""

# connect = sqlite3.connect(':memory')
connection = sqlite3.connect('customer.db')

# Create a cursor
cursor = connection.cursor()
cursor_2 = connection.cursor()

# Create user table information

# user_table = "CREATE TABLE usuario (nombre text, apellido text)"
# cursor.execute(user_table)

title = 'base de datos sqlite3 python'
print(f"{'=' * 10} {title.upper()} {'=' * 10} \n")


# Conseguir datos de inicio de sesion.
def login_req():
	username = ''

	print(f"Iniciar sesion en SQLITE PYTHON \n")
	get_username = input(f"Nombre de usuario: ")

	if get_username != '':
		username = get_username.strip()

		return username

	else:
		return username


def add_data():
	default = ''

	confirm_res = ['y', 's']
	request = input(f"Te gustaia registrar clientes si (s): ")

	def user_confirm(request, confirm):
		default = ''

		if request.strip().lower() in confirm:

			question = input(f"Introduce cantidad de clientes: ")

			try:
				if question != '':
					number = int(question)

					return number
				else:
					return default
			except:
				print(f"La cantidad {question}, no es valido. Intenta otra vez")
				return default
		else:
			return default

	user_confirm = user_confirm(request, confirm_res)

	if user_confirm:
		number_customer = user_confirm
		data = []
		
		i = 0
		while i < number_customer:

			name = input(f"\nNombre del cliente: ")
			last_name = input(f"Apellido del cliente: ")
			email = input(f"Correo del cliente: ")

			if name != '' and last_name != '' and email != '':
				data.append([])
				data[i].append(name)
				data[i].append(last_name)
				data[i].append(email)

			i += 1

		return data
	else:
		return default


# Registrar nuevos usuarios.
def user_register():
	default = ''
	user_default = 1
	user_data = []

	i = 0
	while i < user_default:
		name = input(f"Nombre de usuario: ") 
		lastname = input(f"Apellido de usuario: ")

		if name != '' and lastname != '':
			user_data.append([])
			user_data[i].append(name)
			user_data[i].append(lastname)

		i += 1

	if user_data:
		user_reg = []
		for user in user_data:
			user_reg.append(tuple(user))

		return user_reg

	else:
		return default

# clientes = cursor.execute("SELECT rowid, * FROM customers")
usuarios = cursor_2.execute("SELECT * FROM usuario")

# print('vista 1:', usuarios)
# print(cursor.fetchone()[0])
# print(cursor.fetchmany(2))
# print(cursor.fetchall())
# print(f"vista 2: {clientes}")

# Peticion de inicio de sesion.
username = login_req()


def user_login(username, clientes):
	default = ''
	user_res = ['y', 's']

	# User have an accout.
	if username:
		for user in clientes:
			
			if username in user:

				if username == user[1]:

					print(f"Hola {username}, bienvenido a tu cuenta")
					customers = add_data()
					return customers
				
				else:
					pass
			else:
				pass
		print(f"Hola {username}, no tienes una cuenta")
	else:
		return default

	# User not have an account.
	if username:
		user_req = input(f"Te gustaria registrar en Python App si (s): ")

		if user_req.strip().lower() in user_res:
			register = user_register()

			if register:
				cursor_2.executemany("INSERT INTO usuario VALUES (?, ?)", register)
			else:
				pass
			# if register == '':
			# 	print('Datos de registros vacio:', register)
		else:
			pass
			# print(f"No se puede registrar usuario")
	else:
		pass

	return default

# Agregar mas clientes por el usuario.
customers = user_login(username, clientes)


def add_customer(customers):
	default = ''
	many_customers = []

	if customers:
		for customer in customers:
			many_customers.append(tuple(customer))

		return many_customers
	else:
		pass	

	return default

many_customers = add_customer(customers)

# Fetchall method
# print(cursor.fetchall())

# for item in user_items:
# 	print(f"usuario: {item}")

# Commit our command
connection.commit()
# Close our connection
connection.close()
