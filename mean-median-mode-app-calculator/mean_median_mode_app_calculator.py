# -*- coding: utf-8 -*-
"""mean_median_mode_app_calculator.ipynb

Automatically generated by Colaboratory.

# **1. Required libraries and modules installation**
"""

!pip install pandas numpy ipywidgets

import pandas as pd
import numpy as np
import ipywidgets as widgets
from IPython.display import display
import io

"""# **2. Customization of widget appearance**"""

custom_style = """
<style>
    .widget-label { max-width: 100%; overflow: hidden; text-overflow: ellipsis; }
    .widget-text, .widget-hbox, .widget-vbox { overflow: hidden; }
    textarea { resize: none !important; }
</style>
"""
display(widgets.HTML(custom_style))

"""# **3. Widget creation**"""

data_input = widgets.Textarea(description="Data: ",
                              placeholder="Enter data separated by semicolons (e.g., 1.0; 2.0; 3.0; 4.0; 5.0).",
                              layout=widgets.Layout(width='95%', height='120px'))

mean_checkbox = widgets.Checkbox(description='Mean', tooltip='Calculate the average value.')
median_checkbox = widgets.Checkbox(description='Median', tooltip='Calculate the middle value.')
mode_checkbox = widgets.Checkbox(description='Mode', tooltip='Calculate the most frequent value.')

checkbox_container = widgets.HBox(children=[mean_checkbox, median_checkbox, mode_checkbox],
                                  layout=widgets.Layout(margin='10px', justify_content='space-around'))

calculate_button = widgets.Button(description="Calculate", button_style='info')

mean_label = widgets.HTML(value="")
median_label = widgets.HTML(value="")
mode_label = widgets.HTML(value="")

result_container = widgets.VBox([mean_label, median_label, mode_label])

"""# **4. Statistics calculation functions**"""

def calculate_mean(df):
    return df['Data'].mean()

def calculate_median(df):
    return df['Data'].median()

def calculate_mode(df):
    return df['Data'].mode()[0]

"""# **5. Function to calculate statistics and display results**"""

def calculate_statistics(b):
    data = data_input.value.strip().replace(" ", "").split(';')
    
    # Check if data contains only numeric values
    if all([d.replace('.', '', 1).isdigit() for d in data]):
        data = [float(d) for d in data]
        df = pd.DataFrame({'Data': data})
        
        # Check if at least one checkbox is selected
        if any([mean_checkbox.value, median_checkbox.value, mode_checkbox.value]):
            mean_label.value = f'<b style="color: #1f77b4;">Mean</b> (average value): <b>{calculate_mean(df):.2f}</b>' if mean_checkbox.value else ""
            median_label.value = f'<b style="color: #ff7f0e;">Median</b> (middle value): <b>{calculate_median(df):.2f}</b>' if median_checkbox.value else ""
            mode_label.value = f'<b style="color: #2ca02c;">Mode</b> (most frequent value): <b>{calculate_mode(df):.2f}</b>' if mode_checkbox.value else ""
        else:
            mean_label.value = "Please select at least one statistic to calculate."
            median_label.value = ""
            mode_label.value = ""
    else:
        mean_label.value = "Please enter only numeric values."
        median_label.value = ""
        mode_label.value = ""

"""# **6. Linking the calculation function to the click event of the button**"""

calculate_button.on_click(calculate_statistics)

"""# **7. Creation of containers for widgets and display of results**"""

# Create a container for the text area and checkboxes
input_container = widgets.VBox(children=[data_input, checkbox_container],
                               layout=widgets.Layout(width='100%'))

# Create a container for the output area
output_container = widgets.VBox([result_container],
                                layout=widgets.Layout(width='100%', margin='10px'))

# Create a container for all the widgets
all_widgets_container = widgets.VBox(children=[input_container, calculate_button, output_container])

# Create a container for the results
result_container = widgets.VBox([mean_label, median_label, mode_label],
                                layout=widgets.Layout(align_items='center', margin='10px'))

# Center the Calculate button using an HBox
calculate_button_container = widgets.HBox([calculate_button], layout=widgets.Layout(justify_content='center'))

# Create a container for the text area and checkboxes
input_container = widgets.VBox(children=[data_input, checkbox_container],
                               layout=widgets.Layout(width='100%'))

# Create a container for the output area
output_container = widgets.VBox([result_container],
                                layout=widgets.Layout(width='100%', margin='10px'))

# Create a container for all the widgets
all_widgets_container = widgets.VBox(children=[input_container, calculate_button_container, output_container])

# Display the widgets
display(all_widgets_container)