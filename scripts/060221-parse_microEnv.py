import pandas as pd
import numpy as np
import os

def get_microEnv():
    #get Data
    d = '/home/kenneth/proj/repodox/data/listOfMicroEnv_sup.tsv'
    df = pd.read_csv(d,sep="\t",header=0)
    return(df)

#main function controls everyone
def main():
    df = get_microEnv() 
    print(df)
    exit()
    dfPDB = pd.read_excel('/home/kenneth/proj/repodox/data/redox_modules_onPDB.xls')
    dfCofPDB = pd.read_excel('/home/kenneth/proj/repodox/data/redox_modules_onCofactorPDB.xls')
    print(dfCofPDB['module'])
    exit()
    print(df[(df.module == 85) & (df.ec != '-.-.-.-')])
    # print(df1['ID'][0:20])
    # print(df1[df1['ID'] == '85'])
    # .sort_values(by='count',ascending=False))
main()