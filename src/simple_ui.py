# Copyright (c) 2024 Alessandro Borges
# This file is licensed under the  MIT License.
# See the LICENSE file in the project root for full license details.

"""
This script provides a simple UI for interacting with ARC tasks. 
It includes functions to display labels and tasks using buttons.
Use the 'create_button_grid' function to generate a grid of buttons 
for each label, which when clicked, displays tasks associated with that label.
"""
import ipywidgets as widgets
from IPython.display import display, clear_output
import numpy as np
import pandas as pd

from simple_loader import get_all_labels, filter_tasks_by_label, get_labels_stats
from simple_plotter import plot_task

def get_labels():    
    return get_all_labels()

def show_labels(button_text):
    # This is your function that will be called when a button is clicked
    clear_output()
    print(f"show_labels() called with: {button_text}")

def show_tasks(button_text, samples):
    # This is your function that will be called when a button is clicked
    print(f"Show tasks labeled as: {button_text}")    
    try:
        label = button_text
        tasks = filter_tasks_by_label(samples, label)
        if len(tasks) == 0:
            print(f"No tasks found for label: {label}")
        else:
            print(f"Found {len(tasks)} tasks for label: {label}")    
            for i, task in enumerate(tasks):
                plot_task(task, i, 'training')
    except Exception as e:
        print(f"show_tasks() error: {e}")
    
    

def create_button_grid(names, samples, cols=6):
    # Calculate dimensions
    n_names = len(names)
    n_rows = (n_names + cols - 1) // cols
    names_padded = names + [''] * (n_rows * cols - n_names)
    matrix = np.array(names_padded).reshape(n_rows, cols)
    
    # Create output widget for displaying results
    output = widgets.Output()
    
    # Create button click handler
    def button_clicked(b):
        with output:
            output.clear_output()
            #show_labels(b.description)
            show_tasks(b.description, samples)
    
    # Create buttons with consistent styling
    buttons = []
    for name in names_padded:
        if name:  # Only create buttons for non-empty names
            button = widgets.Button(
                description=name,
                style={'button_color': '#f0f0f0'},
                layout=widgets.Layout(
                    width='auto',
                    height='auto',
                    padding='5px',
                    margin='2px'
                )
            )
            button.on_click(button_clicked)
            buttons.append(button)
        else:  # Add empty space for padding
            buttons.append(widgets.HTML(value=''))
    
    # Create rows of buttons
    rows = []
    for i in range(n_rows):
        row_buttons = buttons[i*cols:(i+1)*cols]
        row = widgets.HBox(row_buttons, 
                          layout=widgets.Layout(
                              justify_content='flex-start',
                              margin='0'
                          ))
        rows.append(row)
    
    # Combine all rows into a vertical box
    grid = widgets.VBox(rows, 
                       layout=widgets.Layout(
                           border='1px solid #ddd',
                           padding='10px',
                           margin='10px 0'
                       ))
    
    # Create a container for both grid and output
    container = widgets.VBox([
        widgets.HTML(value='<h3>Click a button to show Tasks:</h3>'),
        grid,
        output
    ])
    
    return container

def create_label_grid(samples, cols=6):
    names = get_labels()
    button_grid = create_button_grid(names=names, samples=samples, cols=cols)
    display(button_grid)
    
def show_stats(samples):
    """
    Show label stats from samples
    """
    print('show_stats() called')
    # Print statistics
    labels_stats = get_labels_stats(samples)
    print("Labels statistics:")
    #print labels stats in a pandas table, with coluns label_is, label_str, description, count
    # labels_stats is a list of dictionaries
    df = pd.DataFrame(labels_stats)
    # Update alignment of the columns to left
    styled_df = df.style.set_table_styles(
        [{'selector': 'th', 'props': [('text-align', 'left')]},  # Align header to left
        {'selector': 'td', 'props': [('text-align', 'left')]}]  # Align cells to left
    )
    display(styled_df)
    print("Total samples: ", len(samples))  
    