# Copyright (c) 2025 Emmi Räisälä
# License: MIT

import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "fi_FI.UTF-8")

def muunna_sahko(sahko: list) -> list:
    """Muuntaa datatyypit"""
    muutettusahko = []

    aika = datetime.fromisoformat(sahko[0])
    paiva = aika.date()
    muutettusahko.append(paiva)
    kello = aika.time()
    muutettusahko.append(kello)

    kulutusv1 = int(sahko[1])
    muutettusahko.append(kulutusv1)

    kulutusv2 = int(sahko[2])
    muutettusahko.append(kulutusv2)

    kulutusv3 = int(sahko[3])
    muutettusahko.append(kulutusv3)

    tuotantov1 = int(sahko[4])
    muutettusahko.append(tuotantov1)

    tuotantov2 = int(sahko[5])
    muutettusahko.append(tuotantov2)

    tuotantov3 = int(sahko[6])
    muutettusahko.append(tuotantov3)

    return muutettusahko

def hae_sahko(sahkotiedosto: str) -> list:
    """Lukee datan"""
    sahko = []
    sahko.append(["Päivä", "Kello", "Kulutus v1", "Kulutus v2", "Kulutus v3", "Tuotanto v1", "Tuotanto v2", "Tuotanto v3"])
    with open(sahkotiedosto, "r", encoding="utf-8") as f:
        next(f)
        for sahkorivi in f:
            sahkorivi = sahkorivi.strip()
            sahkorivitiedot = sahkorivi.split(';')
            sahko.append(muunna_sahko(sahkorivitiedot))
    return sahko

def print_kokovko(sahko: list, vkonro: int, f):
    """printtaa viikon tiedot"""
    
    f.write ("\n")
    
    f.write(f"Viikon {vkonro} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n")

    f.write ("\n")

    f.write("Päivä\tPäivämäärä\t\tKulutus (kWh)\t\t\t\tTuotanto (kWh)\t\t\t\n")
    f.write("\t\t(pv.kk.vvvv)\tv1\t\tv2\t\tv3\t\t\tv1\t\tv2\t\tv3\t\t\n")
    f.write("---------------------------------------------------------------------------\n")
    edellinenPaiva = False
    summaKulutusV1 = 0
    summaKulutusV2 = 0
    summaKulutusV3 = 0
    summaTuotantoV1 = 0
    summaTuotantoV2 = 0
    summaTuotantoV3 = 0
    for rivi in sahko [1:]:
        suomalainenpvm = rivi[0].strftime("%d.%m.%Y")
        if edellinenPaiva == False or edellinenPaiva == suomalainenpvm:
            summaKulutusV1 += rivi[2]/1000
            summaKulutusV2 += rivi[3]/1000
            summaKulutusV3 += rivi[4]/1000
            summaTuotantoV1 += rivi[5]/1000
            summaTuotantoV2 += rivi[6]/1000
            summaTuotantoV3 += rivi[7]/1000
        else:
            summaKulutusV1 = f"{summaKulutusV1:.2f}" 
            summaKulutusV1 = summaKulutusV1.replace(".", ",")
            summaKulutusV2 = f"{summaKulutusV2:.2f}" 
            summaKulutusV2 = summaKulutusV2.replace(".", ",")
            summaKulutusV3 = f"{summaKulutusV3:.2f}" 
            summaKulutusV3 = summaKulutusV3.replace(".", ",")
            summaTuotantoV1 = f"{summaTuotantoV1:.2f}" 
            summaTuotantoV1 = summaTuotantoV1.replace(".", ",")
            summaTuotantoV2 = f"{summaTuotantoV2:.2f}" 
            summaTuotantoV2 = summaTuotantoV2.replace(".", ",")
            summaTuotantoV3 = f"{summaTuotantoV3:.2f}" 
            summaTuotantoV3 = summaTuotantoV3.replace(".", ",")
            viikonpaiva = datetime.strptime(edellinenPaiva, "%d.%m.%Y").strftime("%a")
            f.write(f"{viikonpaiva}\t\t{edellinenPaiva}\t\t{summaKulutusV1}\t{summaKulutusV2}\t{summaKulutusV3}\t\t{summaTuotantoV1}\t{summaTuotantoV2}\t{summaTuotantoV3}\n") 
            summaKulutusV1 = rivi[2]/1000
            summaKulutusV2 = rivi[3]/1000
            summaKulutusV3 = rivi[4]/1000
            summaTuotantoV1 = rivi[5]/1000
            summaTuotantoV2 = rivi[6]/1000
            summaTuotantoV3 = rivi[7]/1000

        edellinenPaiva = suomalainenpvm
        
    summaKulutusV1 = f"{summaKulutusV1:.2f}" 
    summaKulutusV1 = summaKulutusV1.replace(".", ",")
    summaKulutusV2 = f"{summaKulutusV2:.2f}" 
    summaKulutusV2 = summaKulutusV2.replace(".", ",")
    summaKulutusV3 = f"{summaKulutusV3:.2f}" 
    summaKulutusV3 = summaKulutusV3.replace(".", ",")
    summaTuotantoV1 = f"{summaTuotantoV1:.2f}" 
    summaTuotantoV1 = summaTuotantoV1.replace(".", ",")
    summaTuotantoV2 = f"{summaTuotantoV2:.2f}" 
    summaTuotantoV2 = summaTuotantoV2.replace(".", ",")
    summaTuotantoV3 = f"{summaTuotantoV3:.2f}" 
    summaTuotantoV3 = summaTuotantoV3.replace(".", ",")
    viikonpaiva = datetime.strptime(edellinenPaiva, "%d.%m.%Y").strftime("%a")
    f.write(f"{viikonpaiva}\t\t{edellinenPaiva}\t\t{summaKulutusV1}\t{summaKulutusV2}\t{summaKulutusV3}\t\t{summaTuotantoV1}\t{summaTuotantoV2}\t{summaTuotantoV3}\n")    

def main():
    """Kokoaa datan taulukoksi"""
    with open("yhteenveto.txt", "a", encoding="utf-8") as f:
        for vkonro in [41, 42, 43]:
            sahko = hae_sahko(f"viikko{vkonro}.csv")
            print_kokovko(sahko, vkonro, f)
        

if __name__ == "__main__":
    main()

