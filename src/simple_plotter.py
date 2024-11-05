# Copyright (c) 2024 Alessandro Borges
# This file is licensed under the  MIT License.
# See the LICENSE file in the project root for full license details.

# Simple plotter for ARC tasks

"""
 This module provides functions to visualize ARC tasks using matplotlib.
 It includes a colormap for task visualization and functions to plot tasks
 and display the colormap. The tasks are represented as dictionaries containing
 task metadata and examples, which are plotted to help understand the task structure.
 """


import matplotlib.pyplot as plt
from matplotlib import colors 
import numpy as np

from simple_loader import create_train_loader

# 0:black, 1:blue, 2:red, 3:green, 4:yellow, # 5:gray, 6:magenta, 7:orange, 8:sky, 9:brown
cmap_ = colors.ListedColormap(
    ['#000000', '#0074D9', '#FF4136', '#2ECC40', '#FFDC00',
     '#AAAAAA', '#F012BE', '#FF851B', '#7FDBFF', '#870C25'])
norm_ = colors.Normalize(vmin=0, vmax=9)


def show_colormap(cmap=cmap_, norm=norm_):    
    plt.figure(figsize=(3, 1), dpi=150)
    plt.imshow([list(range(10))], cmap=cmap, norm=norm)
    plt.xticks(list(range(10)))
    plt.yticks([])
    plt.show()
    
    
def plot_task(task, i, t, max_examples=6,cmap=cmap_, norm=norm_):
    """    
    Plots the examples and question of a specified task,
    using same color scheme as the ARC app  
    
    The input task is a dictionary as following
        dict: A dictionary containing:
            - task_id (str): The unique task identifier
            - task_num (int): The task number
            - classe_id (int): The numeric category ID for the task
            - classe_str (str): The string description of the task category
            - examples (list): List of (input, output) matrix tuples for training
            - question (ndarray): Input matrix for test example, aka 'test'
            - question_answer (ndarray): Solution matrix for test example, aka 'solution'
    args:
        - samples: list of tasks
        - i: index of the task to plot
        - t: title of the plot
        - max_examples: maximum number of examples to plot. default is 5
        - cmap: colormap
        - norm: color normalization
    """    
   
    # the number of samples to plot, limited to 5
    num_train = len(task['examples'])
    if num_train >max_examples:
        num_train = max_examples
        
    # Check if this task has a test question - if so there is 1 test case, otherwise 0
    # This determines how many test examples to plot alongside the training examples
    num_test  = 1 if 'question' in task else 0
        
    w=num_train+num_test
    
    fig, axs  = plt.subplots(2, w, figsize=(3*w ,3*2))
    task_id = task['task_id']
    task_num = task['task_num']
    classe_str = task['classe_str']
    plt.suptitle(f'Task: {task_id} - (#{task_num}), Label: {classe_str}          Set: {t}', fontsize=18, fontweight='bold', y=0.98)
    
    examples = task['examples']
    for j in range(len(examples)):         
        example = examples[j]
        matrix_input = example[0]
        matrix_output = example[1]
        #ploting examples aka train   
        plot_one(task, axs[0, j], j+1, matrix_input ,'train', 'input')
        plot_one(task, axs[1, j], j+1, matrix_output,'train', 'output')        
    
    # plot the task's question
    matrix_question = task['question'] 
    plot_one(task, axs[0, j+1], 0, matrix_question ,'test', 'input')

    matrix_answer = task['question_answer'] if 'question_answer' in task else None
    #if matrix_answer is not None:
    #    plot_one(task, axs[1, j+1], 0, matrix_answer ,'test', 'output')
    
    if matrix_answer is None:
        matrix_answer = np.zeros((2,2), dtype=np.byte)
    
    shape = matrix_answer.shape
    xx = shape[1]
    yy = shape[0] 
    axs[1, j+1].imshow(matrix_answer, cmap=cmap_, norm=norm_)
    axs[1, j+1].grid(True, which = 'both',color = 'lightgrey', linewidth = 0.5)
    axs[1, j+1].set_yticks([x-0.5 for x in range(1 + len(matrix_answer))])
    axs[1, j+1].set_xticks([x-0.5 for x in range(1 + len(matrix_answer[0]))])     
    axs[1, j+1].set_xticklabels([])
    axs[1, j+1].set_yticklabels([])
    axs[1, j+1].set_title(f'Test output ({xx}x{yy})')

    fig.patch.set_linewidth(5)
    fig.patch.set_edgecolor('black')  # substitute 'k' for black
    fig.patch.set_facecolor('#dddddd')
   
    plt.tight_layout()
    plt.show()  
    
    print()


def plot_one(task, ax, i, matrix_to_plot, train_or_test, input_or_output, cmap=cmap_, norm=norm_):
    """
    Plot a single matrix of the i-th task, input or output
    """    
    ax.imshow(matrix_to_plot, cmap=cmap, norm=norm)
    ax.grid(True, which = 'both',color = 'lightgrey', linewidth = 0.5)

    plt.setp(plt.gcf().get_axes(), xticklabels=[], yticklabels=[])
    ax.set_xticks([x-0.5 for x in range(1 + len(matrix_to_plot[0]))])     
    ax.set_yticks([x-0.5 for x in range(1 + len(matrix_to_plot))])  
    
    shape = matrix_to_plot.shape
    xx = shape[1]
    yy = shape[0] 
    title = f"{train_or_test} #{i} {input_or_output}  - ({xx}x{yy})"
    if train_or_test == 'test' and input_or_output == 'input':
        title = f"{train_or_test} {input_or_output}  - ({xx}x{yy})"        
    ax.set_title(title)

def demo():
    samples = create_train_loader(max_tasks=2)
    for i, sample in enumerate(samples):        
        plot_task(sample, i, 'training')    
    print('simple_plotter Done')

if __name__ == '__main__':
    #show_colormap()
    #demo()    
    print('simple_plotter loaded')