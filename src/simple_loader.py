# Copyright (c) 2024 Alessandro Borges
# This file is licensed under the  MIT License.
# See the LICENSE file in the project root for full license details.

# Simple loader for ARC AGI dataset

"""
This module is responsible for loading and managing data related to the ARC AGI dataset.
It determines the appropriate base path for loading data, depending on the environment
(development or production). It provides functions to load JSON data and CSV files,
specifically for task labels and task-label associations. The module also includes
global variables for paths and a counter for unknown tasks.
"""


import json
import os
import random
from typing import Dict, List
import pandas as pd
import numpy as np


# base loading path is dev_path, but if prod_path exists, it will be used instead
dev_path='/data/input/arc-prize-2024/'
# prod paths
prod_path='/kaggle/input/arc-prize-2024/'
prod_path_dot='./kaggle/input/arc-prize-2024/'

# default base loading path is dev_path, but if prod_path exists, it will be used instead
base_path = dev_path

# check if prod_path exists and if not, fallback to dev_path local
if os.path.exists(prod_path):
    base_path = prod_path
    print('Production mode')
elif os.path.exists(prod_path_dot): # just in case the first path fails
    base_path = prod_path_dot
    print('Production mode with dot')    
else:
    print('Development mode')


# labels path
labels_path = './task_classes_names.csv'
label_task_path = './task_and_labels.csv'

global_unkown_task_counter = 0

# Loading JSON data
def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def load_labels_csv(file_path, index_col=None):
    """
    Load CSV file with for indexing
    """
    print(f'Loading data from {file_path}')
    df = pd.read_csv(file_path, index_col=index_col)
    return df

# load labels and puzzles with labels
labels_only = load_labels_csv(labels_path, index_col="label_str")
task_and_labels = load_labels_csv(label_task_path, index_col="task_id")
print("labels_only len(): ", len(labels_only))

# choose or not to load evaluation tasks
load_evaluation = True 

# load puzzle dataset
print('Loading ARC AGI dataset (simple_loader.py)' )
training_challenges   = load_json(base_path +'arc-agi_training_challenges.json')
training_solutions    = load_json(base_path +'arc-agi_training_solutions.json')

evaluation_challenges = load_json(base_path +'arc-agi_evaluation_challenges.json') if load_evaluation else None
evaluation_solutions  = load_json(base_path +'arc-agi_evaluation_solutions.json') if load_evaluation else None
test_challenges       = load_json(base_path +'arc-agi_test_challenges.json')


def get_all_labels()->List[str]:
    """
    Get all labels from the dataset
    """
    return list(labels_only.index)

def get_label_metadata(label_str:str)->dict:
    """
    Get label metadata from the dataset.
    Return the label_id, label_str and description
    
    Args:
        label_str (str): The string label to look up metadata for
        
    Returns:
        dict: A dictionary containing:
            - label_id (int): The numeric ID of the label
            - label_str (str): The string label
            - description (str): Description of what the label represents
    """
    meta = labels_only.loc[label_str]
    return {
        'label_id': meta['label_id'],
        'label_str': label_str,
        'description': meta['description']
    }

def get_labels_stats(samples=None) -> List[tuple]:
    """
    Gets label stats, like metadata and counts
    from the dataset.
    Returns a list of metadata dictionaries as described below:
        dict: A dictionary containing:
                - label_id (int): The numeric ID of the label
                - label_str (str): The string label
                - description (str): Description of what the label represents
                - count(int): Number of samples with this label
    
    """
    labels = get_all_labels()
    metadata = [get_label_metadata(label) for label in labels]
    # array with counts of each label - zeroed
    count_arr=[0]*len(labels)
    # get all samples
    samples = samples if samples is not None else create_train_loader()
    for sample in samples:
        label = sample['classe_str']
        idx = labels.index(label)
        count_arr[idx] += 1
    # add counts to metadata
    for i, meta in enumerate(metadata):
        meta['count'] = count_arr[i]
    return metadata    
            
     

def filter_tasks_by_label(tasks:List[Dict], label_str:str):
    """
    Filter tasks by label string
    """
    filtered_tasks = []
    for task in tasks:
        task_id = task['task_id']
        _, label_str_, _ = get_task_metadata(task_id)
        if label_str_ == label_str:
            filtered_tasks.append(task)
            
    return filtered_tasks

def create_train_loader(which_one="training", 
                        init_task:int=0, 
                        max_tasks:int=400,                          
                        shuffle=False,
                        debug=False)->List[Dict]:
    """  
    This function creates a training loader with few-shot samples for training or evaluation.

    Parameters:   
    - which_one (str): Specifies whether to use "training" , "evaluation" or "all" tasks. Default is "training".
    - init_task (int): The initial task index to start from. Default is 0.
    - max_tasks (int): The maximum number of tasks to include. Default is 400.    
    - num_samples (int): The number of samples to return. Use None to get all samples. Default is None.
    - extend_samples (bool): Whether to augment the samples using data augmentation techniques. Default is True.
    - extend_mode (str): The mode for extending the samples. Must be 'full' or 'limited'. Default is 'limited'.
    - simplify_color_map (bool): Whether to simplify the color map by enhancing contrast. Default is True.
    - shuffle (bool): Whether to shuffle the samples. Default is False.

    Returns:
    - List[FewShotSample]: A list of FewShotSample objects to be used for training or evaluation.
    """
    train_loader = [] 
    #which_one = "training" # "evaluation" # "test"
    #train_or_test = "train" #"test"
    #input_or_output =  "input" #"output"
    
    if which_one not in ["training", "evaluation", "all"]:
        raise ValueError("which_one must be either 'training', 'evaluation', or 'all'.")
    if max_tasks > 400:
        raise ValueError("max_tasks must be less than or equal to 400.")
    
    if which_one == "all":
        max_tasks = max_tasks // 2 # divide by 2 to get training and evaluation tasks
        training_load = create_train_loader(which_one="training", init_task=init_task, max_tasks=max_tasks, shuffle=shuffle)	
        eval_load = create_train_loader(which_one="evaluation", init_task=init_task, max_tasks=max_tasks, shuffle=shuffle)	
        for sample in training_load:
             train_loader.append(sample)
        for sample in eval_load:
             train_loader.append(sample)
        return train_loader         
    # load training tasks
    elif which_one == "training":
        print('ARC AGI training samples loading...')
        for i in range(init_task, init_task + max_tasks):
            task_id=list(training_challenges)[i]           
            task=training_challenges[task_id]
            task_solution = training_solutions[task_id][0]            
            task_num = i + 1 # 1-based index :: 1 to 400
            sample = create_unique_task_sample(task, task_solution, task_num=task_num, task_id=task_id)
            train_loader.append(sample)
            if debug:
                print(f"Task training {i+1} : {task_id}, examples: {len(sample['examples'])}")  
    # load evaluation tasks               
    elif which_one == "evaluation":
        print('ARC AGI evaluation samples loading...')
        for i in range(init_task, init_task + max_tasks):
            task_id=list(evaluation_challenges)[i]            
            task=evaluation_challenges[task_id]
            task_solution = evaluation_solutions[task_id][0]            
            task_num = i + 401 # 1-based index :: 401 to 800
            sample = create_unique_task_sample(task, task_solution, task_num=task_num, task_id=task_id)            
            train_loader.append(sample)
            if debug:
                print(f"Task evaluation {i+1} : {task_id}, examples: {len(sample['examples'])}")            
    # Shuffle the samples
    if shuffle:
        random.shuffle(train_loader)
    print(f"Number of {which_one} samples: {len(train_loader)}")    
    return train_loader

def	create_unique_task_sample(task, task_solutions, task_num:int, task_id:str)->dict:	
    """  
    Create a single sample dictionary from a task and its solutions.
    Used by create_train_loader() to create a single sample for a task.
    
    Args:
        task (dict): A dictionary containing the task data, including 'train' and 'test' examples.
        task_solutions (list): A list of solutions for the task.
        task_num (int): The task number (1-400 for training, 401-800 for evaluation).
        task_id (str): The unique identifier for the task.

    Returns:
        dict: A dictionary containing:
            - task_id (str): The unique task identifier
            - task_num (int): The task number
            - classe_id (int): The numeric category ID for the task
            - classe_str (str): The string description of the task category
            - examples (list): List of (input, output) matrix tuples for training
            - question (ndarray): Input matrix for test example
            - question_answer (ndarray): Solution matrix for test example
    """
    num_train = len(task['train'])   

    examples_ = []
    for j in range(num_train):
        input  = get_matrix(task, j, 'train', 'input')
        output = get_matrix(task, j, 'train', 'output')
        tupla = (input, output)
        examples_.append(tupla)
    
    question_ = get_matrix(task, 0, 'test', 'input')
    question_answer_ = np.array(task_solutions, dtype=np.byte)
    label_id, label_str, _ =  get_task_metadata(task_id) 
     
    sample = {
        'task_id': task_id,
        'task_num': task_num,
        'classe_id': label_id,
        'classe_str': label_str,    
        'examples': examples_,
        'question': question_,
        'question_answer': question_answer_, 
    }
    return sample

def get_matrix(task, i, train_or_test, input_or_output, dtype_=np.byte):  
    """
    Returns the matrix of the i-th task, train or test, input or output
    # input_matrix = task[train_or_test][i][input_or_output]
    """  
    matrix = task[train_or_test][i][input_or_output]
    matrix = np.array(matrix, dtype=dtype_)
    return matrix

def get_task_metadata(task_id:str, debug=False)->tuple:
    """  
    Returns metadata information for a given task ID.
    Args:
        task_id (str): The unique identifier for the task
        debug (bool): Whether to print debug information. Default is False.
    Returns:
        tuple: A tuple containing:
            - label_id (int): The numeric ID of the task's label category
            - label_str (str): The string description of the task's label category 
            - task_order (int): The ordinal position/index of this task
    """    
   
    if debug:
        print(f"Task ID: {task_id}")
        try:
            label_str = task_and_labels.loc[task_id, 'label_str']        
        except KeyError:
            raise ValueError(f"Task ID {task_id} not found in task_and_labels DataFrame.")
            
        if label_str not in labels_only.index:
                raise ValueError(f"Task ID {task_id} not found in labels_only index.")
                
        try:
            label_id = labels_only.loc[label_str, 'label_id']        
        except KeyError:
            raise ValueError(f"Task ID {task_id} not found in labels_only index.")
        if label_id is None:
                raise ValueError(f"Task ID {task_id} not found in labels_only index.")
            
        task_order = task_and_labels.loc[task_id, 'ord']
        return label_id, label_str, task_order
    else:
        global global_unkown_task_counter
        try:
            task_order = task_and_labels.loc[task_id, 'ord']
            label_str = task_and_labels.loc[task_id, 'label_str']        
            label_id = labels_only.loc[label_str, 'label_id']
        except KeyError:
            global_unkown_task_counter += 1
            return 0, 'unspecified', global_unkown_task_counter 
        return label_id, label_str, task_order

def test_load():
    # test the loader
    train_loader = create_train_loader(which_one="training", init_task=0, max_tasks=400, shuffle=False)
    print(f"Number of training samples: {len(train_loader)}")
    for i, sample in enumerate(train_loader):
        if i<5:
            print(f"Task ID: {sample['task_id']}, Task Num: {sample['task_num']}, Class: {sample['classe_str']}")
            print(f"Class ID: {sample['classe_id']}")
            print(f"Class Str: {sample['classe_str']}")
            print(f"Number of examples: {len(sample['examples'])}")
            print(f"Question: \n{sample['question']}")
            print(f"Question Answer: \n{sample['question_answer']}")       
            print("")

if __name__ == "__main__":    
    print("simple_loader loaded")
    #test_load()

#classe_id, classe_str, task_order = get_task_metadata('000d4b032')