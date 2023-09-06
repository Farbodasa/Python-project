#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Economics

import pandas
import numpy
import matplotlib.pyplot as plt

def highest_grossing_company(df):
    return df.groupby('company')['price'].sum()

def plot_pie_highest_sharing_company(df):
    df1 = df.groupby('company').size()/len(df)*100
    company = list(set(df['company']))
    percents = list(df1)
    #Edit Colors' List as Desired
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'pink', 'red',
              'yellow', 'magenta', 'green', 'orange', 'purple', '0.65']
    #Edit Radius as Desired
    patches, texts = plt.pie(percents, colors=colors, startangle=90, radius=2.5)
    #Creating Legend
    labels = ['{0} - {1:1.2f} %'.format(i,j) for i,j in zip(company, percents)]
    plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.),
           fontsize=10)
    plt.axis('equal')
    #Edit Chart Name Here
    plt.title('Flight Share(Percent)')
    plt.show()
    
def plot_pie_highest_grossing_company(df):
    df1 = df
    df1 = df1.groupby('company')['price'].sum()
    company = list(set(df['company']))
    for i in range(len(company)):
        company[i] = str(company[i])
    income = list(df1)
    plt.xlabel('Company')
    plt.ylabel('Income')
    #Colors
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'pink', 'red',
              'yellow', 'magenta', 'green', 'orange', 'purple', '0.65']
    #Creating Legend
    labels = ['{0} - {1:1.2f}'.format(i,j) for i,j in zip(company, income)]
    patches ,texts = plt.pie(df1, colors=colors, startangle=90, radius=1)
    plt.legend(patches, labels, bbox_to_anchor=(-0.1, 1.),
           fontsize=10)
    #Edit Chart Title Here
    plt.title('Company Income(USD)')
    plt.show()

def plot_bar_highest_grossing_company(df):
    df1 = highest_grossing_company(df)
    company = list(df1._index)
    for i in range(len(company)):
        company[i] = str(company[i])
    income = list(df1)
    plt.xlabel('Company')
    plt.ylabel('Income')
    #Creating Legend
    labels = ['{0} - {1:1.2f}'.format(i,j) for i,j in zip(company, income)]
    patches = plt.bar(company, income)
    plt.legend(patches, labels, loc='left center', bbox_to_anchor=(-0.1, 1.), fontsize=10)
    #Edit Chart Title Here
    plt.title('Company Income')
    plt.show()
    