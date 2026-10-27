actividades = ["Create Purchase Order", "Approve Purchase Order", "Change Price",
               "Approve Purchase Order", "Receive Goods", "Receive Invoice",
               "Receive Invoice", "Pay Invoice"]

def contar(actividades):
    conteo = {}
    for a in actividades:
        conteo[a] = conteo.get(a,0) + 1

    return conteo

print(contar(actividades))