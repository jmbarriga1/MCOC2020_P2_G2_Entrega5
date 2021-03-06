from reticulado import Reticulado
from barra import Barra

def caso_L():
	
	# Unidades base
	m = 1.
	kg = 1.
	s = 1. 
	
	#Unidades derivadas
	N = kg*m/s**2
	cm = 0.01*m
	mm = 0.001*m
	KN = 1000*N
	Pa = N / m**2
	KPa = 1000*Pa
	MPa = 1000*KPa
	GPa = 1000*MPa
	
	#Parametros
	L = 5.0   * m
	B = 2.0   * m
	H = 5.0   * m
	Z = 100.0 * m
	O = 10.0  * m #Origen
	A_X = 115.0 * m   
	A_Z = 70.0  * m
	
	#Carga
	q = 400 * 9.8 * kg / m**2
	F1 = q*L*B/4
	F2 = q*L*B/2	
	
	#Inicializar modelo
	ret = Reticulado()

	#Nodos
	
	x = 43
	
	#Nodos Tablero
	for i in range(x+1):#47
		ret.agregar_nodo(O + i*L     , 0  ,  Z  )
	
	#Nodos en y = 2
	for i in range(x+1):#47
		ret.agregar_nodo(O + i*L     , B  ,  Z  )
		
	#Nodos arriba
	ret.agregar_nodo(O + 52.5   , B/2 ,  Z + H  )
	ret.agregar_nodo(A_X + 55.0   , B/2 ,  Z + H  )
	
	#Nodos de apoyo
	ret.agregar_nodo(A_X  , 0 ,  A_Z  )	#140 - 131

	#Barras
	R = 100.0 * cm
	t = 50.0  * mm		
	props = [R,t,200*GPa, 7600*kg/m**3, 420*MPa]	

	barra_n = 0

	#Laterales e = 5 m
	for i in range(x):
		ret.agregar_barra(Barra(i,i+1,*props))
		barra_n += 1
		ret.agregar_barra(Barra(x+i+1,x+i+2,*props))
		barra_n += 1
	
	#Piramides	
	for i in range(22):
		ret.agregar_barra(Barra(i,88,*props))
		barra_n += 1
		
	for i in range(44,66):
		ret.agregar_barra(Barra(i,88,*props))
		barra_n += 1
		
	for i in range(21,44):
		ret.agregar_barra(Barra(i,89,*props))
		barra_n += 1
		
	for i in range(65,88):
		ret.agregar_barra(Barra(i,89,*props))
		barra_n += 1
	
	#Union Laterales
	for i in range (x+1):
		ret.agregar_barra(Barra(i,x+1+i,*props))
		barra_n += 1
	
	#X
	for i in range(x):	
		ret.agregar_barra(Barra(i,x+i+2,*props))
		barra_n += 1
		ret.agregar_barra(Barra(x+i+1,i+1,*props))
		barra_n += 1
	
	#Apoyo
	ret.agregar_barra(Barra(90,21,*props))		
	
	#Nodo 0  y 4 fijos
	ret.agregar_restriccion(0  , 0, 0)
	ret.agregar_restriccion(0  , 1, 0)
	ret.agregar_restriccion(0  , 2, 0)
	ret.agregar_restriccion(x+1, 0, 0)
	ret.agregar_restriccion(x+1, 1, 0)
	ret.agregar_restriccion(x+1, 2, 0)

	# Nodos 3 y 7 libres en X
	ret.agregar_restriccion(x    ,  1, 0)
	ret.agregar_restriccion(x    ,  2, 0)
	ret.agregar_restriccion(2*x+1,  1, 0)
	ret.agregar_restriccion(2*x+1,  2, 0)
	
	ret.agregar_restriccion(90  ,  0, 0)
	ret.agregar_restriccion(90  ,  1, 0)
	ret.agregar_restriccion(90  ,  2, 0)

        
	#Fuerzas en nodos
	for i in range((x+1)*2):
		if i == 0 or i == x or i == x+1 or i == 2*x+1:
			ret.agregar_fuerza(i , 2, -F1)
		else:
			ret.agregar_fuerza(i , 2, -F2)
        
	return ret

