importar numpy como np
importar matplotlib.pyplot como plt
desde mpi4py import  MPI


comm =  MPI . COMM_WORLD
rango = com.Get_rank ()


 función defx ( x ):
    
    fxi = np.sqrt (x) * np.sin (x)
    volver (fxi)

def  integrales ( a , b , Tramos ):
    h = (b - a) / tramos
    x = a
    suma = functionx (x)
    para i en  rango ( 0 , tramos -  1 , 1 ):
        x = x + h
        suma = suma +  2  * functionx (x)
    suma = suma + funciónx (b)
    área = h * (suma /  2 )
    área de     retorno
            

a =  1
b =  4
tramos =  10



print (integral (a, b, tramos))

 
para i en  rango ( 1 , tramos):
    
    
    print ( " tramos " , i, " area " , integral (a, b, i))
muestras = tramos +  1
xi = np.linspace (a, b, muestras)
fi = functionx (xi)


# Gráfica
# Referencia función contínua
xig = np.linspace (a, b, muestras *  10 )
fig = functionx (xig)
plt.plot (xig, fig)
# Trapecios
plt.fill_between (xi, 0 , fi, color  =  ' y ' )
plt.title ( ' Integral: Regla de Trapecios ' )
para i en  rango ( 0 , muestras, 1 ):
    plt.axvline (xi [i], color  =  ' w ' )
plt.plot (xi, fi, ' o ' ) # puntos muestra
plt.xlabel ( ' x ' )
plt.ylabel ( ' f (x) ' )
plt.show ()
plt.savefig ( " i.jpg " )

print ( ' tramos: ' , tramos)