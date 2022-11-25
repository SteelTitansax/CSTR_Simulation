
#Design equation of an CSTR
#-------------------------
#Libraries
#Variable declarations
#---------------------

k = 0.5 #1/min
Ca0= 10 #mol/l
X = 0.8
#Kinetics
#--------
def rA(X):
    Ca = Ca0*(1-X)
    return k*Ca
#Volume
V = (-Ca0 * X) /-rA(X)
print("Volumen : " + str(V) )



