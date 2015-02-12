def verificar(numero):
	if numero <2: return False
	if numero == 2: return True
	for elementos in range(3,int(numero**0.5)+1,2):
		if numero % elementos == 0:
			return  False
	return True

def loscompuestos():
	return [x for x in range(3,100000,2) if verificar(x)== False]

def conjetura():
	lista = [] 
	compuestos = loscompuestos()
	for x in compuestos:
		p = 1
		bandera = False
		while 2*(p**2) < x: 
			lista.append(x - 2*(p**2))
			p += 1
		for y in lista :
			if (verificar(y)== False): 
				bandera = False
			else:
				bandera = True 
				break
		lista =[]	
		if(bandera == False):
			return x

print conjetura()









	



	




