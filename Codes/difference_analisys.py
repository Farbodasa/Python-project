#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Difference Analisys

import pandas
import numpy
import matplotlib.pyplot as plt

def plot_month(df):
    (df.groupby(['departure_month'])['difference'].mean()).plot.bar()
    plt.title('Average Request Time and Flight Time Difference')
    plt.xlabel('Companies')
    plt.ylabel('Days')
    plt.show()
    
def plot_company(df):
    (df.groupby(['company'])['difference'].mean()).plot.bar()
    plt.title('Average Request Time and Flight Time Difference')
    plt.xlabel('Companies')
    plt.ylabel('Days')
    plt.show()
    
def timedelta_per_company(df):
    df9=df.groupby(['company'])['difference'].mean()
    df9.plot.bar(color='#8f1a4e')
    plt.title('Average Request Time and Flight Time Difference')
    plt.xlabel('company')
    plt.ylabel('Days')
    plt.show()