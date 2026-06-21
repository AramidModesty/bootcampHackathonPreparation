import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def funcion_cuadrado(n):
    return n**2
def limpiar_df(df:pd.DataFrame):
    df_limp=df.dropna(axis=1,thresh=0.1)
    #thresh: Limite de porcentaje permitido de nulos por columna
    df_limp.dropna()
    df_limp.drop_duplicates()
    return df_limp
def limpiar_tiempos_df(df_limp,column,limInf,limSup):
    df_limp.at_time(pd.date_range(start=limInf,end=limSup))
    return df_limp
def get_dataframe():
    df=pd.read_excel("sampleDataframe.xlsx")
    return df
def graphFun(fun,numxInf,numxSup,nVals=50,title=""):
    arrX=np.linspace(numxInf,numxSup,nVals)
    arrY=fun(arrX)
    print(arrX,arrY)
    plt.plot(arrX,arrY)
    plt.title(title)
    return plt.show()
if __name__=="__main__":
    graphFun(funcion_cuadrado,0,100,10)