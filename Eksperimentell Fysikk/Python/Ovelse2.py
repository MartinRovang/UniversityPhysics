import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 14
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


#Import data
df = np.array(pd.read_csv('Data\Eksperiment_1.csv'))
df2 = np.array(pd.read_csv('Data\Eksperiment_2.csv'))
df3 = np.array(pd.read_csv('Data\Eksperiment_3.csv'))

#Initialize array
Time = df[:,0] - 1100
Temp = df[:,2] + df[:,3]*10**(-2)
Time2 = df2[:,0]
Temp2 = df2[:,2] + df2[:,3]*10**(-2)
Time3 = df3[:,0]
Temp3 = df3[:,2] + df3[:,3]*10**(-2)

#-------------------------EXPERIMENT 1----------------------------------
#Uncertainty
#Linreg rom temp
timer = 155.5
coefs,cov = np.polyfit(Time[:200], Temp[:200],1,cov=True)
coefs11,cov11 = np.polyfit(Time[288:450], Temp[288:450],1,cov=True)
coefs111,cov111 = np.polyfit(Time[550:782], Temp[550:782],1,cov=True)
sumromtemp = timer*coefs[0]




#-------------------------EXPERIMENT 2----------------------------------
#Uncertainty
#Linreg rom temp
timer2 = 209.1
coefs2,cov2 = np.polyfit(Time2[15:150], Temp2[15:150],1,cov=True)
coefs22,cov22 = np.polyfit(Time2[315:495], Temp2[315:495],1,cov=True)
coefs222,cov222 = np.polyfit(Time2[600:700], Temp2[600:700],1,cov=True)
sumromtemp2 = timer2*coefs2[0]





#-------------------------EXPERIMENT 3----------------------------------
#Uncertainty
#Linreg rom temp
timer3 = 143.6
coefs3,cov3 = np.polyfit(Time3[15:150], Temp3[15:150],1,cov=True)
coefs33,cov33 = np.polyfit(Time3[280:412], Temp3[280:412],1,cov=True)
coefs333,cov333 = np.polyfit(Time3[469:600], Temp3[469:600],1,cov=True)
sumromtemp3 = timer3*coefs3[0]




#-------------------------PLOT 1-------------------------------------
plt.figure(figsize=(10,6))
plt.plot(Time,Temp, label='Forsøk 1')
#Baseline
plt.plot(Time[100:250],Time[100:250]*coefs[0] + coefs[1],'--', label='Baseline 1')
plt.plot(Time[200:600],Time[200:600]*coefs11[0] + coefs11[1],'--', label='Baseline 2')
plt.plot(Time2[500:800],Time2[500:800]*coefs111[0] + coefs111[1],'--', label='Baseline 3')
plt.plot([464,464],[21.3,33.5])
plt.plot([1033,1033],[26.13,33.6])
plt.text(300, 20.5,'-0.000110x + 21.721782', fontsize=10)
plt.text(717, 34.3,'-0.000242x + 33.760149', fontsize=10)
plt.text(1235, 27,'-0.000850x + 27.239970', fontsize=10)
plt.text(250, 28, r'$\Delta$T = 11.97 $^{\circ}$C', fontsize=10)
plt.text(1075, 29.7, r'$\Delta$T = 7.14 $^{\circ}$C', fontsize=10)



plt.yticks(np.arange(min(Temp),36,1))
plt.legend(loc='upper left')
plt.xlabel('Tid [s]')
plt.ylabel('Temperatur [$^{\circ}$C]')
plt.savefig('Plot1.pdf')
plt.show()



#-------------------------PLOT 2-------------------------------------
plt.figure(figsize=(10,6))
plt.plot(Time2,Temp2, label='Forsøk 2')
#Baseline
plt.plot(Time2[100:250],Time2[100:250]*coefs2[0] + coefs2[1],'--', label='Baseline 1')
plt.plot(Time2[200:600],Time2[200:600]*coefs22[0] + coefs22[1],'--', label='Baseline 2')
plt.plot(Time2[500:800],Time2[500:800]*coefs222[0] + coefs222[1],'--', label='Baseline 3')
plt.plot([466,466],[12.9,33.5])
plt.plot([1052,1052],[23,31.5])
plt.text(200, 14,'0.000560x + 12.374556', fontsize=10)
plt.text(760, 33,'-0.001567x + 33.095603', fontsize=10)
plt.text(1150, 21.9,'-0.000376x + 23.764780', fontsize=10)
plt.text(560, 23, r'$\Delta$T = 19.73 $^{\circ}$C', fontsize=10)
plt.text(1099, 27, r'$\Delta$T = 8.07 $^{\circ}$C', fontsize=10)


plt.yticks(np.arange(min(Temp2),36,1))
plt.legend(loc='upper left')
plt.xlabel('Tid [s]')
plt.ylabel('Temperatur [$^{\circ}$C]')
plt.savefig('Plot2.pdf')

plt.show()

#-------------------------PLOT 3-------------------------------------
plt.figure(figsize=(10,6))
plt.plot(Time3,Temp3, label='Forsøk 3')
#Baseline
plt.plot(Time3[100:250],Time3[100:250]*coefs3[0] + coefs3[1],'--', label='Baseline 1')
plt.plot(Time3[200:500],Time3[200:500]*coefs33[0] + coefs33[1],'--', label='Baseline 2')
plt.plot(Time3[400:600],Time3[400:600]*coefs333[0]  + coefs333[1],'--', label='Baseline 3')
plt.plot([413,413],[17.9,33.5])
plt.plot([855,855],[23.10,32.91])
plt.text(310, 16.37,'0.000174x + 17.766455', fontsize=10)
plt.text(685, 33.8,'-0.001303x + 33.902473', fontsize=10)
plt.text(910, 22,'-0.000465x + 23.697656', fontsize=10)
plt.text(484, 25, r'$\Delta$T = 15.52 $^{\circ}$C', fontsize=10)
plt.text(897, 27, r'$\Delta$T = 9.48 $^{\circ}$C', fontsize=10)


plt.yticks(np.arange(min(Temp2),36,1))
plt.legend(loc='upper left')
plt.xlabel('Tid [s]')
plt.ylabel('Temperatur [$^{\circ}$C]')
plt.savefig('Plot3.pdf')

plt.show()


#Prints
print("-----------------------PLOT1----------------------------------")
print("Stigning temp første: %f og %f" %(coefs[0],coefs[1]))
print("Stigning temp øverste: %f og %f" %(coefs11[0],coefs11[1]))
print("Stigning temp siste: %f og %f" %(coefs111[0],coefs111[1]))

print("-----------------------PLOT2----------------------------------")
print("Stigning temp første: %f og %f" %(coefs2[0],coefs2[1]))
print("Stigning temp øverste: %f og %f" %(coefs22[0],coefs22[1]))
print("Stigning temp siste: %f og %f" %(coefs222[0],coefs222[1]))

print("-----------------------PLOT3----------------------------------")
print("Stigning temp første: %f og %f" %(coefs3[0],coefs3[1]))
print("Stigning temp øverste: %f og %f" %(coefs33[0],coefs33[1]))
print("Stigning temp siste: %f og %f" %(coefs333[0],coefs333[1]))




print("%f"%((coefs11[0]*464+coefs11[1])-(coefs[0]*464+coefs[1])))
print("%f"%((coefs22[0]*466+coefs22[1])-(coefs2[0]*466+coefs2[1])))
print("%f"%((coefs33[0]*413+coefs33[1])-(coefs3[0]*413+coefs3[1])))
print("T1 %f"%(coefs11[0]*1033+coefs11[1]))
print("T2 %f"%(coefs111[0]*1033+coefs111[1]))
print("T1 for 2 %f"%(coefs22[0]*1052+coefs22[1]))
print("T2 for 2 %f"%(coefs222[0]*1052+coefs222[1]))
print("T1 for 3 %f"%(coefs33[0]*855+coefs33[1]))
print("T2 for 3 %f"%(coefs333[0]*855+coefs333[1]))

print("%f"%((coefs11[0]*1033+coefs11[1])-(coefs111[0]*1033+coefs111[1])))
print("%f"%((coefs22[0]*1052+coefs22[1])-(coefs222[0]*1052+coefs222[1])))
print("%f"%((coefs33[0]*855+coefs33[1])-(coefs333[0]*855+coefs333[1])))

#heatcap
deltaTstart = Temp[150]-Temp[15]
deltaTvarme = ((coefs11[0]*464+coefs11[1])-(coefs[0]*464+coefs[1]))
P = 322
varmekap = P*timer/(deltaTvarme)



#heatcap
deltaTstart2 = Temp2[150]-Temp2[15]
deltaTvarme2 = ((coefs22[0]*466+coefs22[1])-(coefs2[0]*466+coefs2[1]))
P2 = 323
varmekap2 = P2*timer2/(deltaTvarme2)



#heatcap
deltaTstart3 = Temp3[169]-Temp3[0]
deltaTvarme3 = ((coefs33[0]*413+coefs33[1])-(coefs3[0]*413+coefs3[1]))
P3 = 323
varmekap3 = P3*timer3/(deltaTvarme3)

print(varmekap)
print(varmekap2)
print(varmekap3)
