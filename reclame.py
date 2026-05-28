from Algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    korting=(1-korting)
    korting=prijs*korting
    print (f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro.")

def inkomsten_totaal(inkomsten):
    
    totaal=sum (inkomsten)
    bedrag=sum (inkomsten)*0.09
    
    return(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")
print(inkomsten_totaal((220,430,125,160,205,90,345)))

def laag_en_hoog(mijn_lijst):
    
    return(max(mijn_lijst),min(mijn_lijst))

print(laag_en_hoog((220,430,125,160,205,90,345)))

def gemiddelde(mijn_lijst):
    if mijn_lijst:
        gemiddelde=sum(mijn_lijst)/len(mijn_lijst)
        return (f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro")
    
print(gemiddelde((220,430,125,160,205,90,345)))

def meervoudig(invoer_lijst):
    terug=laag_en_hoog(invoer_lijst)
    return terug 

print(meervoudig((2,4,5,6,7,8,6,3,9)))

def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer=mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer