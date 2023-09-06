#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)

import pandas
import matplotlib.pyplot as plt

import frequent_flyer_program
import data_standardisation
import popularity
import economics
import dependence_analisys
import difference_analisys


df = pandas.read_excel('C:/Users/aryan/Desktop/FlightSales.xlsx')
df = data_standardisation.standardisation(df)
df.to_excel('C:/Users/aryan/Desktop/complex.xlsx')
df.to_csv('C:/Users/aryan/Desktop/complex.csv')

#part 1
print(frequent_flyer_program.purchase_userID(df).mean())
frequent_flyer_program.normal_distribiution(df)

#part 2
frequent_flyer_program.reward(df)
print(frequent_flyer_program.customer_reward(df))
df1 = frequent_flyer_program.customer_club(df,10000, 30000, 100000)
df1.to_excel('C:/Users/aryan/Desktop/customerclub.xlsx')
df1.to_csv('C:/Users/aryan/Desktop/customerclub.csv')
frequent_flyer_program.club_chart(df1)

#part 3
dependence_analisys.plot_hour_sell(df)
dependence_analisys.plot_weekday_sell(df)
dependence_analisys.plot_month_sell(df)

#part 4
difference_analisys.plot_month(df)

#part 5
df5 = popularity.route(df)
df5.to_frame().to_excel('C:/Users/aryan/Desktop/route.xlsx')
df5.to_frame().to_csv('C:/Users/aryan/Desktop/route.csv')
popularity.airport_plot(df)

#part 6
df6 = economics.highest_grossing_company(df)
df6.to_frame().to_excel('C:/Users/aryan/Desktop/company_grossment.xlsx')
df6.to_frame().to_csv('C:/Users/aryan/Desktop/company_grossment.csv')
economics.plot_pie_highest_sharing_company(df)
economics.plot_pie_highest_grossing_company(df)
economics.plot_bar_highest_grossing_company(df)

#question 1
difference_analisys.plot_company(df)

#question 2
dependence_analisys.plot_hour_departure(df)
dependence_analisys.plot_weekday_departure(df)
dependence_analisys.plot_month_departure(df)

#others
popularity.plot_source(df)
popularity.plot_destination(df)
popularity.plot_source_per_company(df)
popularity.plot_destination_per_company(df)
difference_analisys.timedelta_per_company(df)
popularity.plot_month_amount(df)
