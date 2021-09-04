# Gigino e i numeri primi
# By Achille
# Rel. 0.1

numero = input("Dai a Gigino il tuo numero (n>1): ")

for i in range(2, numero-1):
    if numero % i == 0:
        print("Ti do una nota.")
        quit()
print("Il cinghiale si muove di moto rettilineo uniforme.")
