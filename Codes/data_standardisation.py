#Fundumental of Programing Project
#by Aryan Ahadinia, Farbod Asareh, Roxana KhabbazZadeh Moghaddam (Alphabetical)
#Data Standardisation

import pandas
import numpy
import matplotlib.pyplot as plt
import datetime

def int_weekday(x):
    return datetime.date(x // 10000, (x // 100) % 100, x % 100).weekday()

def standardisation(df):
    #removing duplicates entries
    df.drop_duplicates(keep = False, inplace = True)
    #removing false entries
    ##ID
    df = df[df.id != 0]
    df = df[df.id.notnull()]
    ##User ID
    df = df[df.user_id != 0]
    df = df[df.user_id.notnull()]
    ##Request Date ID
    df = df[df.request_date_id != 0]
    df = df[df.request_date_id.notnull()]
    ##Request Time
    df = df[df.request_time != 0]
    df = df[df.request_time.notnull()]
    ##Departure Date ID
    df = df[df.departure_date_id != 0]
    df = df[df.departure_date_id.notnull()]
    ##Departure Time ID
    df = df[df.departure_time_id != 0]
    df = df[df.departure_time_id.notnull()]
    df.dtypes
    ##Company
    df = df[df.company != 0]
    df = df[df.company.notnull()]
    ##Source
    df = df[df.source != 0]
    df = df[df.source.notnull()]
    ##Destination
    df = df[df.destination != 0]
    df = df[df.destination.notnull()]
    ##Price
    df = df[df.price != 0]
    df = df[df.price.notnull()]
    #type correction
    #reindexing
    df.reset_index(drop = True, inplace = True)
    df.id = df.id.astype('int')
    df.user_id = df.user_id.astype('int')
    df.request_date_id = df.request_date_id.astype('int')
    df.departure_date_id = df.departure_date_id.astype('int')
    df.company = df.company.astype('int')
    df.source = df.source.astype('int')
    df.destination = df.destination.astype('int')
    #request_time type correction
    if type(df['request_time'][0]) != type(datetime.time(0, 0, 0)):
        df.request_time = df.request_time.astype('int')
        t = []
        for i in range(len(df)):
            t.append(datetime.time(df['request_time'][i] // 100, df['request_time'][i] % 100))
        df['request_times'] = t
    #request_time type correction
    if type(df['departure_time_id'][0]) != type(datetime.time(0, 0, 0)):
        df.departure_time_id = df.departure_time_id.astype('int')
        t = []
        for i in range(len(df)):
            t.append(datetime.time(df['departure_time_id'][i] // 100, df['departure_time_id'][i] % 100))
        df['departure_time_id'] = t  
    #request hour finding
    h = []
    for i in range(len(df)):
        h.append(df['request_time'][i].hour)
    df['request_hour'] = h
    df.request_hour = df.request_hour.astype('int8')
    #departure hour finding
    h = []
    for i in range(len(df)):
        h.append(df['departure_time_id'][i].hour)
    df['departure_hour'] = h
    df.departure_hour = df.departure_hour.astype('int8')
    #request month finding
    df['request_month'] = (df['request_date_id'] // 100) % 100
    #departure month finding
    df['departure_month'] = (df['departure_date_id'] // 100) % 100
    #request weekday finding
    w = []
    for i in range(len(df)):
        w.append(int_weekday(int(df['request_date_id'][i])))
    df['request_weekday'] = w
    df.request_weekday = df.request_weekday.astype('int8')
    #departure weekday finding
    w = []
    for i in range(len(df)):
        w.append(int_weekday(int(df['departure_date_id'][i])))
    df['departure_weekday'] = w
    df.departure_weekday = df.departure_weekday.astype('int8')
    #diffrence finding
    d = []
    for i in range(len(df)):
        d.append((datetime.date(df['departure_date_id'][i] // 10000, (df['departure_date_id'][i] // 100) % 100, df['departure_date_id'][i] % 100) - datetime.date(df['request_date_id'][i] // 10000, (df['request_date_id'][i] // 100) % 100, df['request_date_id'][i] % 100)).days)
    df['difference'] = d
    df = df[df.difference >= 0]
    #reindexing
    df.reset_index(drop = True, inplace = True)
    return df