"""
sample desc
"""
import matplotlib.pyplot as plt


def plot_population_country(df):
    # Sort the DataFrame by population in descending order
    sorted_df = df.sort_values(by='Population', ascending=False)

    # Split the DataFrame into two parts
    split_index = len(sorted_df) // 2
    large_pop_countries_df = sorted_df[:split_index]
    small_pop_countries_df = sorted_df[split_index:]

    # Create a bar chart for countries with large populations
    fig, ax = plt.subplots()
    ax.bar(large_pop_countries_df['Country'], large_pop_countries_df['Population'], label='Population', color='b')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population')
    ax.set_title('EU countries by population')
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
    ax.set_yscale('log')  # Apply logarithmic scale to y-axis

    plt.tight_layout()
    plt.show()

    # Create a bar chart for countries with small populations
    fig, ax = plt.subplots()
    ax.bar(small_pop_countries_df['Country'], small_pop_countries_df['Population'], label='Population', color='b')
    ax.set_xlabel('Country')
    ax.set_ylabel('Population')
    ax.set_title('EU countries by population')
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
    ax.set_yscale('log')  # Apply logarithmic scale to y-axis

    plt.tight_layout()
    plt.show()


def plot_area_country(df):
    # Sort the DataFrame by area in descending order
    sorted_df = df.sort_values(by='Area [km2]', ascending=False)

    # Split the DataFrame into two parts
    split_index = len(sorted_df) // 2
    large_area_countries_df = sorted_df[:split_index]
    small_area_countries_df = sorted_df[split_index:]

    # Create a bar chart for countries with large areas
    fig, ax = plt.subplots()
    ax.bar(large_area_countries_df['Country'], large_area_countries_df['Area [km2]'], label='Area [km2]',
           color=(0.6, 0, 0))
    ax.set_xlabel('Country')
    ax.set_ylabel('Area [km2]')
    ax.set_title('EU countries by Area')
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
    ax.set_yscale('log')  # Apply logarithmic scale to y-axis

    plt.tight_layout()
    plt.show()

    # Create a bar chart for countries with small areas
    fig, ax = plt.subplots()
    ax.bar(small_area_countries_df['Country'], small_area_countries_df['Area [km2]'], label='Area [km2]',
           color=(0.6, 0, 0))
    ax.set_xlabel('Country')
    ax.set_ylabel('Area [km2]')
    ax.set_title('EU countries by Area')
    ax.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
    ax.set_yscale('log')  # Apply logarithmic scale to y-axis

    plt.tight_layout()
    plt.show()
