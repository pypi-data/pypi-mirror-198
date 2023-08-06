import pandas as pd
import json
import os
import apitest_harness
def get_output_sheet(dict_data):
    outputsheet_values_list = []   
    for dict_obj in dict_data:
        d1 = dict_obj['Swagger Output']
        if d1=='':
            continue
        output_dict = json.loads(d1)
        keys = output_dict.keys()
        param_keys=[]
        for k in keys:
            if k !='commodity' and  k!= 'country':
                param_keys.append(k)
                output = output_dict[k]
                if isinstance(output, dict):
                    dict_key = k
                    output.keys()
                    param_keys.extend([key for key in output.keys()])
        for pkey in param_keys:
            output_values = []
            try:
                output_data = output_dict[pkey]
                if isinstance(output_data,str):
                    continue
                output_values.append(dict_obj['Test Case No'])
                output_values.append(pkey)
                output_values.append(type(output_data).__name__)
                output_values.append(f"size={len(output_data)}")
                outputsheet_values_list.append(output_values)
            except KeyError as e:
                output_data = output_dict[dict_key][pkey]
                if type(output_data).__name__ =='str':
                    continue
                output_values.append(dict_obj['Test Case No'])
                output_values.append(pkey)
                output_values.append(type(output_data).__name__)
                output_values.append(f"size={len(output_data)}")
                outputsheet_values_list.append(output_values)
        main_key = ''
        for key in param_keys: 
            if key in output_dict:
                param_data = output_dict[key]
            else:
                param_data = output_dict[main_key][key]
                if type(param_data).__name__== 'str':
                    key = F"{main_key}.0.{key}"
            if isinstance(param_data,str):
                output_values1=[]
                output_values1.append(dict_obj['Test Case No'])
                output_values1.append(key)
                output_values1.append(type(param_data).__name__)
                output_values1.append(param_data)
                outputsheet_values_list.append(output_values1)
                continue
            elif isinstance(param_data,dict):
                main_key=key
                continue
            num = 0
            for obj in param_data:
                if len(param_data)>20:
                    indx = param_data.index(obj) 
                    if indx >=2 and indx<len(param_data)-2:
                        num+=1
                        continue
                for param_key,val in obj.items():
                    output_values1=[]
                    output_values1.append(dict_obj['Test Case No'])
                    param = F"{key}.{num}.{param_key}"
                    output_values1.append(param)
                    output_values1.append(type(val).__name__)
                    value_type = type(val).__name__
                    if value_type=='bool':
                        output_values1.append(str(val))
                    else:
                        output_values1.append(val)
                    outputsheet_values_list.append(output_values1)
                num+=1   
    output_df = pd.DataFrame(outputsheet_values_list,columns=['test_id','param','type','value'])
    return output_df

def get_test_sheet(dict_data):
    testsheet_keys=['Test Case No','Test Name','Type','API Name']
    testsheet_values_list = []
    path1 = '/license-screening-service/api/v1/license_requirements/license_requirement/'
    path2 = '/license-screening-service/api/v1/license_requirements/'
    for obj in dict_data:
        if obj[testsheet_keys[0]]== '':
            continue
        test_values = []
        for key in testsheet_keys:
            if key == 'API Name':
                value = obj[key]
                if value == 'getLicenseRequirements' or value == 'checkexception':
                    final_apiname = path1+value
                    test_values.append(final_apiname)
                else:
                    final_apiname = path2+value
                    test_values.append(final_apiname)
            else:
                test_values.append(obj[key])
        test_values.append('yes')
        testsheet_values_list.append(test_values)
    test_df = pd.DataFrame(testsheet_values_list,columns=['test_id','test_name','Api_Type','Api_name','test_execute'])
    return test_df

def get_input_sheet(dict_data):
    inputsheet_values_list = []
    for obj in dict_data:
        input_values = []
        if obj['Test Case No']!='':
            test_id = obj['Test Case No']
        input_values.append(test_id)
        input_values.append(obj['Parameter'])
        value = obj['Value']
        if '[' in value:
            value = eval(value)
            input_values.append(type(value).__name__)
        else:
            input_values.append(type(obj['Value']).__name__)
        input_values.append(obj['Value'])
        inputsheet_values_list.append(input_values)
    input_df = pd.DataFrame(inputsheet_values_list,columns=['test_id','param','type','value'])
    return input_df


def generate_testcases_sheet():
    regression_path =  os.environ.get('regression_file')
    sheet = os.environ.get('regression_sheet')
    regression_sheet_df = pd.read_excel(regression_path,sheet, keep_default_na=False)
    df = regression_sheet_df.replace(r'\n','', regex=True)
    dict_data = df.to_dict('records')
    test_df = get_test_sheet(dict_data)
    input_df = get_input_sheet(dict_data)
    output_df = get_output_sheet(dict_data)
    dir = apitest_harness.__file__
    directory = dir.split('__init__')[0]
    version =regression_path.split('_')[-1].split('.xlsx')[0]
    with pd.ExcelWriter(f"{directory}/source/LSCC_APIVerification_{version}.xlsx") as writer:   
    # use to_excel function and specify the sheet_name and index
    # to store the dataframe in specified sheet
        test_df.to_excel(writer, sheet_name="test",index=False)
        input_df.to_excel(writer, sheet_name="input",index=False)
        output_df.to_excel(writer, sheet_name="output",index=False)
generate_testcases_sheet()
