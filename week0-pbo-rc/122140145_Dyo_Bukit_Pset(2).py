jumlah_siswa = int(input("Masukan jumlah siswa : "))
nilai_siswa = {}

for i in range (jumlah_siswa):
    nama = input(f"Masukan nama siswa {i + 1} : ")
    nilai = int(input(f"Masukan nilai {nama} : "))
    
    nilai_siswa[nama] = nilai

print("\nNilai siswa : ")

for nama, nilai in nilai_siswa.items():
    print(f"{nama} : {nilai}")
