import pandas as pd
import json 
import os
import numpy as np
import datetime
import apitest_harness

def typeconverter(obj):
    if isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, datetime.datetime):
        return obj.__str__()

def write_json(new_data, filename="testcase_json.JSON"):
    dir = apitest_harness.__file__
    desired_dir = dir.split('__init__')[0]
    full_path = f"{desired_dir}/source/{filename}"
    with open(full_path, 'w') as f:
        json_string=json.dumps(new_data,default=typeconverter)
        f.write(json_string)

def excel_to_json():
    path = os.environ.get("source_file")
    test_sheet = os.environ.get('sheet_test')
    input_sheet = os.environ.get('sheet_input')
    output_sheet =os.environ.get('sheet_output')
    test_df = pd.read_excel(path, test_sheet, keep_default_na=False)
    input_df = pd.read_excel(path, input_sheet, keep_default_na=False)
    output_df = pd.read_excel(path, output_sheet, keep_default_na=False)
    structure_json= {'data':[]}
    for id in test_df['test_id'].unique():
        temp_dict= {}
        test_column_list = test_df.columns
        input_column_list =  input_df.columns 
        output_column_list = output_df.columns
        for tcol in test_column_list:
            temp_dict.update({tcol:test_df[tcol][id-1]})
        filter_input_df = input_df[input_df['test_id'] == id].reset_index()
        input_dict = {'input':[]}
        for indx in filter_input_df.index:
            temp_dict_one = {}
            input_column_list = [ele for ele in input_column_list if ele != 'test_id']
            for icol in input_column_list:
                temp_dict_one.update({icol:filter_input_df[icol][indx]})
            input_dict['input'].append(temp_dict_one)
        temp_dict.update(input_dict)
        filter_output_df = output_df[output_df['test_id'] == id].reset_index()
        output_dict = {'output':[]}
        for indx  in filter_output_df.index:
            temp_dict_two = {}
            output_column_list = [ele for ele in output_column_list if ele != 'test_id']
            for ocol in output_column_list:
                temp_dict_two.update({ocol:filter_output_df[ocol][indx]})
            output_dict['output'].append(temp_dict_two)
        temp_dict.update(output_dict)
        structure_json['data'].append(temp_dict)
    # print(structure_json)
    write_json(structure_json)
   
