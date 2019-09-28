import scipy.integrate as integrate
import math

def density(r,id):
    global den

    x=r/RE
    
    if id==1: # constant den model
        
        den=5.51*1000 # density in kg/m^3
        
    elif id==2:  #For all layers of earth
           if r <= 1221.5*1000:      #Inner Core
            den=(13.0885-8.8381*x**2)*1000 
           elif r>1221.5*1000 and r<=3480.0*1000:  #Outer Core
            den=(12.5815-1.2638*x-3.6426*x**2-5.5281*x**3)*1000
           elif r>3480.0*1000 and r<=3630.0*1000:    #Lower Mantle
            den=(7.9565-6.4761*x+5.5283*x**2-3.0807*x**3)*1000
           elif r>3630.0*1000 and r<=5600.0*1000:
            den=(7.9565-6.4761*x+5.5283*x**2-3.0807*x**3)*1000
           elif r>5600.0*1000 and r<=5701.0*1000:
            den=(7.9565-6.4761*x+5.5283*x**2-3.0807*x**3)*1000
           elif r>5701.0*1000 and r<=5771.0*1000:    #Transition Zone
            den=(5.3197-1.4836*x)*1000
           elif r>5771.0*1000 and r<=5971.0*1000:
            den=(11.2494-8.0298*x)*1000
           elif r>5971.0*1000 and r<=6151.0*1000:
            den=(7.1089-3.8045*x)*1000
           elif r>6151.0*1000 and r<=6291.0*1000:    #LVZ (Low Velocity Zone)
            den=(2.6910+0.6924*x)*1000
           elif r>6291.0*1000 and r<=6346.6*1000:    #LID
            den=(2.6910+0.6924*x)*1000
           elif r>6346.6*1000 and r<=6356.0*1000:    #Crust
            den=2.900*1000
           elif r>6356.0*1000 and r<=6368.0*1000:
            den=2.600*1000
           elif r>6368.0*1000 and r<=RE:   #Ocean
            den=1.020*1000
           else:
            den=0.0
    return den

def mass(r,id):
    res=integrate.quad(lambda y: 4.0*math.pi*density(y,id)*y*y,0,r)
    return res[0]

RE=6371.0*1000 #Radius of the Earth in meters
G=6.67*10**(-11)

    
P0=0.0
id=float(input("Enter '1' for Average density or '2' for Density at the user given distance: "))

#Using Simpson's 1/3 rule
r=RE    #Starting from the surface of the earth
dr=50.0*1000.0
x=-1
s=G*mass(r,id)*density(r,id)/r/r    
P=s*dr/3
print(r/1000,P/10**9,density(r,id)/1000)
n=1
while r>0:
    r=r-dr 
    if r>0 and r<50.0:              #For the last point
        s=s+G*mass(r,id)*density(r,id)/r/r
        P=(s)*dr/3
        print(r/1000,P/10**9,density(r,id)/1000)
    elif r>=50.0:
        s=s+(3-x)*G*mass(r,id)*density(r,id)/r/r
        P=(s)*dr/3
        print(r/1000,P/10**9,density(r,id)/1000)
    n=n+1
    x=-x

def inertia(r,id):
    calc=integrate.quad(lambda a: 8.0*math.pi/3.0*density(a,id)*a*a*a*a,0,RE)
    return calc[0]

print ("id: ",id)
print ("mass (kg): ",mass(RE,id))
print ("pressure at the center of the earth(GPa): ",P/10**9,n)
print ("Inertia of Earth(I): ", inertia (RE,id))



