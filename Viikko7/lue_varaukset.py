# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.

#Käytössä sanakirja, koska avaimet tuntuvat loogisemmilta ja lyhyemmiltä kuin olioissa. 

from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    muutettu_varaus = []
    muutettu_varaus.append(int(varaus[0]))
    muutettu_varaus.append(varaus[1])
    muutettu_varaus.append(varaus[2])
    muutettu_varaus.append(varaus[3])
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())
    muutettu_varaus.append(int(varaus[6]))
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8].lower() == "true")
    muutettu_varaus.append(varaus[9])
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muutettu_varaus

def hae_varaukset(varaustiedosto: str) -> list:
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def muunna_varaustiedot(varaus_lista: list[str]) -> dict:
    return {
        "id": int(varaus_lista[0]),
        "nimi": varaus_lista[1],
        "sahkoposti": varaus_lista[2],
        "puhelin": varaus_lista[3],
        "pvm": datetime.strptime(varaus_lista[4], "%Y-%m-%d").date(),
        "klo": datetime.strptime(varaus_lista[5], "%H:%M").time(),
        "kesto": int(varaus_lista[6]),
        "hinta": float(varaus_lista[7]),
        "vahvistettu": varaus_lista[8],
        "tila": varaus_lista[9],
        "luotu": varaus_lista[10]
    }


def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            print(f"- {varaus["nimi"]}, {varaus["tila"]}, {varaus["pvm"].strftime('%d.%m.%Y')} klo {varaus["klo"].strftime('%H.%M')}")

    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus["kesto"] >= 3):
            print(f"- {varaus["nimi"]}, {varaus["pvm"].strftime('%d.%m.%Y')} klo {varaus["klo"].strftime('%H.%M')}, kesto {varaus["kesto"]} h, {varaus["tila"]}")

    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            print(f"{varaus["nimi"]} → Vahvistettu")
        else:
            print(f"{varaus["nimi"]} → EI vahvistettu")

    print()

def varausten_lkm(varaukset: list):
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl")
    print()

def varausten_kokonaistulot(varaukset: list):
    varaustenTulot = 0
    for varaus in varaukset[1:]:
        if(varaus["vahvistettu"]):
            varaustenTulot += varaus["kesto"]*varaus["hinta"]

    print("Vahvistettujen varausten kokonaistulot:", f"{varaustenTulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()