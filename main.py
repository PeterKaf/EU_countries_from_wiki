import Data_processing as dp
import Data_visualization as dv


def main():
    # Set the URL and file name for the saved HTML content
    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe"
    filename = "europe_states.html"

    # Parse the HTML and normalize the dataframe
    df = dp.parse_html(dp.read_html_file(url, filename))
    df_short = dp.normalize_dataframe(df)

    # Save the dataframe to a CSV file
    dp.save_to_csv(df_short, 'EU_countries.csv')

    # Visualize the data
    dv.plot_population_country(df_short)
    dv.plot_area_country(df_short)


if __name__ == "__main__":
    main()
