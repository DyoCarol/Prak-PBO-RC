import random

class GolonganDarah:
    def __init__(self, tipe):
        self.tipe = tipe.upper()

    def __str__(self):
        return self.tipe

class OrangTua:
    def __init__(self, golongan_darah):
        self.golongan_darah = GolonganDarah(golongan_darah)
        self.alel = self._get_alel(self.golongan_darah)

    def _get_alel(self, golongan_darah):
        if golongan_darah == 'A':
            return ['A', 'O']
        elif golongan_darah == 'B':
            return ['B', 'O']
        elif golongan_darah == 'AB':
            return ['A', 'B']
        elif golongan_darah == 'O':
            return ['O', 'O']
        else:
            raise ValueError("")

class Anak:
    def __init__(self, ayah, ibu):
        self.ayah = ayah
        self.ibu = ibu
        self.golongan_darah = self._tentukan_golongan_darah_anak()

    def _tentukan_golongan_darah_anak(self):
        alel_anak = [random.choice(parent.alel) for parent in [self.ayah, self.ibu]]

        if alel_anak.count('A') == 2 or ('A' in alel_anak and 'B' in alel_anak):
            return 'AB'
        elif alel_anak.count('B') == 2:
            return 'B'
        elif alel_anak.count('A') == 1:
            return 'A'
        else:
            return 'O'

def main():
    try:
        golongan_darah_ayah = input("Enter the Father's allele: ").upper()
        golongan_darah_ibu = input("Enter the Mother's allele: ").upper()

        ayah = OrangTua(golongan_darah_ayah)
        ibu = OrangTua(golongan_darah_ibu)
        anak = Anak(ayah, ibu)

        print(f"Child's allele: {anak.golongan_darah}")
    except ValueError as e:
        print(f"Error {e}")

if __name__ == "__main__":
    main()
