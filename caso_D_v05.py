from reticulado import Reticulado
from barra import Barra

def caso_D():
	
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
	H = 20.0   * m
	Z = 100.0 * m
	O = 10.0  * m #Origen
	A_X = 115.0 * m   
	A_Z = 70.0  * m
	
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
	ret.agregar_nodo(O + 26.25           , B/2 ,  Z + H  )
	ret.agregar_nodo(A_X - 55.0 +26.25   , B/2 ,  Z + H  )
	ret.agregar_nodo(A_X + 27.5          , B/2 ,  Z + H  )
	ret.agregar_nodo(A_X + 55.0 +27.5    , B/2 ,  Z + H  )
	
	#Nodos de apoyo
	ret.agregar_nodo(A_X  , 0 ,  A_Z  )	#140 - 131

	#Barras
	R_t = [[0.06, 0.003], [0.1, 0.005], [0.05, 0.003], [0.12, 0.006], [0.09, 0.005], [0.14, 0.007], [0.12, 0.006], [0.16, 0.008], [0.14, 0.007], [0.17, 0.009], [0.16, 0.008], [0.18, 0.009], [0.17, 0.009], [0.2, 0.01], [0.18, 0.01], [0.21, 0.011], [0.2, 0.01], [0.22, 0.012], [0.21, 0.011], [0.24, 0.012], [0.04, 0.003], [0.12, 0.006], [0.09, 0.005], [0.09, 0.005], [0.12, 0.006], [0.06, 0.003], [0.14, 0.007], [0.04, 0.003], [0.16, 0.008], [0.08, 0.005], [0.18, 0.009], [0.11, 0.006], [0.19, 0.01], [0.14, 0.007], [0.2, 0.01], [0.16, 0.008], [0.22, 0.011], [0.17, 0.009], [0.23, 0.012], [0.18, 0.009], [0.44, 0.023], [0.94, 0.047], [0.27, 0.014], [0.31, 0.016], [0.24, 0.012], [0.28, 0.014], [0.2, 0.01], [0.24, 0.012], [0.13, 0.007], [0.19, 0.01], [0.06, 0.003], [0.14, 0.007], [0.15, 0.008], [0.05, 0.003], [0.2, 0.011], [0.15, 0.008], [0.24, 0.013], [0.2, 0.011], [0.28, 0.015], [0.25, 0.013], [0.32, 0.016], [0.28, 0.015], [0.34, 0.017], [0.32, 0.016], [0.32, 0.016], [0.3, 0.015], [0.28, 0.015], [0.26, 0.013], [0.24, 0.013], [0.22, 0.011], [0.2, 0.011], [0.18, 0.009], [0.14, 0.008], [0.1, 0.006], [0.04, 0.002], [0.1, 0.005], [0.14, 0.007], [0.17, 0.009], [0.2, 0.01], [0.22, 0.011], [0.24, 0.012], [0.26, 0.013], [0.28, 0.014], [0.3, 0.015], [0.3, 0.016], [0.33, 0.017], [0.25, 0.013], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.002], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.17, 0.009], [0.18, 0.009], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.002], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.25, 0.013], [0.17, 0.009], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.002], [0.05, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.05, 0.003], [0.1, 0.005], [0.26, 0.013], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.89, 0.045], [0.86, 0.044], [0.47, 0.024], [0.05, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.02, 0.002], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.05, 0.003], [0.43, 0.022], [0.96, 0.048], [0.86, 0.043], [0.06, 0.003], [0.05, 0.003], [0.04, 0.002], [0.06, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.04, 0.003], [0.38, 0.019], [0.42, 0.022], [0.05, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.002], [0.04, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.05, 0.003], [0.38, 0.019], [0.38, 0.019], [0.05, 0.003], [0.04, 0.003], [0.04, 0.003], [0.04, 0.002], [0.04, 0.002], [0.04, 0.003], [0.04, 0.002], [0.04, 0.003], [0.04, 0.003], [0.05, 0.003], [0.42, 0.022], [1.0, 0.05], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.02, 0.001], [0.07, 0.004], [0.07, 0.004], [0.07, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.07, 0.004], [0.06, 0.003], [0.32, 0.017], [0.32, 0.017], [0.06, 0.003], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.08, 0.004], [0.07, 0.004], [0.02, 0.001], [0.06, 0.004], [0.06, 0.004], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.003], [0.06, 0.004], [1.0, 0.05], [0.09, 0.005], [0.05, 0.003], [0.08, 0.005], [0.04, 0.003], [0.08, 0.005], [0.04, 0.002], [0.08, 0.005], [0.04, 0.002], [0.08, 0.004], [0.04, 0.002], [0.08, 0.004], [0.04, 0.002], [0.08, 0.005], [0.03, 0.002], [0.08, 0.005], [0.04, 0.002], [0.08, 0.005], [0.04, 0.002], [0.09, 0.005], [0.05, 0.003], [0.06, 0.003], [0.1, 0.005], [0.06, 0.003], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.004], [0.1, 0.005], [0.06, 0.003], [0.1, 0.005], [0.03, 0.002], [0.08, 0.004], [0.52, 0.027], [0.53, 0.027], [0.09, 0.005], [0.12, 0.006], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.003], [0.14, 0.007], [0.06, 0.004], [0.14, 0.007], [0.06, 0.004], [0.13, 0.007], [0.13, 0.007], [0.07, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.006], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.12, 0.007], [0.08, 0.004], [0.13, 0.007], [0.07, 0.004], [0.42, 0.021]]
	props = [200*GPa, 7600*kg/m**3, 420*MPa]	

	barra_n = 0

	#Laterales e = 5 m
	for i in range(x):
		ret.agregar_barra(Barra(i,i+1,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		ret.agregar_barra(Barra(x+i+1,x+i+2,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	
	#Piramides	
	for i in range(11):
		ret.agregar_barra(Barra(i,88,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	for i in range(44,55):
		ret.agregar_barra(Barra(i,88,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		
	for i in range(10,22):
		ret.agregar_barra(Barra(i,89,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	for i in range(54,66):
		ret.agregar_barra(Barra(i,89,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		
	for i in range(21,33):
		ret.agregar_barra(Barra(i,90,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	for i in range(64,77):
		ret.agregar_barra(Barra(i,90,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		
	for i in range(32,44):
		ret.agregar_barra(Barra(i,91,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	for i in range(76,88):
		ret.agregar_barra(Barra(i,91,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		
	#Union Laterales
	for i in range (x+1):
		ret.agregar_barra(Barra(i,x+1+i,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	
	#X
	for i in range(x):	
		ret.agregar_barra(Barra(i,x+i+2,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
		ret.agregar_barra(Barra(x+i+1,i+1,R_t[barra_n][0],R_t[barra_n][1],*props))
		barra_n += 1
	
	#Apoyo
	ret.agregar_barra(Barra(92,21,R_t[barra_n][0],R_t[barra_n][1],*props))		
	
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
	
	ret.agregar_restriccion(92  ,  0, 0)
	ret.agregar_restriccion(92  ,  1, 0)
	ret.agregar_restriccion(92  ,  2, 0)
    
	
	return ret

