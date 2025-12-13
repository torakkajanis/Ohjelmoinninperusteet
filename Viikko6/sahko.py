# Copyright (c) 2025 Oma Nimi
# License: MIT

import locale
from datetime import datetime, date

locale.setlocale(locale.LC_TIME, "fi_FI.UTF-8")

def muunna_sahko(sahko: list) -> list:
    """Muuntaa datatyypit"""
    muutettusahko = []

    aika = datetime.fromisoformat(sahko[0])
    paiva = aika.date()
    muutettusahko.append(paiva)
    kello = aika.time()
    muutettusahko.append(kello)

    kulutus = float(sahko[1].replace(",", "."))
    muutettusahko.append(kulutus)

    tuotanto = float(sahko[2].replace(",", "."))
    muutettusahko.append(tuotanto)

    lampotila = float(sahko[3].replace(",", "."))
    muutettusahko.append(lampotila)

    return muutettusahko

def hae_sahko(sahkotiedosto: str) -> list:
    """Lukee datan"""
    sahko = []
    sahko.append([""])
    #tähän varmaan pitää lisätä jotain????
    with open(sahkotiedosto, "r", encoding="utf-8") as f:
        next(f)
        for sahkorivi in f:
            sahkorivi = sahkorivi.strip()
            sahkorivitiedot = sahkorivi.split(';')
            sahko.append(muunna_sahko(sahkorivitiedot))
    return sahko

def tarjoa_valikkoa() -> list: 
    """Antaa valinnan mahdollisuuden käyttäjälle"""
    sahko = hae_sahko("2025.csv")
    raportti = ""
    while True:
        print(f"Valitse raporttityyppi:\n1) Päiväkohtaiset yhteenvedot\n2) Kuukausikohtaiset yhteenvedot\n3) Vuoden 2025 kokonaisyhteenveto\n4) Lopeta ohjelma")
        valinta = input("Syötä valintasi numerona: ").strip()
        if valinta == "1":
            raportti = laske_paivakohtainen(sahko)
        elif valinta == "2":
            raportti = laske_kuukausikohtainen(sahko)
        elif valinta == "3":
            raportti = laske_vuosi_2025 (sahko)
        elif valinta == "4":
            print(f"Kiitos käytöstä, ohjelma päättyy")
            break
        else: 
            print ("Tuntematon valinta, yritä uudelleen. Anna valintasi kokonaislukuna välillä 1-4.")
        print(f"Mitä haluat seuraavaksi?\n1) Kirjoita raportti tiedostoon raportti.txt\n2) Luo uusi raportti\n3) Lopeta")
        valintaB = input("Syötä valintasi numerona: ").strip()
        if valintaB == "1":
            kirjoita_raportti(raportti)
        elif valintaB == "2":
            continue
        elif valintaB == "3":
            print(f"Kiitos käytöstä, ohjelma päättyy.")
            break
        else: 
            print ("Tuntematon valinta. Yritä uudelleen.")

    
def laske_paivakohtainen(sahko: list) -> str: 
    """laskee ja printtaa päiväkohtaisen yhteenvedon koko tiedostosta"""
    print(f"Valitse ajanjakso. Kirjoita valintasi muodossa pp.kk.vvvv")
    alkupaiva = input("Anna aloituspäivämäärä: ")
    loppupaiva = input("Anna lopetuspäivämäärä: ")
    raportti = ""
    print_str = (f"Päivän a) sähkönkulutus b) sähköntuotanto c) keskilämpötila")
    raportti += (f"{print_str}\n")
    print(print_str)
    alkupvm = datetime.strptime(alkupaiva, "%d.%m.%Y").date()
    loppupvm = datetime.strptime(loppupaiva, "%d.%m.%Y").date()
    edellinenPaiva = False
    summakulutus = 0
    summatuotanto = 0
    lampotila = 0
    lampotilamaara = 0
    for rivi in sahko [1:]:
        if rivi[0] >= alkupvm and rivi[0] <= loppupvm:
            pvm = rivi[0].strftime("%d.%m.%Y")
            if edellinenPaiva == False or edellinenPaiva == pvm:
                summakulutus += rivi[2]
                summatuotanto += rivi[3]
                lampotila += rivi[4] 
                lampotilamaara += 1
            else: 
                summakulutus = f"{summakulutus:.2f}" 
                summakulutus = summakulutus.replace(".", ",")
                summatuotanto = f"{summatuotanto:.2f}" 
                summatuotanto = summatuotanto.replace(".", ",")
                keskilampotila = lampotila/lampotilamaara
                keskilampotila = f"{keskilampotila:.2f}"
                keskilampotila = keskilampotila.replace(".", ",")
                print_str = (f"{pvm} : a) {summakulutus} b) {summatuotanto} c) {keskilampotila}")
                raportti += (f"{print_str}\n")
                print(print_str)
                summakulutus = 0
                summakulutus += rivi[2]
                summatuotanto = 0
                summatuotanto += rivi[3]
                lampotila = 0
                lampotila += rivi[4] 
                lampotilamaara = 0
                lampotilamaara += 1
            edellinenPaiva = pvm
    summakulutus = f"{summakulutus:.2f}" 
    summakulutus = summakulutus.replace(".", ",")
    summatuotanto = f"{summatuotanto:.2f}" 
    summatuotanto = summatuotanto.replace(".", ",")
    keskilampotila = lampotila/lampotilamaara
    keskilampotila = f"{keskilampotila:.2f}"
    keskilampotila = keskilampotila.replace(".", ",")
    print_str = (f"{pvm} : a) {summakulutus} b) {summatuotanto} c) {keskilampotila}")
    raportti += (f"{print_str}\n")
    print(print_str)

    return raportti

def laske_kuukausikohtainen(sahko: list) -> str: 
    """laskee ja printtaa kk-kohtaisen yhteenvedon koko tiedostosta"""
    print(f"Valitse kuukausi. Anna kuukauden numero, esim. tammikuu = 1, helmikuu = 2, jne.")
    valittukuukausi = input("Anna kuukauden numero (1-12): ")
    raportti = ""
    print_str = (f"Kuukauden a) sähkönkulutus b) sähköntuotanto c) keskilämpötila")
    raportti += (f"{print_str}\n")
    print(print_str)
    edellinenKuukausi = False
    summakulutus = 0
    summatuotanto = 0
    lampotila = 0
    lampotilamaara = 0
    for rivi in sahko [1:]:
        if int(rivi[0].strftime("%m")) == int(valittukuukausi):
            kk = rivi[0].strftime("%bkuu %Y")
            if edellinenKuukausi == False or edellinenKuukausi == kk:
                summakulutus += rivi[2]
                summatuotanto += rivi[3]
                lampotila += rivi[4] 
                lampotilamaara += 1
            else: 
                summakulutus = f"{summakulutus:.2f}" 
                summakulutus = summakulutus.replace(".", ",")
                summatuotanto = f"{summatuotanto:.2f}" 
                summatuotanto = summatuotanto.replace(".", ",")
                keskilampotila = lampotila/lampotilamaara
                keskilampotila = f"{keskilampotila:.2f}"
                keskilampotila = keskilampotila.replace(".", ",")
                kk2 = datetime.strptime(edellinenKuukausi, "%bkuu %Y").strftime("%bkuu %Y")
                print_str = (f"{kk2} : a) {summakulutus} b) {summatuotanto} c) {keskilampotila}")
                raportti += (f"{print_str}\n")
                print(print_str)
                summakulutus = 0
                summakulutus += rivi[2]
                summatuotanto = 0
                summatuotanto += rivi[3]
                lampotila = 0
                lampotila += rivi[4] 
                lampotilamaara = 0
                lampotilamaara += 1
            edellinenKuukausi = kk
            kk = datetime.strptime(edellinenKuukausi, "%bkuu %Y").strftime("%bkuu %Y")
    summakulutus = f"{summakulutus:.2f}" 
    summakulutus = summakulutus.replace(".", ",")
    summatuotanto = f"{summatuotanto:.2f}" 
    summatuotanto = summatuotanto.replace(".", ",")
    keskilampotila = lampotila/lampotilamaara
    keskilampotila = f"{keskilampotila:.2f}"
    keskilampotila = keskilampotila.replace(".", ",")
    print_str = (f"{kk} : a) {summakulutus} b) {summatuotanto} c) {keskilampotila}")
    raportti += (f"{print_str}\n")
    print(print_str)

    return raportti

def laske_vuosi_2025(sahko: list) -> str: 
    """laskee koko vuoden 2025 yhteenvedon"""
    raportti = ""
    print_str = (f"Vuoden 2025 sähkönkulutus sähköntuotanto ja keskilämpötila")
    raportti += (f"{print_str}\n")
    print(print_str)
    summakulutus = 0
    summatuotanto = 0
    lampotila = 0
    lampotilamaara = 0
    for rivi in sahko [1:]:
        summakulutus += rivi[2]
        summatuotanto += rivi[3]
        lampotila += rivi[4] 
        lampotilamaara += 1
    summakulutus = f"{summakulutus:.2f}" 
    summakulutus = summakulutus.replace(".", ",")
    summatuotanto = f"{summatuotanto:.2f}" 
    summatuotanto = summatuotanto.replace(".", ",")
    keskilampotila = lampotila/lampotilamaara
    keskilampotila = f"{keskilampotila:.2f}"
    keskilampotila = keskilampotila.replace(".", ",")
    print_str = (f"{summakulutus}, {summatuotanto}, {keskilampotila}")
    raportti += (f"{print_str}\n")
    print(print_str)

    return raportti

def kirjoita_raportti (raportti: str): 
    with open("raportti.txt", "w", encoding="utf-8") as f:
         f.write(raportti)


def main():
    tarjoa_valikkoa()
        

if __name__ == "__main__":
    main()