print("Calcuation of Weisz Prater criterion")
def WeiszPrater(r, p, rl, deff, C):
    cwp = -r*p*rl**2/(deff*C)

    print("Weisz Prater criterion value: " , cwp)
    if cwp < 1:
        print("Internal Mass Transfer is negligible")
    else:
        print("Internal Mass Transfer is significant")

r = float(input("reaction rate (mol/g s) :"))
p = float(input("density of catalyst (g/ cm^3):"))
rl = float(input("characteristic length of catalyst particle (cm) :"))

kb = 1.3807 * 10 ** -16 #cm^2 g s^-1 K^-1
T = float(input("Reaction Temperature (K):"))
mr = float(input("molar mass of reactant:"))
dpr = float(input("pore diameter of catalyst (cm):"))
deff = (1/3)*(8*kb*T/(3.14*mr))**0.5*dpr
C = float(input("Concentration of the reactant gas on the catalyst surface (mol cm^-3) :"))

print(WeiszPrater(r, p, rl, deff, C))



