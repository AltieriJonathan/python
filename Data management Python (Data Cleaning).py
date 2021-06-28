#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


#A)Question 1
superficie = pd.read_csv("EuropeSuperficie.csv")


# In[4]:


superficie.head()


# In[5]:


superficie["Superficie(km2)"].sum()


# In[6]:


Total = {"États membres":"Total" , "Superficie(km2)": 4329287}
superficietotale=superficie.append(Total,ignore_index=True)


# In[7]:


import seaborn as sns
import matplotlib.pyplot as plt
fig_dims = (10, 10)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x ="Superficie(km2)" , y = "États membres", ax=ax, data=superficie)
test = "Bulgarie|Roumanie|Allemagne|Autriche|Belgique|Chypre|Danemark|Espagne|Estonie|Finlande|France|Grèce|Hongrie|Irlande|Italie|Lettonie|Lituanie|Luxembourg|Malte|Pays-Bas|Pologne|Portugal|République tchèque|Royaume-Uni|Slovaquie|Slovénie|Suède"


# In[8]:


superficie["Superficie(km2)"].max()


# In[9]:


superficie["Superficie(km2)"].min()


# In[10]:


#A)Question 2
population = pd.read_csv("pop.csv",encoding="utf-8")
population.head(30)


# In[11]:


europe = population.iloc[0]["Value"]
print("la population actuelle de l'europe est de:", europe ,"personnes" )


# In[12]:


popvalue= population["Value"].str.replace('\.','').str.replace('\:','')
popvalue


# In[13]:


popvalue.replace('', np.nan, inplace=True)
popvalue


# In[14]:


popvalue.fillna(0,inplace=True)


# In[15]:


popvalue=popvalue.astype(int)


# In[16]:


popvalue = pd.DataFrame(popvalue)
popvalue["Value"].sort_values().head(50)


# In[17]:


population["Value"]=popvalue["Value"]
population


# In[18]:


roundup="Union|Zone|euro|ancien|ancienne|Echange|composition|tropolitaine|Ancienne|Conseil|Azerba"
populationcleaned= population
populationcleaned=population.drop(labels=["AGE","SEX","UNIT","Flag and Footnotes"],axis=1)
populationcleaned["GEO"].str.replace("¿", "e")
populationcleaned=populationcleaned[~populationcleaned.GEO.str.contains(roundup)] 
populationcleaned


# In[19]:


populationcleaned.Value.sort_values().head(50)


# In[20]:


#min (flemmingite aigue)
Mini=populationcleaned[populationcleaned['Value'].astype(str).str.contains('31269')]
Mini


# In[21]:


populationcleaned.sort_values(["Value"]).tail()


# In[22]:


#max (flemmingite tres aigue)
paysmax= population.iloc[400]["Value"]
print("Le pays avec la plus grande population est de  :", paysmax, "personnes et c'est le pays suivant:",population.iloc[400]["GEO"] )
Maxi=populationcleaned[populationcleaned['Value'].astype(str).str.contains('143666931')]
Maxi


# In[23]:


pop2017=populationcleaned[populationcleaned['TIME'].astype(str).str.contains('2017')]
pop2017


# In[ ]:





# In[24]:


#B) Criminalité 
criminalite = pd.read_csv("crimes.csv")
criminalite.head(50)


# In[25]:


liste= criminalite["ICCS"].unique().tolist()
liste


# In[26]:


cambriolages = criminalite[criminalite['ICCS'].str.contains('Cambriolage')]


# In[27]:


cambriolagesen2007= cambriolages[cambriolages['TIME'] >=2007]
cambriolagesen2007.sort_values(["Value"])


# In[28]:


payscambriolagemin=cambriolagesen2007[cambriolagesen2007['Value'].astype(str).str.contains('102')]
payscambriolagemin["GEO"]


# In[29]:


valmin = cambriolagesen2007['Value'].min()


# In[30]:


print("La valeur minimale de cambriolages en 2007 est :",valmin,"et le pays est  :",payscambriolagemin.GEO)


# In[31]:


valmax = cambriolagesen2007["Value"].max()


# In[32]:


payscambriolagemax=cambriolagesen2007[cambriolagesen2007['Value'].astype(str).str.contains('280696')]
payscambriolagemax["GEO"]


# In[33]:


print("La valeur minimale de cambriolages en 2007 est :",valmax,"et le pays est  :",payscambriolagemax.GEO)


# In[34]:


#B2)
meurtres =criminalite[criminalite['ICCS'].str.contains('Homicide')]
meurtres


# In[35]:


paysmeurtres= meurtres.groupby("GEO")["Value"].sum().sort_values()
paysmeurtres


# In[36]:


paysmeurtres.iloc[0]
print("Le moins de meurtres se sont déroulés à Liechtenstein et le nombre etait de :",paysmeurtres.iloc[0])


# In[37]:


anneemeurtres= meurtres.groupby("TIME")["Value"].sum().sort_values()
anneemeurtres


# In[38]:


anneemeurtresmin= anneemeurtres.iloc[0]
print("l'année avec le moins de meurtre etait 2007 avec :",anneemeurtresmin,"meurtres.")


# In[39]:


meurtrespaysannees= meurtres.groupby(["TIME","GEO"])["Value"].sum().sort_values()
meurtrespaysannees.head(15)


# In[40]:


#B3)
blesses = criminalite[criminalite['ICCS'].str.contains('Actes')]
blesses


# In[41]:


blessesparpays= blesses.groupby(["GEO"])["Value"].sum().sort_values()
blessesparpays


# In[42]:


print("Le pays avec le moins de risques  d'etre bléssé est Liechtenstein avec un total de :",blessesparpays[0],"bléssés")


# In[43]:


print("Le pays avec le plus de risques  d'etre bléssé est England et Wales avec un total de :",blessesparpays[-1],"bléssés")


# In[44]:


#C) POLICE
police = pd.read_csv("police.csv",encoding="latin-1")
police.head()


# In[45]:


police2 = police["Value"].str.replace('\.','').str.replace('\:','').str.replace('\<','')


# In[46]:


police2.replace('', np.nan, inplace=True)


# In[47]:


police2=police2.fillna(0)


# In[48]:


police2 = pd.DataFrame(police2)
police2


# In[49]:


police2=police2["Value"].astype(int)
police2


# In[50]:


police2 = pd.DataFrame(police2)
police2


# In[51]:


police["Value"]=police2["Value"]


# In[52]:


police["Value"]=police2["Value"]


# In[53]:


moyeffectifs = police.groupby(["TIME","GEO"])["Value"].mean().sort_values()
moyeffectifs= pd.DataFrame(moyeffectifs)
moyeffectifs=moyeffectifs.reset_index()
moyeffectifs


# In[54]:


moyeffectifs2002= moyeffectifs[moyeffectifs['TIME'].astype(str).str.contains('2002')]
moyeffectifs2002


# In[55]:


import seaborn as sns
import matplotlib.pyplot as plt
fig_dims = (10, 10)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x ="Value" , y = "GEO", ax=ax, data=moyeffectifs2002)


# In[56]:


#Pays avec le plus d'effectif en 2002
moyeffectifs2002.iloc[-1]


# In[57]:


copsurpop = police
copsurpop=copsurpop.drop("UNIT",axis=1)
copsurpop.sort_values
copsurpop.tail(60)


# In[58]:


roundup2="métropolitaine|jusqu'en "
copsurpop=copsurpop[~copsurpop.GEO.str.contains(roundup2)] 


# In[59]:


copsurpop2007=copsurpop[copsurpop.TIME.astype(str).str.contains("2007")] 
copsurpop2007


# In[60]:


tolist=copsurpop2007["GEO"].tolist()
tolist


# In[61]:


Dict1={'Belgique':10666866,
 'Tchéquie':10343422,
 'Danemark':5475791,
 'Estonie':1338440,
 'Irlande':4457765,
 'Grèce':11060937,
 'Espagne':45668939,
 'France':64007193,
 'Croatie':4311967,
 'Italie':58652875,
 'Chypre':776333,
 'Lettonie':2191810,
 'Lituanie':3212605,
 'Luxembourg':483799,
 'Hongrie':10045401,
 'Malte':407832,
 'Pays-Bas':16405399,
 'Autriche':8307989,
 'Pologne':38115641,
 'Portugal':10553339,
 'Roumanie':20635460,
 'Slovénie':2010269,
 'Slovaquie':5376064,
 'Finlande':5300484,
 'Suède':9182927,
 'England et Wales':61571647,
 'Scotland':5454000,
 'Northern Ireland (UK)':1882000,
 'Islande':315459,
 'Liechtenstein':35356,
 'Norvège':4737171,
 'Suisse':7593494,
 'Ancienne République yougoslave de Macédoine':23230000 ,
 'Turquie':82000000}
liste1 =[10666866,10343422,5475791,1338440,4457765,11060937,45668939,64007193,4311967,58652875,
        776333,2191810,3212605,483799,10045401,407832,16405399,8307989,38115641,10553339,20635460,2010269
        ,5376064,5300484,9182927,61571647,5454000,1882000,315459,35356,4737171,7593494,23230000,82000000]
copsurpop2007["Population"]=liste1
copsurpop2007


# In[62]:


copsurpop2007["RateCop"]=copsurpop2007['Value']/copsurpop2007['Population']*100000
copsurpop2007


# In[63]:


import seaborn as sns
import matplotlib.pyplot as plt
fig_dims = (10, 10)
fig, ax = plt.subplots(figsize=fig_dims)
sns.barplot(x ="RateCop" , y = "GEO", ax=ax, data=copsurpop2007)


# In[187]:


copsurpop2007.to_csv(r'C:\Users\Ultim\Documents\Driss Mongodb\copsurpop2007.csv')


# In[253]:


#D)Prison
Prison= pd.read_csv("prison.csv")
Prison


# In[254]:


CleanPrison= Prison["Eff_pri"].str.replace("\:","").str.replace('\:','').str.replace('\<','')

CleanPrison


# In[255]:


CleanPrison.replace('', np.nan, inplace=True)
CleanPrison=CleanPrison.fillna(0)
CleanPrison = pd.DataFrame(CleanPrison)
CleanPrison


# In[256]:


CleanPrison=CleanPrison["Eff_pri"].astype(int)
CleanPrison


# In[257]:


CleanPrison = pd.DataFrame(CleanPrison)
CleanPrison


# In[258]:


Prison["Eff_pri"]=CleanPrison["Eff_pri"]
Prison


# In[259]:


Payscarceral= Prison.groupby(["Pays"])["Eff_pri"].sum().sort_values()
Payscarceral=pd.DataFrame(Payscarceral)
Payscarceral.reset_index()


# In[260]:


#1)
payspluscarceral= Payscarceral.iloc[-1]
payspluscarceral


# In[261]:


#2)
paysmoinscarceral=Payscarceral.iloc[0]
paysmoinscarceral


# In[264]:


Prison= pd.DataFrame(Prison)


# In[274]:


#3)
anneepluscarcerale= Prison.groupby(["Annee"])["Eff_pri"].sum().sort_values()
anneepluscarcerale= pd.DataFrame(anneepluscarcerale).reset_index()
anneepluscarcerale.iloc[-1]


# In[277]:


#E)1)
Santé=pd.read_csv("depensesSanté.csv")
Santé.head(50)


# In[292]:


europarhabitant= Santé.groupby(["Unite","Pays"])["Montant"].sum()
europarhabitant=pd.DataFrame(europarhabitant)
europarhabitant=europarhabitant.head(39)
europarhabitant


# In[298]:


europarhabitant=europarhabitant.Montant.sort_values()
europarhabitant=pd.DataFrame(europarhabitant)
europarhabitant.iloc[-1]


# In[309]:


tauxbulgarie=Santé[Santé.Pays.astype(str).str.contains("Bulgarie")] 
tauxbulgarie=tauxbulgarie[tauxbulgarie["Annee"].astype(str).str.contains("Bulgarie")] 
tauxbulgarie


# In[ ]:




