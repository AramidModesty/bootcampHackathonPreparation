import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def funcionCuadrado(n):
    return n**2
def limpiarDf(df:pd.DataFrame):
    df_limp=df.dropna(axis=1,thresh=0.1)
    #thresh: Limite de porcentaje permitido de nulos por columna
    df_limp.dropna()
    df_limp.drop_duplicates()
    return df_limp
def limpiarTiemposDf(df_limp,column,limInf,limSup):
    df_limp.at_time(pd.date_range(start=limInf,end=limSup))
    return df_limp
if __name__=="__main__":
    df=pd.read_excel("sampleDataframe.xlsx")
    print(df.info())
    print(df)
    df_limp=limpiarDf(df)
    print(df_limp.info())
    print(df_limp)