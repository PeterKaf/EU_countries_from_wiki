"""
This code is responsible for webscraping wiki page about EU territories, normalizing its dataframe and saving it into
the csv files for further operations
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import unidecode


def read_html_file(url, filename):
    # Check if the file exists
    try:
        with open(filename, "r") as f:
            html = f.read()
    except FileNotFoundError:
        # If the file doesn't exist, make a request to the URL and save the HTML content to the file
        print("No file found in directory, downloading one from wiki")
        html = requests.get(url).content
        with open(filename, "wb") as f:
            f.write(html)
        # read from the newly created file
        with open(filename, "r") as f:
            html = f.read()
    return html


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_tags = soup.find_all('table', class_='wikitable sortable')
    df = pd.read_html(str(table_tags))[0]
    return df


def normalize_dataframe(df):
    # Drop unnecessary columns
    df = df.drop(columns=['Flag', 'Map', 'Domestic short and formal name(s)[16][17][18]'])

    # Rename columns
    df = df.rename(columns={'English short, formal names, and ISO[16][17][18][19]': 'Country',
                            'Capital[19][20][21]': 'Capital', 'Population 2021[22][23]': 'Population',
                            'Area[a][24]': 'Area [km2]', 'Currency[19]': 'Currency'})

    # Regex patterns
    country_pattern = r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?<!ISL)'
    capital_pattern = r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?=[^a-z]|$)'
    area_pattern = r'\d{1,3}(?:,\d{3})*(?:\.\d+)?\s'

    # Replace country column data with just its name
    df['Country'] = df['Country'].apply(
        lambda x: re.search(country_pattern, x).group(0) if re.search(country_pattern, x) else None)

    # Normilize Capitals for unicode
    df['Capital'] = df['Capital'].apply(
        lambda x: unidecode.unidecode(x) if x else None)

    # Replace capital column data with just its name
    df['Capital'] = df['Capital'].apply(
        lambda x: re.search(capital_pattern, x).group(0) if re.search(capital_pattern, x) else None)

    # Replace Area column data so it contains just km2 values
    df['Area [km2]'] = df['Area [km2]'].apply(
        lambda x: re.search(area_pattern, x).group(0) if re.search(area_pattern, x) else None)
    df['Area [km2]'] = df['Area [km2]'].str.replace(r'[^0-9.]', '').astype(float)

    return df


def save_to_csv(df, filename):
    try:
        df.to_csv(filename, index=True)
        print(f'Dataframe saved to {filename}')
    except Exception as e:
        print(f'Error saving dataframe to csv file: {str(e)}')
