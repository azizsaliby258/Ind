# Import Libraries 
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.figure_factory as ff
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# Setting a title for the streamlit app
st.title('Suicide')

# Setting a small introduction on the suicide topic
st.caption("From a long time suicide it's been a major problem for NGOs and governments since it is considered as taboo and didn't get the attention it deserves. But it is really important to study the trend of this problem to get insights about: where we should launch prevention campaign, in which country, the target population and many more.")

# Loading the Data
st.header("First of all lets take a clear view on the Datframe that we have")
data = pd.read_csv("master.csv")
print(data)
st.write(data)

# printing general informations about our data
data.info()

# Checking for missing data in the columns
data.isnull().sum()

# Dropping the column that contains missing value
data.drop("HDI for year",axis=1,inplace=True)

# Dividing the data into 2 subcategory, data that contains all the information on males and the other on females
data_men = data[data.sex == "male"]
data_women = data[data.sex == "female"]

#Now our data is clean and splitted and ready for the EDA part

# Pie Chart 
# The most important question Who commit suicides more males or females
st.header(" Who commit Suicides more? females or males?")

# To answer this question i plotted a pie chart to see the number that committed suicides
plt.pie([data_men["suicides_no"].sum(),data_women["suicides_no"].sum() ], labels= [' Percentage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men["suicides_no"].sum(),data_women["suicides_no"].sum()], title='%/number of suicides committed from 1987 to 2016 across gender')])
st.plotly_chart(fig)
st.caption("As clear in the Boxplots Man tend to suicide 3.3 more times higher than females")

# Same Plot for all countries 
st.subheader("What if we want to know the percentage in a specific country")

option = st.selectbox(
     'Select Please your Specific country',
     ('Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'Finland', 'France' ,'Georgia', 'Germany' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States', 'Uruguay',
 'Uzbekistan'))

st.write('You selected:', option)

datacountry1 = data[data["country"]==option]

data_men1 = datacountry1[data.sex == "male"]
data_women1 = datacountry1[data.sex == "female"]

plt.pie([data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum() ], labels= ['Percantage of men that commited suicides', 'Percentage of women that commited suiced'], autopct='%1.1f%%')
fig= go.Figure(data=[go.Pie(labels=['Males', 'Females'], values=[data_men1["suicides_no"].sum(),data_women1["suicides_no"].sum()], title='Number of Suicides committed by males and females since 1985 till 2016')])
st.plotly_chart(fig)


#Lets Take a look on the trend of suicides in the world.
total_gender = data[['sex', 'suicides_no', 'population', 'year', 'country']]
total_gender['proportion'] = total_gender.suicides_no / total_gender.population
gender_prop = pd.DataFrame(total_gender.groupby(['year', 'sex'])['proportion'].mean()).unstack()
fig = go.Figure()

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.male,
                         mode = 'lines+markers',
                         name = 'Male death ',
                         marker = dict(color='#FF9900')))

fig.add_trace(go.Scatter(x= gender_prop.index,
                         y = gender_prop.proportion.female,
                         mode = 'lines+markers',
                         name = 'Female death',
                         marker = dict(color='rgb(179,222,105)')))

fig.update_layout(height=500, width=900,
                  title = 'Trend of suicides across gender throught the years from 1985 till 2015',
                  font = dict(color="black"))

fig.update_xaxes(title_text = 'Year', color="RebeccaPurple")
fig.update_yaxes(title_text = 'Proportion', color="RebeccaPurple")
st.plotly_chart(fig)

#The Trend of suicides in specific country.
gog =  st.selectbox(
     'Select Please your Specific country',
     ('Armenia','Albania', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'Finland', 'France' ,'Georgia', 'Germany' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States', 'Uruguay'))

datacountry2 = data[data["country"]==gog]

data_men2 = datacountry2[data.sex == "male"]
data_women2 = datacountry2[data.sex == "female"]

fig = plt.figure(figsize=(10, 4))
sns.lineplot(x = data_men2.year, y = data_men2['suicides/100k pop'], data= datacountry2,hue="sex")
sns.lineplot(x = data_women2.year, y = data_women2['suicides/100k pop'], data= datacountry2)
st.pyplot(fig)

st.caption("As seen in the first graph the world record the highest rate of suicides in 1995 and after this year it take a negative trend, in other words it begans to decrease")
st.caption("After doing some extra research to understand why this year have the highest rate of suicides across the world, I found that many bad events hitted different countries in this time for example:Barings Bank collapsed in the UK,Oklahoma City Bombing,Aum Shinrikyo gassed and the Serbs rounded up and killed an estimated 8,000 men and boys...etc")
st.caption("We can conclude that Economic Crises, war, genocides... can lead to mental health disorders which increase the percentage for people to commit suicide")
st.caption("To validate this point of vue lets see if the GDP pf the country has an impact on suicide number ")

# plotting a graph to visualize if the gdp has an efect on the suicide number.
st.header("Does the GDP per capita affect the number of suicides committed in a certain country?")
gog1 =  st.selectbox(
     'Select Please your Specific country',
     ('Finland','Germany','Armenia','Albania', 'Antigua and Barbuda', 'Argentina', 'Aruba', 'Australia',
 'Austria' ,'Azerbaijan' ,'Bahamas', 'Bahrain' ,'Barbados', 'Belarus', 'Belgium',
 'Belize' ,'Bosnia and Herzegovina' ,'Brazil', 'Bulgaria' ,'Cabo Verde',
 'Canada' ,'Chile', 'Colombia' ,'Costa Rica', 'Croatia', 'Cuba', 'Cyprus',
 'Czech Republic', 'Denmark' ,'Dominica', 'Ecuador', 'El Salvador', 'Estonia'
 'Fiji', 'France' ,'Georgia' ,'Greece', 'Grenada',
 'Guatemala' ,'Guyana' ,'Hungary' ,'Iceland' ,'Ireland', 'Israel', 'Italy',
 'Jamaica' ,'Japan', 'Kazakhstan' ,'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
 'Lithuania' ,'Luxembourg', 'Macau', 'Maldives', 'Malta', 'Mauritius', 'Mexico',
 'Mongolia', 'Montenegro', 'Netherlands' ,'New Zealand', 'Nicaragua' ,'Norway',
 'Oman' ,'Panama' ,'Paraguay' ,'Philippines', 'Poland', 'Portugal',
 'Puerto Rico', 'Qatar', 'Republic of Korea' ,'Romania', 'Russian Federation',
 'Saint Kitts and Nevis' ,'Saint Lucia', 'Saint Vincent and Grenadines',
 'San Marino', 'Serbia', 'Seychelles', 'Singapore' ,'Slovakia' ,'Slovenia',
 'South Africa', 'Spain', 'Sri Lanka' ,'Suriname' ,'Sweden', 'Switzerland',
 'Thailand' ,'Trinidad and Tobago' ,'Turkey', 'Turkmenistan', 'Ukraine',
 'United Arab Emirates' ,'United Kingdom', 'United States'))

datacountry3 = data[data["country"]==gog1]

f, ax = plt.subplots(1,1, figsize=(10,8))
ax = sns.scatterplot(x="gdp_per_capita ($)", y="suicides_no", data=datacountry3, color='yellow')
st.pyplot(f)

#suicide number across age brackets in the specific chosen country

st.header("What is the average age a person commits suicide?")
title = st.text_input('Country name', 'Germany')
st.write('The country selected is', title)
datacountry3 = data[data["country"]==title]

f,ax=plt.subplots(1,2,figsize=(20,8))
plt.figure(figsize=(10,5))
suicidenoVSgender = sns.barplot(x = 'sex', y = 'suicides_no', hue = 'age',ax=ax[0],data=datacountry3)
suicidenoVSgenerations= sns.barplot(x = 'sex', y = 'suicides_no', hue = 'generation',ax=ax[1],data = datacountry3)
st.pyplot(f)

# Number of suicides/100k pop in all countries (using plotly map)
st.subheader("Rate of suicide committed in the available countries")
geo = data.groupby(by=['country']).agg({"suicides/100k pop": ['sum']})
geo.columns = ['total_suicide']
geo.reset_index(inplace=True)

fig = px.choropleth(geo, locations="country", locationmode='country names',
                    color="total_suicide", 
                    hover_name="country",
                    color_continuous_scale='sunset')

fig.update_layout(
    title="Number of suicides/100k population committed in countries from 1985 till 2015",
    font=dict(
        size=15,)
)
st.plotly_chart(fig)

#Top 10 countries which recored the highest suicides rates across the years
st.subheader("Top 10 Countries with the highest Suicides Rates")

Year = st.slider('Select The year Please', 1987, 2016, 1988)

datayear = data[data["year"]==Year]
f, ax = plt.subplots(1,1, figsize=(10,8))
data_country_total = datayear.groupby(by=['country']).agg({'suicides/100k pop': ['sum']})
data_country_total.columns = ['total_suicide']
data_country_total.reset_index(inplace=True)
data_country_total = data_country_total.sort_values(by=['total_suicide'], ascending=False).head(10)

ax = sns.barplot(x='total_suicide', y='country', data=data_country_total)

plt.title('Top 10 Countries With Highest Number Of Suicides')

st.pyplot(f)

f1, ax1 = plt.subplots(1,1, figsize=(10,8))
data_country_total = datayear.groupby(by=['country']).agg({'suicides/100k pop': ['sum']})
data_country_total.columns = ['total_suicide']
data_country_total.reset_index(inplace=True)
data_country_total = data_country_total.sort_values(by=['total_suicide'], ascending=False).tail(10)

ax1 = sns.barplot(x='total_suicide', y='country', data=data_country_total)

plt.title(' Top 10 Countries With Lowest Number Of Suicides')

st.pyplot(f1)












               




