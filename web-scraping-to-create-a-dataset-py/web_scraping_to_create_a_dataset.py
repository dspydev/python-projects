!pip install beautifulsoup4
!pip install pandas
!pip install tabulate

import csv
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate

# Constants
WIKI_URL = "https://en.wikipedia.org/wiki/Comparison_of_programming_languages"
CSV_FILE = "prog_lang_comparison.csv"
TABLE_CLASS = "wikitable"

# Function to extract data and store it in a CSV file
def extract_data(url: str, file_name: str) -> None:
    """
    Extract table data from a web page and write it to a CSV file.

    Parameters:
    url (str): The URL of the web page.
    file_name (str): The name of the CSV file to be created.
    """
    try:
        html = urlopen(url)
    except Exception as e:
        print(f"Error accessing URL: {e}")
        return

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"class": TABLE_CLASS})
    if not table:
        print(f"No table found with class '{TABLE_CLASS}' on page {url}")
        return

    rows = table.findAll("tr")
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            cells = row.findAll(["td", "th"])
            writer.writerow([cell.get_text() for cell in cells])
    print(f"Data extracted successfully and stored in file '{file_name}'.")

# Call the function to extract data and store it in a CSV file
extract_data(WIKI_URL, CSV_FILE)

# Read data from the CSV file using the Pandas library
df = pd.read_csv(CSV_FILE)

# Display the number of columns and rows
print(f"The file contains {len(df.columns)} columns and {len(df)} rows.")

# Function to display data as a table
def display_table(df):
    """
    Display the data in a Pandas DataFrame as a formatted table.
    """
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None
    print(tabulate(df, headers='keys', tablefmt='psql'))

# Display column names
print("The columns of the file are as follows:")
print(list(df.columns))

# Display all rows and columns of the data as a table
print("Here is the data as a table:")
display_table(df)
