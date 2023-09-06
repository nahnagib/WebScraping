from bs4 import BeautifulSoup 
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text , "html")

table = soup.find_all('table')[1]
world_titles = table.find_all('th')
 
world_table_titles = [word.text.strip() for word in world_titles]

import pandas as pd
df = pd.DataFrame( columns=world_table_titles)

table_data = table.find_all('tr')

for row in table_data[1:]:
    row_data = row.find_all('td')
    singel_row_data = [data.text.strip() for data in row_data ]
    length = len(df)
    df.loc[length] = singel_row_data

df.to_csv(r'/Users/nahlaburweiss/Desktop/Data Analysis/OutPut/Compnies.csv' , index=False)