# EU_countries_from_wiki

Data analysis of webscrapped EU countries dataset in terms of Area and Population

## Requirements

This code is using following libraries:
Pandas, matplotlib, BeautifulSoup4 (bs4), requests, and unidecode.

All of which can be installed with:
```
pip install pandas matplotlib bs4 requests unidecode
```

## Description

Code provided can be run from main file. It make use of Data_processing and Data_visualization files containing functions performing all neccesary operations

Dataset used was obtained from:
https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe#UN_member_states_and_UNGA_non-member_observer_state

- Main - responsible for running a script
- Data_processing - responsible for webscraping, edition and saving dataset to csv file
- Data_visualization - responsible for creating a plots to visualize data from csv file
