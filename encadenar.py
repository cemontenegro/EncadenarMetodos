class Usuario:
	nombre_banco = "Primer Dojo Nacional"
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.balance_cuenta = 0
	# agregando el método de depósito
	def hacer_deposito(self, amount):	# toma un argumento que es el monto del depósito
		self.balance_cuenta += amount
		return self
	def retirar_deposito(self, amount):
		self.balance_cuenta -= amount
		return self
	def mostrar_balance_usuario(self):
		self.balance_cuenta
		return self
	def transferir_dinero(self, destino, amount):
		self.balance_cuenta -= amount
		destino.balance_cuenta += amount
		return self

#def transfer_dinero(self, other_user, amount):

usuario1 = Usuario("Adrien", "guido@python.com")
usuario2 = Usuario("Mr. Nibbles", "monty@python.com")
usuario3 = Usuario("Benny Bob", "monty@python.com")

usuario1.hacer_deposito(100).hacer_deposito(150).hacer_deposito(50).retirar_deposito(80)
print((usuario1.name),', Balance: ', (usuario1.balance_cuenta))

usuario2.hacer_deposito(500).hacer_deposito(100).retirar_deposito(100).retirar_deposito(200)
print((usuario2.name),', Balance: ', (usuario2.balance_cuenta))


usuario3.hacer_deposito(50).retirar_deposito(100).retirar_deposito(200).retirar_deposito(100)
print((usuario3.name),', Balance: ', (usuario3.balance_cuenta))


usuario1.transferir_dinero(usuario3, 30)
print((usuario1.name),', Balance: ', (usuario1.balance_cuenta))
print((usuario3.name),', Balance: ', (usuario3.balance_cuenta))