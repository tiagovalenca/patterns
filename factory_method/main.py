class animals():
   class galinha():
       info = "Isso é uma galinha"
   class cachorro():
       info = "Isso é um cachorro"
   class pato():
       info = "isso é um pato"
 def fabricar_animais(tipo):
   if tipo == "galinha":
       return animals.galinha
   elif tipo == "cachorro":
       return animals.cachorro
   elif tipo == "pato":
       return animals.pato
lista =[]
while True:
   info = input("Qual animal você quer na sua fazenda?")
   animal = fabricar_animais(info)
   lista.append(animal.info)
   print(lista)
