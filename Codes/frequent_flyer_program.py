#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Frequent_Flyer Program

import pandas
import numpy
import matplotlib.pyplot as plt

def purchase_userID(df):
    return df.groupby(['user_id'])['price'].sum()

def count_userID(df):
    return df.groupby(['user_id'])['price'].count()

def normal_distribiution(df):
    df1=df.groupby(['user_id'])['price'].mean()
    df1=list(df1)
    y,x,_ = plt.hist(df1,150,color='#9c2abf')
    plt.xlabel('Average Purchase')
    plt.ylabel('Count')
    plt.title('Average Purchase Normal Distribution',fontsize=14)
    plt.show()

def reward(df):
    df['reward'] = df['price'] // 100 * 500
    
def customer_reward(df):
    return df.groupby(['user_id'])['reward'].sum().astype('int')

def customer_club(df, silver_min_rew, gold_min_rew, platinium_min_rew):
    reward(df)
    ds = customer_reward(df)
    s = ds >= silver_min_rew
    s = s.astype('int')
    g = ds >= gold_min_rew
    g = g.astype('int')
    p = ds >= platinium_min_rew
    p = p.astype('int')
    ds = ds.to_frame()
    ds['level'] = s + g + p
    return ds

def club_chart(ds):
    ds1=ds.groupby(['level'])['level'].count()
    new_index=['Bronze','Silver','Gold','Platinum']
    ds1=list(ds1)
    plt.bar(new_index,ds1)
    plt.title('Customer Club')
    plt.ylabel('Count')
    patches = plt.bar(new_index, ds1)
    labels = ['{0} - {1:1.2f}'.format(i,j) for i,j in zip(new_index, ds1)]
    plt.legend(patches, labels, loc = 'left center', bbox_to_anchor = (-0.1, 1.), fontsize = 10)
    plt.show()