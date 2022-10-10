print("    ")
#   adj meg egy szót és egy betűt
szoveg = input(str("Adj meg egy szót: "))
betu = input(str("Adj meg egy betűt: "))

#  ha a megadott betű nincs a megadott szövegben, írd ki majd lépj ki
if betu not in szoveg:
     print("A megadott betű , ami :", betu, ", nincs a beírt szóban!")
     exit()

#  ha a megadott szövegben NINCS benne a megadott betű
if betu in szoveg:
  print("A megadott", betu, "betű benne van a beírt szóban!")


#   cseréljük ki a megadott karaktert mosolyra
print("-----------------------------------------------")
print("A beírt szó, a karaktercsere után:")
print(szoveg.replace(betu, ":)"))
print("_______________________________________________")
