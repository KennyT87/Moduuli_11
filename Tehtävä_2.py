class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.nykyinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nykyinen_nopeus = 0
        else:
            self.nykyinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        matkan_muutos = self.nykyinen_nopeus * tunnit
        self.kuljettu_matka += matkan_muutos


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko


sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

# Kiihdytys
sahkoauto.kiihdyta(120)
polttomoottoriauto.kiihdyta(130)

# Ajetaan kolme tuntia
sahkoauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton matkamittarilukema: {sahkoauto.kuljettu_matka} km")
print(f"Polttomoottoriauton matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")
