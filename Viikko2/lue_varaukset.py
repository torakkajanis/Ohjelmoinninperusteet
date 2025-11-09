"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tulostetaan varaus konsoliin
    #print(varaus)

    from datetime import datetime

    # Kokeile näitä
    #print(varaus.split('|'))
    varausId = int(varaus.split('|')[0])
    varaaja = varaus.split('|')[1]
    paiva = datetime.strptime(varaus.split('|')[2], "%Y-%m-%d").date()
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
    suomalainenAika = aika.strftime("%H.%M")
    tunnit = int(varaus.split('|')[4])
    tuntihinta = float(varaus.split('|')[5])
    kokonaishinta = tunnit * tuntihinta
    maksettu = bool(varaus.split('|')[6])
    kohde = varaus.split('|')[7]
    puhelin = varaus.split('|')[8]
    email = varaus.split('|')[9]
    #print(varausId)
    #print(type(varausId))
    print(f"Varausnumero: {varausId}")
    print(f"Varaaja: {varaaja}")
    print(f"Päivämäärä: {suomalainenPaiva}")
    print(f"Aloitusaika: {suomalainenAika}")
    print(f"Tuntimäärä: {tunnit}")
    print(f"Tuntihinta: {tuntihinta} €")
    print(f"Kokonaishinta: {kokonaishinta} €")
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    print(f"Kohde: {kohde}")
    print(f"Puhelin: {puhelin}")
    print(f"Sähköposti: {email}")

    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()