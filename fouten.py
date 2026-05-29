import math
def discriminant(a,b,c):
    try:
        D1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        D2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        uitvoer=[D1,D2]

    except:
        uitvoer="  "

    return (uitvoer)

a=int (input("wat is a?"))
b=int (input("wat is b?"))
c=int (input("wat is c?"))
uitkomst=discriminant(a,b,c)
'''
if uitkomst >0:
    D1=uitkomst[0]
else:
    D1="geen oplossing"
'''    
D1=uitkomst[0]
D2=uitkomst[1]

print(f"Voor de formule ax^2+bx+c, geef {a},{b} en {c}: {D1} en {D2}")