import pandas as pd 
from datetime import datetime


weekdays = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
data = pd.read_csv('./data/Crime_Reports.csv')

data['year'] = data['Occurred Date'].str[-4:]

data = data.loc[data['year'] >= str(2010),]

data['month'] = data['Occurred Date'].str[:2]


databyyear = data.groupby('year')

pd.DataFrame(databyyear.size()).to_csv('./data/crimes_by_year.csv')


datano2021 = data.loc[data['year'] < str(2021),]

crimebymonthyear = datano2021.groupby(['month','year'],as_index = False).size()
cbm = crimebymonthyear.groupby('month',as_index=False)
cbm.mean() #to csv this

datano2021['day'] = pd.to_datetime(datano2021['Occurred Date'])

datano2021['day'] = datano2021['day'].apply(lambda x: weekdays[x.weekday()])


crimes_by_day = datano2021.groupby(['day','year'],as_index=False)
cbd = crimes_by_day.size()

a = cbd.groupby('day',as_index = False)
a.mean() # to csv this


dbyarea = datano2021.groupby(["Zip Code", "day"])
dbyarea.size().to_csv('./data/crimebyareaday.csv')