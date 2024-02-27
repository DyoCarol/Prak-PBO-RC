tinggi = int(input("Masukan tinggi segitiga : "))

spasi = tinggi - 1
bintang = 1

for i in range (tinggi) : 
    print(f"{' ' * spasi} {'*' * bintang}")
    spasi -= 1
    bintang += 2
