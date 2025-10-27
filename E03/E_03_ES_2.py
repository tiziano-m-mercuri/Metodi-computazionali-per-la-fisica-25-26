import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#creo un dataframe partendo dal file assegnato
df_planets=pd.read_csv('/Users/tizianomercuri/MCF/E03/ExoplanetsPars_2025.csv',comment='#')
print(df_planets)
#stampo i nomi delle colonne
print(df_planets.columns)
#stampo le prime 5 righe del dataframe
print(df_planets.head())
#creo un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale
asse_x=df_planets['pl_orbper']
asse_y=df_planets['pl_bmassj']
#verifico che all'interno del file ci siano i pianeti del nostro sistema solare
pianeti=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
presenti=df_planets['pl_name'].isin(pianeti)
print(df_planets[presenti])
#dal momento che non ci sono, creo un nuovo dataframe con i pianeti del sistema solare
dati_sol = {'pl_name': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'], 'mass': [0.00017,0.00256,0.00315,0.00034,1.00000,0.29942,0.04561,0.05380],   # masse in confronto con quella di Giove
'period': [88, 225, 365, 687, 4333, 10759, 30687, 60190],       # giorni
'orbp_max': [0.387,0.723,1.000,1.525,5.203,9.537,19.191,30.07] #semiasse maggiore dell'orbita
}
df_sol = pd.DataFrame(dati_sol)
plt.figure(figsize=(10,6))
plt.scatter(asse_x,asse_y,color='orange',label='esopianeti',alpha=0.6)
plt.scatter(dati_sol['period'],dati_sol['mass'],color='grey',label='sistema solare')
plt.xlabel('periodo[giorni]')
plt.ylabel('massa[M_j]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
#creo un grafico in termini di R_max^2/M_star in funzione del periodo orbitale, sempre in scala logaritmica
rapp_exop=np.array([(df_planets['pl_orbsmax']**2/df_planets['st_mass'])])
massa_sole=np.ones(8)
rapp_sistsol=np.array([df_sol['orbp_max']**2/massa_sole])
plt.figure(figsize=(10,6))
plt.scatter(asse_x,rapp_exop,color='orange',label='esopianeti',alpha=0.6)
plt.scatter(dati_sol['period'],rapp_sistsol,color='grey',label='sistema solare')
plt.xlabel('periodo[giorni]')
plt.ylabel('R^2_max/m_star[m_sun/giorni]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
#creo un grafico che ricalca il primo, differenziando il modo di scoperta degli esopianeti
asse_x_2=df_planets.loc[df_planets['discoverymethod']=='Radial Velocity','pl_orbper']
asse_y_2=df_planets.loc[df_planets['discoverymethod']=='Radial Velocity','pl_bmassj']
asse_x_3=df_planets.loc[df_planets['discoverymethod']=='Transit','pl_orbper']
asse_y_3=df_planets.loc[df_planets['discoverymethod']=='Transit','pl_bmassj']
plt.figure(figsize=(10,6))
plt.scatter(asse_x_2,asse_y_2,color='green',label='Radial Velocity',alpha=0.6)
plt.scatter(asse_x_3,asse_y_3,color='tomato',label='Transit',alpha=0.6)
plt.scatter(dati_sol['period'],dati_sol['mass'],color='grey',label='Sistema Solare')
plt.xlabel('Periodo[Giorni]')
plt.ylabel('Massa[_Mj]')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
#creo un istogramma che distingua il numero di esopianeti per modo di scoperta
plt.figure(figsize=(10,6))
max_mass = max(df_planets['pl_bmassj'].max(), 1)
plt.hist(asse_y_2,bins=50,range=(0,max_mass),alpha=0.6,color='blue',label='Radial Velocity')
plt.hist(asse_y_3,bins=50,range=(0,max_mass),alpha=0.6,color='orange',label='Transit')
plt.ylabel('Numero di pianeti')
plt.xscale('log')
plt.legend()
plt.show()
