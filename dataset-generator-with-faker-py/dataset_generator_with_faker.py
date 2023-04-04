!pip install pandas faker ipywidgets openpyxl

import pandas as pd
import random
import string
import ipywidgets as widgets
from IPython.display import display
from faker import Faker
from pathlib import Path

# Initialize the Faker library
fake = Faker()

# Define the list of data types to generate
data_types = [
    {'label': 'Name', 'value': 'name'},
    {'label': 'Address', 'value': 'address'},
    {'label': 'Phone number', 'value': 'phone_number'},
    {'label': 'Email', 'value': 'email'},
    {'label': 'Job', 'value': 'job'},
    {'label': 'Company', 'value': 'company'},
    {'label': 'Postal code', 'value': 'postcode'},
    {'label': 'City', 'value': 'city'},
    {'label': 'Country', 'value': 'country'}
]

# Define the function to generate the data
def generate_data(num_rows, selected_fields):
    """
    Generate fake data for the selected fields and return a Pandas DataFrame.
    """
    data = {}
    # Use list comprehension to generate the data for each selected field
    for field in selected_fields:
        data[field['value']] = [getattr(fake, field['value'])() for i in range(num_rows)]
    return pd.DataFrame(data)

# Define the function to save the data
def save_data(filename, data, file_format):
    """
    Save the data to a file with the specified name and format.
    """
    # Use pathlib library to create the file name with the extension
    file_path = Path(filename + '.' + file_format)
    if file_format == 'csv':
        data.to_csv(file_path, index=False)
    elif file_format == 'excel':
        data.to_excel(file_path, index=False)
    print(f'The data has been saved to a {file_format.upper()} file named "{filename}".')

# Define the function to generate and save the data
def generate_and_save_data(button):
    """
    Generate and save the data based on the user input.
    """
    # Get the user input
    num_rows = int(num_rows_input.value)
    selected_fields = [data_types[i] for i in range(len(data_types)) if checkboxes[i].value]
    filename = filename_input.value.strip()
    file_format = format_select.value
    
    # Generate the data
    data = generate_data(num_rows, selected_fields)
    
    # Save the data
    save_data(filename, data, file_format)
    
    # Display the data
    display(data)

# Create the widgets for the user input
num_rows_input = widgets.Text(value='10', placeholder='Number of rows')
filename_input = widgets.Text(value='data', placeholder='File name')
format_select = widgets.Dropdown(options=['csv', 'excel'], value='csv', description='Format:')
checkboxes = [widgets.Checkbox(description=field['label'], value=True) for field in data_types]

# Organize the checkboxes in a 3x3 grid
grid = widgets.GridBox(children=checkboxes, layout=widgets.Layout(grid_template_columns="repeat(3, auto)"))

# Create a VBox to organize the widgets vertically
vbox = widgets.VBox([
    widgets.HBox([num_rows_input, filename_input, format_select]),
    widgets.Box([grid], layout=widgets.Layout(padding='10px')),
    widgets.Button(description='Generate and save', button_style='primary', layout=widgets.Layout(margin='10px'))
])

# Set the function to be called when the button is clicked
vbox.children[2].on_click(generate_and_save_data)

# Display the widgets
display(vbox)
