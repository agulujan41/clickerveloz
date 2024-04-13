listaNombres = ["Agustin","Sebastian"]
listaNombres.append("Jhon")
listaNombres.append("Jose")
listaNombres.append("Francisco")
listaNombres.append("Elias")
listaNombres.append("Franco")
listaNombres.append("Daniel")
listaNombres.append("Roman")
print(listaNombres)
#Fernando
#in
if "Fernando" not in listaNombres:
    print("No está dentro de la lista")
else:
    print("Está adentro de la lista")
print("Tenemos",len(listaNombres),"elementos")
tamanio = len(listaNombres)

print("El primero de la lista",listaNombres[0])
print("En el medio de la lista esta",listaNombres[tamanio//2])
print("El ultimo de la lista",listaNombres[tamanio-1])

