# Maria Camila Guzman Bolaños
#Ventas U
def cuantoRecibe (usuario):
    descuento = 0
    if usuario == "estudiante":
        descuento = 50
    else:
        descuento == 20
    return descuento

def registrocmpra(items):
    listcompra = []  #ej: [[076,3,6000]]
    for i in range(3):
        datoscompra = input()
        listcompra.append(datoscompra)
    listcompra = [int(i) for i in listcompra]
    return listcompra

def sindescuento (lista, items):
    precio = []
    var = 0
    if items == 1:
        if lista[1]>1:
            var = lista[0][2] * lista[0][1]
            precio.append(var)
        else:
            precio.append(lista[2])
    if items < 1:
        for x in range (lista):
            if lista[x][1]>1:
                var = lista[0][2] * lista[0][1]
                precio.append(var)
    for z in precio:
        preciot = precio + precio 
    v = [int(h) for h in preciot]
    return v

def descuento(valordescuebto,preciosindes):
    var1 = valordescuebto / 100
    var2 = float(var1) * preciosindes
    var3 = preciosindes - var2
    return var3

def leerImp():
    datoscliente = []  #[identificacion,rol]
    for d in range(2):
        datos = input()
        datoscliente.append(datos)
    items = int(input("itemsa comprar"))
    recibe = cuantoRecibe(datoscliente[1])
    compra = registrocmpra(items)
    preciosindescuento = sindescuento(compra,items)
    preciodescuento = descuento(recibe,preciosindescuento)
    if items == 1:
        print("el"+ datos[1] + "con numero identidad:" + datos[0] + ", debe pagar:"
                   + preciodescuento + "por el producto" + compra[0])
    else:
        print("el"+ datos[1] + "con numero identidad:" + datos[0] + ", debe pagar:"+ preciodescuento)
leerImp()


    