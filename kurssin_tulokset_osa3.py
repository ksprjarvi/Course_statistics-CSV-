# Funktio antaa lopullisen kurssin arvosanan riippuen pistemäärästä. 
def lopullinen_arvosana(pisteet: int):
    pisterajat = [15, 18, 21, 24, 28]
    if pisteet >= 28:
        return 5
    for raja in pisterajat:
        if pisteet < raja:
            arvosana = pisterajat.index(raja)
            return arvosana

# Funktio luo ja palauttaa tehtävien arvosanan. 
def tehtava_pisteet(tehtavat: int):
    return tehtavat // 4

# Funktio tulostaa otsikot oikeaan tulostusmuotoon. 
def tulosta_otsikot():
    nimi = 'nimi'
    teht_lkm = 'teht_lkm'
    teht_pist = 'teht_pist'
    koe_pist = 'koe_pist'
    yht_pist = 'yht_pist'
    arvo_sana = 'arvosana'

    print(f'{nimi:30}{teht_lkm:10}{teht_pist:10}{koe_pist:10}{yht_pist:10}{arvo_sana:10}')


# Funktio lukee 3 CSV tiedostoa ja muodostaa niistä tulostettavan kokonaistilaston. 
def kurssin_tulokset():
    # Luetaan ensiksi valitut tiedostot.
    opiskelijatiedot = input("Opiskelijatiedot: ")
    tehtavatiedot = input("Tehtävätiedot: ")
    koepisteet = input('Koepisteet: ')

    # Lisätään opiskelijat omaan sanakirjaansa muodossa: opiskelijanumero, nimi
    with open(opiskelijatiedot) as tiedosto:
        opiskelijat = {}

        # Käydään tiedosto läpi rivi riviltä.
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '')
            osat = rivi.split(';')  # Jaetaan rivi ; - merkkien kohdalta omiksi alkioikseen jotka lisätään 'osat' - listaan. 

            # Käydään osat - lista läpi.
            for osa in osat:
                if osat[0] == 'opnro':  # Jos otsikkorivi; jatketaan.
                    continue
                opiskelijat[osat[0]] = str(f'{osat[1]} {osat[2]}')  # Lisätään opiskelijat sanakirjaan.
    
    # Lisätään tehtävät omaan sanakirjaansa muodossa: opiskelijanumero, tehtävät.
    with open(tehtavatiedot) as tiedosto:
        tehtavat = {}

        # Käydään tiedosto läpi rivi riviltä. 
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '') 
            osat = rivi.split(';')  # Jaetaan rivi ; - merkkien kohdalta omiksi alkioikseen jotka lisätään 'osat' - listaan. 

            # Käydään osat - lista läpi. 
            for osa in osat: 
                if osat[0] == 'opnro': # Jos otsikkorivi; jatketaan. 
                    continue
                tehtavat[osat[0]] = []
                for tehtava in osat[1:]:
                    tehtavat[osat[0]].append(int(tehtava))  # Lisätään tehtävät sanakirjaan. 
    
    # Lisätään koepisteet omaan sanakirjaansa muodossa: opiskelijanumero, arvosanat
    with open(koepisteet) as tiedosto:
        kpisteet = {}

        # Käydään tiedosto läpi rivi riviltä. 
        for rivi in tiedosto:
            rivi = rivi.replace('\n', '')
            osat = rivi.split(';')  # Jaetaan rivi ; - merkkien kohdalta omiksi alkioikseen jotka lisätään 'osat' - listaan.

             # Käydään osat - lista läpi.
            for osa in osat:
                if osat[0] == 'opnro':  # Jos otsikkorivi; jatketaan. 
                    continue
                kpisteet[osat[0]] = []
                for arvosana in osat[1:]:
                    kpisteet[osat[0]].append(int(arvosana))  # Lisätään arvosanat sanakirjaan.
    
    # tulosta_otsikot() tulostaa kaikki yhdistetyt tiedot.
    # Tulostusesimerkki:
    # nimi                          teht_lkm  teht_pist koe_pist  yht_pist  arvosana  
    # pekka peloton                 25        6         11        17        1         
    # jaana javanainen              27        6         10        16        1         
    # liisa virtanen                35        8         6         14        0         
    # donald frump                  0         0         15        15        1         
    # john doe                      28        7         16        23        3         
    # angela tarkel                 32        8         13        21        3         
    # karkki eila                   30        7         7         14        0         
    # alan turing                   28        7         19        26        4         
    # ada lovelace                  27        6         27        33        5   
    tulosta_otsikot()
    for opnro, nimi in opiskelijat.items():
        if opnro in tehtavat:
            if opnro in kpisteet:
                pisteet_yhteensa = sum(kpisteet[opnro]) + tehtava_pisteet(sum(tehtavat[opnro]))  # Yhteispisteet
                tulostettava_arvosana = lopullinen_arvosana(pisteet_yhteensa)  # Arvosana
                tehtavat_lkm = sum(tehtavat[opnro])  # Tehtävien lukumäärä
                tehtavien_pisteet = tehtava_pisteet(sum(tehtavat[opnro]))  # Tehtävien pisteet
                koepisteet = sum(kpisteet[opnro])  # Koepisteet
                print(f'{nimi:30}{tehtavat_lkm:<10}{tehtavien_pisteet:<10}{koepisteet:<10}{pisteet_yhteensa:<10}{tulostettava_arvosana:<10}')

    
if __name__ == '__main__':
    pass
kurssin_tulokset()
