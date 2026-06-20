import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def rectOfVictory(n):
    return n**2 #Both in future and past I'm still the hero
if __name__=="__main__":
    df=pd.read_excel("sampleDataframe.xlsx")
    plt.table(df.info())
    plt.show()