from math import sqrt

import sys
sys.setrecursionlimit(100000)


def primoAnt(n):
	#print("es primo ", n, esPrimo(n))
	#if not(esPrimo(n)):
	#	primoAnt(n-1)
	#return n
	if esPrimo(n):
		
		return n
	else:
		return primoAnt(n-1)



def esPrimo(numero):
	rango = range(2,numero)
	if numero == 1:
		return False
	elif numero == 2:
		return True
	else:
		for elementos in rango:

				if numero % elementos == 0:
					return  False
					break
				else:
					if elementos == numero - 1:
						return True

def esImpar(num):
	if num == 2:
		return False
	if num %2== 0:
		return False
	else:
		return True

def esEntero(num):
	if num == int(num):
		return True
	else:
		return False


def verificaCompuesto(n, p):
	if not(esPrimo(n)) and esImpar(n) and 2<=p:
		c = n-p
		if esEntero(sqrt(c/2)):
			print (n, p, sqrt(c/2))
			return True
		else:
			if p<2:
				return False
			return verificaCompuesto(n,primoAnt(p-2))
			
def buscaMin():
	bandera=True
	num= 9

	while bandera:
		if esPrimo(num):
			num=num+2
		if verificaCompuesto(num, primoAnt(num)):
			num= num+2
		else:
			bandera= False
			return num
	#print num
	return num

def listaImpares(numero):
	lista = []
	for x in range(9,numero,2):
		if esPrimo(x) == False:
			lista.append(x)
	return lista

def primos(numero):
	lista2 =[]
	lista= [ lista2.append(x)   for x in range(1,numero) if esPrimo(x)==True]	
	return lista2


#print buscaMin()
for i in listaImpares(5778):
	print verificaCompuesto(i, primoAnt(i))

#print verificaCompuesto(95, primoAnt(95))