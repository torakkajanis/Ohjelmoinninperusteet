"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | datetime.date | datetime.time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettuvaraus = []
    # Ensimmäisen alkion = varaus[0] muunnos
    muutettuvaraus.append(int(varaus[0]))
    # Ja tästä jatkuu
    muutettuvaraus.append(varaus[1])

    muutettuvaraus.append(varaus[2])

    muutettuvaraus.append(varaus[3])

    varauksen_pvm = datetime.strptime(varaus[4], "%Y-%m-%d").date()
    muutettuvaraus.append(varauksen_pvm)

    varauksen_klo = datetime.strptime(varaus[5], "%H:%M").time()
    muutettuvaraus.append(varauksen_klo)


    muutettuvaraus.append(int(varaus[6]))

    hinta = float(varaus[7])
    muutettuvaraus.append(hinta)

    varaus_vahvistettu = bool(varaus[8] == "True")
    muutettuvaraus.append(varaus_vahvistettu)

    muutettuvaraus.append(varaus[9])
    
    varaus_luotu = datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S")
    muutettuvaraus.append(varaus_luotu)
    

    return muutettuvaraus

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def main():
    # HUOM! seuraaville riveille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset("varaukset.txt")
    print(" | ".join(varaukset[0]))
    print("------------------------------------------------------------------------")
    for varaus in varaukset[1:]:
        print(" | ".join(str(x) for x in varaus))
        tietotyypit = [type(x).__name__ for x in varaus]
        print(" | ".join(tietotyypit))
        print("------------------------------------------------------------------------")

    print("")
    print("")
    print("")

    print("1) Vahvistetut varaukset")
    for varaus in varaukset[1:]:
        suomalainenaika = varaus[5].strftime("%H:%M")
        suomalainenpvm = varaus[4].strftime("%d.%m.%Y")
        if varaus[8]:
            print (f"- {varaus[1]},",f"{varaus[9]},",f"{suomalainenpvm}",f"klo {suomalainenaika}")

    print("")

    print("2) Pitkät varaukset (≥ 3 tuntia)")
    for varaus in varaukset [1:]:
        suomalainenaika = varaus[5].strftime("%H:%M")
        suomalainenpvm = varaus[4].strftime("%d.%m.%Y")
        if varaus[6] >=3:
            print (f"- {varaus[1]},",f"{suomalainenpvm}",f"klo {suomalainenaika},",f"kesto {varaus[6]}h,", f"{varaus[9]}")

    print("")

    print("3) Varausten vahvistusstatus")
    for varaus in varaukset [1:]:
        if varaus [8]:
            print (f"{varaus[1]} -> Vahvistettu")
        else:
            print (f"{varaus[1]} -> EI vahvistettu")

    print("")

    print("4) Yhteenveto vahvistuksista")
    total = 0
    for varaus in varaukset [1:]:
        if varaus[8]:
            total += 1
    print (f"- Vahvistettuja varauksia: {total} kpl")
    total = 0
    for varaus in varaukset [1:]:
        if not varaus[8]:
            total += 1
    print (f"- Ei-vahvistettuja varauksia: {total} kpl")

    print("")
    
    print("5) Vahvistettujan varausten kokonaistulot")
    total=0
    for varaus in varaukset [1:]:
        if varaus[8]:
            total += varaus[6]*varaus[7]
    summa_str = f"{total:.2f}".replace(".", ",")
    print (f"Vahvistettujan varausten kokonaistulot: {summa_str} €")

    print("")


if __name__ == "__main__":
    main()

