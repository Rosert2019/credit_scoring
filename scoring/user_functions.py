# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:10:02 2021

@author: Djonga
"""

import pandas as pd
import os

#transform uploaded file to pandas data frame
def handle_uploaded_file(f):
    f = pd.read_csv(f, sep =';')
    return f

def switch_note(grade):
    
    if grade >= 0 and grade < 7:
        return '01'     
    elif grade >= 7 and grade < 14:
        return '02'
    elif grade >= 14 and grade < 20:
        return '03'
    elif grade >= 20 and grade < 24:
        return '04' 
    elif grade >= 24 and grade < 30:
        return '05'
    elif grade >= 30 and grade < 34:
        return '06'    
    elif grade >= 34 and grade < 38:
        return '07'  
    elif grade >= 38 and grade < 42:
        return '08' 
    elif grade >= 42 and grade < 48:
        return '09'
    elif grade >= 48 and grade < 100:
        return '10'
        
        
        
        
def get_score(data_to_score, tab_dataset = ['Age','Amount','Duration','Rate'], tab_names = ['Age','Amount','Duration','Rate']):
    #give a name to each tab_dataset element
    for i in range(0, len(tab_names)):
        tab_dataset[i].name = tab_names[i]

    #for each column in data_to_score and tab_dataset
    for col in data_to_score.columns:       
        for dataset in tab_dataset:  
            #we search which columna has the same name as dataset in tab_dataset
            if col == dataset.name:
                #we make the left join an drop the key of the right table                 
                data_to_score = pd.merge(data_to_score, dataset[['modalities','grades']], left_on=col, right_on='modalities',how='left').drop(columns= ['modalities'])
                #we search column which starts with grades and we rename to column name and coef
                for col_ in data_to_score.columns:
                   if col_.startswith('grades'): 
                      data_to_score.rename(columns={col_ : col+'_coef'}, inplace=True)
                      
                      
    #grades will be the same of column name ended with coef                 
    data_to_score['grades'] = 0

    for col in data_to_score.columns:
        if col.endswith('_coef'): 
            data_to_score['grades'] =  data_to_score['grades'] + data_to_score[col]       
            
          
    data_to_score['score'] = data_to_score['grades'].apply(switch_note)
    
    return data_to_score


def grade_score(tab = ['a','b','c','d']):
    sum = 0
    for elt in tab:
        sum = sum + float(elt)    
    
    return { 'grade': sum, 'score': switch_note(sum)}