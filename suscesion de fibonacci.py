sucesion = [0, 1]
for i in sucesion:
    nuevo_elemento = sucesion[-1]+sucesion[-2]
    sucesion.append(nuevo_elemento)
    if i == 610:
        break
print (f"la sucecion de fibonacci hasta el numero 1597 contiene los numeros {sucesion}")