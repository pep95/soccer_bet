'''
this class have as goal to generate a predicion using the old statisics

@author: giusc
'''
import pandas as pd
import numpy as np

class stats:
    def __init__(self,pre,post,last_played,threshold):
        self.df = pd.read_csv(post).drop(columns=["Unnamed: 0"]) #upload db with all stats
        self.threshold = threshold
        self.df2 = pd.read_csv(pre,sep=";")[last_played:last_played+10].drop(columns=["Column1","Column3","Column6"]) #upload math to predict results
        
    def calc(self):
        
        def wordcount(lista,col):
            dict = {}
            c = 0
            for word in lista:
                if word in dict:
                    if dict[word]>(len(lista)*0.4):
                        c = 1
                    dict[word] = dict[word]+1
                else:
                    dict[word] = 1
            return dict,c
        
        
        def gg_ng_ht(df):
            gg = 0
            ng = 0
            for row in df.iloc:
                if int(row["gol casa HT"])>0 and int(row["gol trasferta HT"])>0:
                    gg = gg + 1
                else:
                    ng = ng + 1
            return gg,ng
        
        def gg_ng_2t(df):
            gg = 0
            ng = 0
            for row in df.iloc:
                if int(row["gol casa 2T"])>0 and int(row["gol trasferta 2T"])>0:
                    gg = gg + 1
                else:
                    ng = ng + 1
            return gg,ng
        
        
        def game_interesting(casa,tras,df,cols,threshold):
            dfcasa = df[df["casa"]==casa]
            dftras = df[df["trasferta"]==tras]
            print("\n\n",casa," - ",tras)
            dict_HT  = {}
            dict_2T = {}
            dict_HT["1+"]=0
            dict_HT["2+"]=0
            dict_HT["1-"]=0
            dict_HT["2-"]=0
            dict_2T["1+"]=0
            dict_2T["2+"]=0
            dict_2T["1-"]=0
            dict_2T["2-"]=0
            
            
            gg_ht_casa, ng_ht_casa = gg_ng_ht(dfcasa)
            gg_ht_tras, ng_ht_tras = gg_ng_ht(dftras)
            somma = gg_ht_casa+ng_ht_casa+gg_ht_tras+ng_ht_tras
            gg_ht = (gg_ht_casa+gg_ht_tras)/somma
            ng_ht = (ng_ht_casa+ng_ht_tras)/somma
            
            gg_2t_casa, ng_2t_casa = gg_ng_2t(dfcasa)
            gg_2t_tras, ng_2t_tras = gg_ng_2t(dftras)
            somma = gg_2t_casa+ng_2t_casa+gg_2t_tras+ng_2t_tras
            gg_2t = (gg_2t_casa+gg_2t_tras)/somma
            ng_2t = (ng_2t_casa+ng_2t_tras)/somma
            if gg_ht>threshold:
                print("GG HT con prob: ",round(gg_ht,2))
            if ng_ht>threshold:
                print("NG HT con prob: ",round(ng_ht,2))
            if gg_2t>threshold:
                print("GG 2T con prob: ",round(gg_2t,2))
            if ng_2t>threshold:
                print("NG 2T con prob: ",round(ng_2t,2))
                
            for col in cols:
                somma = 0
                conteggiocas,_ = wordcount(list(dfcasa[col]),col)
                conteggiocas = {k: v for k, v in sorted(conteggiocas.items(), key=lambda item: item[1], reverse=True)} #key sorting by descending order of values
                summ = sum(conteggiocas.values())
                somma = somma + summ
                
                if col=="somma gol HT":
                    for key in conteggiocas:
                        if int(key)>0:
                            dict_HT["1+"] = dict_HT["1+"]+ int(conteggiocas[key])
                        if int(key)<2:
                            dict_HT["1-"] = dict_HT["1-"]+ int(conteggiocas[key])
                        if int(key)>1:
                            dict_HT["2+"] = dict_HT["2+"]+ int(conteggiocas[key])
                        if int(key)<3:
                            dict_HT["2-"] = dict_HT["2-"]+ int(conteggiocas[key])
                if col=="somma gol 2T":
                    for key in conteggiocas:
                        if int(key)>0:
                            dict_2T["1+"] = dict_2T["1+"]+ int(conteggiocas[key])
                        if int(key)<2:
                            dict_2T["1-"] = dict_2T["1-"]+ int(conteggiocas[key])
                        if int(key)>1:
                            dict_2T["2+"] = dict_2T["2+"]+ int(conteggiocas[key])
                        if int(key)<3:
                            dict_2T["2-"] = dict_2T["2-"]+ int(conteggiocas[key])
            
                for key in conteggiocas:
                    conteggiocas[key] = round(conteggiocas[key]/summ,3)
                conteggiotras,_ = wordcount(list(dftras[col]),col)
                conteggiotras = {k: v for k, v in sorted(conteggiotras.items(), key=lambda item: item[1], reverse=True)} #key sorting by descending order of values
                summ = sum(conteggiotras.values())
                somma = somma+summ
                if col=="somma gol HT":
                    for key in conteggiotras:
                        if int(key)>0:
                            dict_HT["1+"] = dict_HT["1+"]+ int(conteggiotras[key])
                        if int(key)<2:
                            dict_HT["1-"] = dict_HT["1-"]+ int(conteggiotras[key])
                        if int(key)>1:
                            dict_HT["2+"] = dict_HT["2+"]+ int(conteggiotras[key])
                        if int(key)<3:
                            dict_HT["2-"] = dict_HT["2-"]+ int(conteggiotras[key])
                if col=="somma gol 2T":
                    for key in conteggiotras:
                        if int(key)>0:
                            dict_2T["1+"] = dict_2T["1+"]+ int(conteggiotras[key])
                        if int(key)<2:
                            dict_2T["1-"] = dict_2T["1-"]+ int(conteggiotras[key])
                        if int(key)>1:
                            dict_2T["2+"] = dict_2T["2+"]+ int(conteggiotras[key])
                        if int(key)<3:
                            dict_2T["2-"] = dict_2T["2-"]+ int(conteggiotras[key])
                    
                for key in conteggiotras:
                    conteggiotras[key] = round(conteggiotras[key]/summ,3)
                
                for key1 in conteggiocas:
                    for key2 in conteggiotras:
                        if key1==key2:
                            if conteggiocas[key1]*conteggiotras[key2]>0.85:
                                a=0
                                print("tipo: ",col," esito: ",key1, " con probabilita' ",round(conteggiocas[key1]*conteggiotras[key2],3))
            
                if col=="somma gol HT":
                    for key in dict_HT:
                        if dict_HT[key]/somma>0.85:
                            a=0
                            print("tipo: und/ov HT"," esito: ",key," con probabilita' ",round(dict_HT[key]/somma,3))
                            
                if col=="somma gol 2T":
                    for key in dict_2T:
                        if dict_2T[key]/somma>0.85:
                            a=0
                            print("tipo: und/ov 2T"," esito: ",key," con probabilita' ",round(dict_2T[key]/somma,3))
                    
        
                if col=="somma gol 2T":
                    for key1 in dict_HT:
                        for key2 in dict_2T:
                            if (dict_HT[key1]/somma)*(dict_2T[key2]/somma)>0.85:
                                a=0
                                print(key1,"&",key2," ",round((dict_HT[key1]/somma)*(dict_2T[key2]/somma),2))
                            
                
                
                
        
                
                
            
                
                
        
        
        
        
        
        
        
        
        
        cols = self.df.columns[2:]
        
        casa = list(self.df2["Column2"]) #get teams that will play at home
        tras = list(self.df2["Column4"]) #get teams that will play away
        
        for i in range(len(casa)):
            game_interesting(casa[i],tras[i], self.df, cols, self.threshold)
        
        
        

pre = input("inserisci il path del file csv appena salvato da excel: ")
post = input("inserisci il path del file csv, output di excel to db: ")
last = input("inserisci l'indice dell'ultima partita giocata: ")
thre = input("inserisci la soglia di probabilita' per l'output, consigliata 0.85: ")

stats(pre,post,last,thre).calc()