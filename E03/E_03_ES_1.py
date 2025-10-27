import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df_fromfile=pd.read_csv('/Users/tizianomercuri/MCF/E03/kplr010666592-2011240104155_slc.csv')
#stampo il dataframe a schermo
print (df_fromfile)
#stampo il nome delle colonne
print (df_fromfile.columns)
#creo il grafico del flusso in funzione del tempo
asse_x=df_fromfile['TIME']
asse_y=df_fromfile['PDCSAP_FLUX']
#plt.plot(asse_x,asse_y,color='aquamarine')
#plt.xlabel('BJD-2454833')
#plt.ylabel('e-/s')
#plt.show()
#ricreo lo stesso grafico ma con punti definiti al posto della linea
plt.plot(asse_x,asse_y,'o',color='blue')
plt.xlabel('BJD-2454833')
plt.ylabel('e-/s')
plt.show()
#creo il grafico con errorbar
errore_y=df_fromfile['PDCSAP_FLUX_ERR']
plt.errorbar(asse_x,asse_y,yerr=errore_y,fmt='.',color='orange')
plt.xlabel('BJD-2454833')
plt.ylabel('e-/s')
plt.savefig("grafico.png",dpi=300) #comando per salvare il file nel formato .png
plt.show()
#creo un grafico che ricalca il primo, spostando la mia attenzione su un minimo
asse_x_2=df_fromfile.loc[(df_fromfile['TIME'] > 947.9) & (df_fromfile['TIME'] < 948.3),'TIME']
asse_y_2=df_fromfile.loc[(df_fromfile['TIME'] > 947.9) & (df_fromfile['TIME'] < 948.3),'PDCSAP_FLUX']
plt.plot(asse_x_2, asse_y_2,'o',color='black')
plt.xlabel('BJD-2454833')
plt.ylabel('e-/s')
plt.show()
#creo un grafico che mostra il tempo complessivo, e in un riquadro, uno zoom su un minimo
fig,ax=plt.subplots(figsize=(12,6))
ax.errorbar(asse_x,asse_y,yerr=errore_y,fmt='.',color='green')
x0,y0=0.6,0.65
width,length=0.4,0.35
ins_ax=ax.inset_axes([x0,y0,width,length])
ins_ax.errorbar(asse_x_2,asse_y_2,fmt='o',color='green')
plt.ylim(1.010*10**6,1.030*10**6)
plt.show()
