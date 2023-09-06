#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Dependence Analisys

import pandas
import numpy
import matplotlib.pyplot as plt

def weekday_sell(df):
    return df.groupby(['request_weekday']).size()

def plot_weekday_sell(df):
    dfm = weekday_sell(df)
    dfm.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Weekdays')
    plt.xlabel('Weekdays')
    plt.ylabel('Count')
    plt.show()

def weekday_departure(df):
    return df.groupby(['departure_weekday']).size()

def plot_weekday_departure(df):
    dfw = weekday_departure(df)
    dfw.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Days')
    plt.xlabel('Days')
    plt.ylabel('Count')
    plt.show()

def hour_sell(df):
    return df.groupby(['request_hour']).size()

def plot_hour_sell(df):
    dfm = hour_sell(df)
    dfm.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Hours')
    plt.xlabel('Hours')
    plt.ylabel('Count')
    plt.show()

def hour_departure(df):
    return df.groupby(['departure_hour']).size()

def plot_hour_departure(df):
    dfh = hour_departure(df)
    dfh.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Hours')
    plt.xlabel('Hours')
    plt.ylabel('Count')
    plt.show()

def month_sell(df):
    return df.groupby(['request_month']).size()

def plot_month_sell(df):
    dfm = month_sell(df)
    dfm.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Month')
    plt.xlabel('Months')
    plt.ylabel('Count')
    plt.show()

def month_departure(df):
    return df.groupby(['departure_month']).size()

def plot_month_departure(df):
    dfm = month_departure(df)
    dfm.plot.bar(color="#d60d53")
    plt.title('Number of Flights Per Month')
    plt.xlabel('Months')
    plt.ylabel('Count')
    plt.show()
    