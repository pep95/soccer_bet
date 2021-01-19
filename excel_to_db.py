'''
this class have as goal to read the information of a classic excel db
(with results HT and final results) and generate a new db with a lot
of information like:
- gol casa
- gol trasferta
- 1X2
- gol casa HT
and so on....

@author: giusc
'''

import pandas as pd
import numpy as np

class converter:
    def __init__(self,input_path,output_path,last_element):
        self.input = input_path
        self.output = output_path
        self.last = last_element
    
    def calc(self):
        df = pd.read_csv(self.input,sep=";") #open excel db
        
        ''' creation of a dict that will contain the new informations'''
        dict = {}
        dict["casa"] = []
        dict["trasferta"] = []
        dict["risultato"] = []
        dict["gol casa"] = []
        dict["gol trasferta"] = []
        dict["1X2"] = []
        dict["gol casa HT"] = []
        dict["gol trasferta HT"] = []
        dict["1X2 HT"] = []
        dict["risultato HT"] = []
        dict["gol casa 2T"] = []
        dict["gol trasferta 2T"] = []
        dict["1X2 2T"] = []
        dict["parz/fin"] = []
        dict["ris esatto parz/fin"] = []
        dict["somma gol HT"] = []
        dict["somma gol 2T"] = []
        dict["somma gol totale"] = []
        
        df = df[:self.last] #take from the whole database only the matches already played
        
        '''the for cicle have as goal to get information from existing columns
        and generate more information (new columns) '''
        for row in df.iloc:
            dict["casa"].append(row[1])
            dict["trasferta"].append(row[3])
            
            
            dict["gol casa"].append(int(row[2].split("-")[0]))
            dict["gol trasferta"].append(int(row[2].split("-")[1]))
            dict["risultato"].append(row[2])
            if dict["gol casa"][-1] == dict["gol trasferta"][-1]:
                dict["1X2"].append("X")
            elif dict["gol casa"][-1] > dict["gol trasferta"][-1]:
                dict["1X2"].append("1")
            else:
                dict["1X2"].append("2")
                
            dict["risultato HT"].append(row[4].split("(")[1].split(")")[0])
            dict["gol casa HT"].append(int(row[4].split("(")[1].split("-")[0]))
            dict["gol trasferta HT"].append(int(row[4].split("(")[1].split("-")[1].split(")")[0]))
            if dict["gol casa HT"][-1] ==  dict["gol trasferta HT"][-1]:
                dict["1X2 HT"].append("X")
            elif dict["gol casa HT"][-1] >  dict["gol trasferta HT"][-1]:
                dict["1X2 HT"].append("1")
            else:
                dict["1X2 HT"].append("2")
            
            dict["gol casa 2T"].append(dict["gol casa"][-1]-dict["gol casa HT"][-1])
            dict["gol trasferta 2T"].append(dict["gol trasferta"][-1]-dict["gol trasferta HT"][-1])
            if dict["gol casa 2T"][-1] ==  dict["gol trasferta 2T"][-1]:
                dict["1X2 2T"].append("X")
            elif dict["gol casa 2T"][-1] >  dict["gol trasferta 2T"][-1]:
                dict["1X2 2T"].append("1")
            else:
                dict["1X2 2T"].append("2")
                
            dict["parz/fin"].append(str(dict["1X2 HT"][-1])+"/"+str(dict["1X2"][-1]))
            dict["ris esatto parz/fin"].append(str(dict["risultato HT"][-1])+"/"+str(dict["risultato"][-1]))
            dict["somma gol HT"].append(int(dict["gol casa HT"][-1]+dict["gol trasferta HT"][-1]))
            dict["somma gol 2T"].append(int(dict["gol casa 2T"][-1]+dict["gol trasferta 2T"][-1]))
            dict["somma gol totale"].append(int(dict["gol casa"][-1]+dict["gol trasferta"][-1]))
        
        '''creation of a pandas dataframe from dict and df storage'''
        new_df = pd.DataFrame(data=dict)
        new_df.to_csv(self.output)
        print(new_df)

inp = input("inserisci il path del file csv appena salvato da excel: ")
out = input("inserisci il path del file csv di output: ")
last = input("inserisci l'indice dell'ultima partita giocata: ")
converter(inp,out,last).calc()