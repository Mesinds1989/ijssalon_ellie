from helper import decoreer

def print_aanbieding():
    prijzen={
        "aardbei": 3,
        "vanille": 4,
        "Chocolade": 5,
        
    }

    aanbieding = prijzen["aardbei"]*0.8
    reclame_tekst=(f"vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}")
    reclame_tekst2=reclame_tekst[:63]
    #print(reclame_tekst.index("0"))
    reclame_tekst3=reclame_tekst2.upper()
    reclame_tekst4=reclame_tekst3.split()
    #print(reclame_tekst4)

    for el in reclame_tekst4:
        if (len(el)) <4:
            print(el.lower())
            
        if (len(el))> 3:
            print(el)
decoreer("aanbieding")
print_aanbieding()