#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Popularity

import pandas
import numpy
import matplotlib.pyplot as plt

def route(df):
    return df.groupby(['source', 'destination']).size()

def chart_dest_per_sourse(df, source):
    df0=df[df['source']==source]
    dft=df0.groupby(['destination'])['source'].count()
    dft.plot.bar()
    plt.title('Flights from source '+str(source))
    plt.show()
    
def chart(df):
    l_source=list(set(df['source']))
    for i in range(len(l_source)):
        chart_dest_per_sourse(df,l_source[i])

def source(df):
    return df.groupby(['source']).size()

def plot_source(df):
    df71 = source(df)
    df71.plot.bar(color='#f0846e')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.show()

def destination(df):
    return df.groupby(['destination']).size()

def plot_destination(df):
    df7 = destination(df)
    df7.plot.bar(color='#61c8d4')
    plt.xlabel('Destination')
    plt.ylabel('Count')
    plt.show()

def company(df):
    return df.groupby('company').size() / len(df) * 100

def company_sale(df):
    return df.groupby(['company'])['price'].sum()

def plot_company_sale(df):
    df4 = company_sale(df)
    df4.plot.bar(color='#80cc06')
    plt.title('Total Sales')
    plt.ylabel('Price')
    plt.show()

def plot_company(df):
    #Feel Free to Edit the Chart's Size After 'figsize'
    company(df).plot(kind='pie', figsize=(11,11), fontsize=12, startangle=90)

def month(df):
    return df.groupby(['departure_month']).size()

def month_amount(df):
    return df.groupby(['departure_month'])['price'].sum()

def plot_month_amount(df):
    df7 = df.groupby(['departure_month'])['price'].sum()
    df7.plot.bar(color='#de31a1')
    plt.xlabel('Companies')
    plt.ylabel('Sale')
    plt.title('mizane forosh dar har mah')
    plt.show()

def company_by_month(df):
    return df.groupby(['company','departure_month']).size()

def company_by_source(df):
    return df.groupby(['company', 'source']).size()

def company_by_destination(df):
    return df.groupby(['company', 'destination']).size()

def airport_plot(df):
    plt.style.use('ggplot')
    df1 = source(df) / len(df) * 100
    df2 = destination(df) / len(df) * 100
    sources = list(set(df['source']))
    source_percent = list(df1)
    dest_percent = list(df2)
    d = {'sources': sources, 'source_percent':source_percent, 'dest_percent': dest_percent}
    d = pandas.DataFrame(d, columns = ['sources', 'source_percent', 'dest_percent'])
    d.plot(x="sources", y=["source_percent", "dest_percent"], kind="bar")
    #Edit Chart Labels Here
    plt.xlabel('Source/Destination')
    plt.ylabel('Share of Flights')
    #Edit Chart Name Here
    plt.title('Source/Destination Popularity(Percent)')
    plt.show()
    
def plot_source_per_company(df):
    l_company=list(set(df['company']))
    for i in range(len(l_company)):
        df0=df[df['company']==l_company[i]]
        dft=df0.groupby(['source'])['source'].count()
        dft.plot.bar(color='#b861fa')
        plt.title('tedad parvaz company '+str(l_company[i]))
        plt.xlabel('Source')
        plt.ylabel('Count')
        plt.show()
     
def plot_destination_per_company(df):
    l_company=list(set(df['company']))
    for i in range(len(l_company)):
        df0=df[df['company']==l_company[i]]
        dft=df0.groupby(['destination'])['destination'].count()
        dft.plot.bar(color='#b7e36f')
        plt.title('tedad parvaz company '+str(l_company[i]))
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.show()