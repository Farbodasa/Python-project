#Unprossecced Codes

def plot_company_sale_month(df):
    l_company=list(set(df['company']))
    for n in range(len(l_company)):
        df1=df[df['company']==l_company[n]]
        df2=df1.groupby(['departure_month'])['price'].mean()
        df2.plot.bar(color='#fcba03')
        plt.title('Foroshe company '+str(l_company[n])+' dar har mah')
        plt.xlabel('Month')
        plt.show()

#foorooshe har company

def chart_source_per_month(df):
    l_source=list(set(df['source']))
    for i in range(len(l_source)):
        df0=df[df['source']==l_source[i]]
        dft=df0.groupby(['departure_month'])['source'].count()
        dft.plot.bar()
        plt.title('tedad parvaz az mabda '+str(l_source[i]))
        plt.xlabel('month')
        plt.ylabel('Number')
        plt.show()

    
    
############################## 
def chart_destination_per_month(df):
    l_destination=list(set(df['destination']))
    for i in range(len(l_destination)):
        df0=df[df['destination']==l_destination[i]]
        dft=df0.groupby(['departure_month'])['destination'].count()
        dft.plot.bar(color='#6b1180')
        plt.title('tedad parvaz be maqsad '+str(l_destination[i]))
        plt.xlabel('Month')
        plt.ylabel('Number')
        plt.show()

####################################
#mizane forosh dar har mah




def chart_destination_per_source(df):
    l_source=list(set(df['source']))
    for i in range(len(l_source)):
        df0=df[df['source']==l_source[i]]
        dft=df0.groupby(['destination'])['source'].count()
        dft.plot.bar()
        plt.title('tedad parvaz az mabda '+str(l_source[i]))
        plt.xlabel('Destination')
        plt.ylabel('Count')
        plt.show()


######################################