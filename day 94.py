# Pangkat 

bilangan = int(input("Masukkan Bilangan : "))
pangkat = int(input("Masukkan Pangkat : "))

hasil  = bilangan

for i in range(pangkat):
    hasil *=  bilangan
    
print(f"hasil dari {bilangan} dipangkat {pangkat} adalah {hasil}")