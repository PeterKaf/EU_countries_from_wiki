"""
This code is responsible for webscraping wiki page about EU territories, normalizing its dataframe and saving it into
the csv files for further operations
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import re
import unidecode

# Set the URL and file name for the saved HTML content
url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe"
filename = "europe_states.html"

# Check if the file exists
if os.path.isfile(filename):
    print("Found file in directory, opening it now")
    # If the file exists, read the HTML content from the file
    with open(filename, "r") as f:
        html = f.read()
else:
    # If the file doesn't exist, make a request to the URL and save the HTML content to the file
    print("No file found in directory, downloading one from wiki")

    html = requests.get(url).content
    with open(filename, "wb") as f:
        f.write(html)

# Create a soup object from the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find the table(s) on the page and convert to a Pandas DataFrame
table_tags = soup.find_all('table', class_='wikitable sortable')
df = pd.read_html(str(table_tags))[0]

# Set pandas display option to show all columns
pd.set_option('display.max_columns', None)

# Drop unnecessary columns
df_short = df.drop(columns=['Flag', 'Map', 'Domestic short and formal name(s)[16][17][18]'])
"""
# Display new DataFrame
print(df_short)
print(df_short.columns)
"""

# Rename columns
df_short = df_short.rename(columns={'English short, formal names, and ISO[16][17][18][19]': 'Country',
                                    'Capital[19][20][21]': 'Capital', 'Population 2021[22][23]': 'Population',
                                    'Area[a][24]': 'Area', 'Currency[19]': 'Currency'})
# Regex patterns
country_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?<!ISL)'
capital_pattern = r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?=[^a-z]|$)'
area_pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d+)?\s+km2'

# Replace country column data with just its name
df_short['Country'] = df_short['Country'].apply(
    lambda x: re.search(country_pattern, x).group(0) if re.search(country_pattern, x) else None)

# Normilize Capitals for unicode
df_short['Capital'] = df_short['Capital'].apply(
    lambda x: unidecode.unidecode(x) if x else None)

# Replace capital column data with just its name
df_short['Capital'] = df_short['Capital'].apply(
    lambda x: re.search(capital_pattern, x).group(0) if re.search(capital_pattern, x) else None)

# Replace Area column data so it contains just km2 values
df_short['Area'] = df_short['Area'].apply(
    lambda x: re.search(area_pattern, x).group(0) if re.search(area_pattern, x) else None)

print(df_short.columns)
print(df_short)

# Save dataframe into csv file:
try:
    df_short.to_csv('EU_countries.csv', index=True)
    print('Dataframe saved to EU_countries.csv')
except Exception as e:
    print(f'Error saving dataframe to csv file: {str(e)}')
