

def presenteer(dict,totaal):
    for k,v in dict.items():
        print(f"{k} : {v}")
    
    print("==========================")
    totaal=(f"Totaal : {totaal}")
    return totaal
    

   

totaal=50
mijn_dict={'vis':10, 'vlees':25,'overig':15}
