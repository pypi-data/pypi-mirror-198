import requests
import pandas as pd
import json
import builtins
import numpy
from datetime import datetime
import os
from deepdiff import DeepDiff
import apitest_harness
from logging import *

class TestHarness:

    def __init__(self):
        dir = apitest_harness.__file__
        self.package_dir = dir.split('__init__')[0]
        regression_path = os.environ.get('regression_file')
        if regression_path !=None:
            from apitest_harness.src.Ls_regression import generate_testcases_sheet
            generate_testcases_sheet()
        source_type = os.environ.get("source_type")
        if source_type == 'EXCEL':
            path = os.environ.get("source_file") if regression_path ==None else self.package_dir + os.environ.get("source_file")
            test_sheet = os.environ.get('sheet_test')
            input_sheet = os.environ.get('sheet_input')
            output_sheet =os.environ.get('sheet_output')
            self.path = os.environ.get('source_file')
            self.test_df = pd.read_excel(path, test_sheet, keep_default_na=False)
            self.input_df = pd.read_excel(path, input_sheet, keep_default_na=False)
            self.output_df = pd.read_excel(path, output_sheet, keep_default_na=False)
        else:
            self.test_df, self.input_df, self.output_df, self.path  = self.generate_df()
       
    def doTests(self):
        report_data_list = []
        for id in self.test_df['test_id'].unique():
            test_name = self.test_df['test_name'][id-1]
            execute_test = self.test_df['test_execute'][id-1]
            if execute_test.lower() == 'yes':
                validation_result = self.check_validations(id)
                api_path, method_type, json_body,api_name = self.get_inputs(id)
                if len(validation_result)== 0:
                    if method_type == 'GET':
                        api_response_data = self.execute_httpRequest(api_path, method_type)
                    elif method_type == 'POST':
                        api_response_data = self.execute_httpRequest(api_path, method_type, json_body)
                    output_data, test_id = self.get_output(id)
                    # DO THE COMPARISON HERE between output_data and api_response_data
                    print()
                    print(f'api_response_data:{id} {api_response_data}')
                    print()
                    print(f'Test===========>{test_id} {output_data}')
                    testcase_result,testcase_name,root_cause = self.compare_dictionaries(api_response_data,output_data,test_id)
                    print(f'Test===========>{id} {testcase_result}')
                    validations = None
                    report_data_list.append([id,testcase_name,api_name,testcase_result,root_cause,validations])
                else:
                    testcase_result = 'Failed'
                    root_cause = 'Validations Error'
                    validations_error = {'validations':validation_result}
                    report_data_list.append([id,test_name,api_name,testcase_result,root_cause,validations_error])
                    continue
            else:
                continue
        self.generate_report(report_data_list)
        
    def get_inputs(self, id):
        filter_test_df = self.test_df[self.test_df['test_id'] == id]
        for api in filter_test_df['Api_name']:
            for type in filter_test_df['Api_Type']:
                path = api
                method_type = type
        filter_input_df = self.input_df[self.input_df['test_id'] == id].reset_index()
        if method_type == "GET":
            api_path, method_type,api_name = self.method_get_inputs(filter_input_df, method_type, path)
            return api_path, method_type, None,api_name
        elif method_type == 'POST':
            api_path, method_type, json_body,api_name = self.method_post_inputs(filter_input_df, method_type, path)
            return api_path, method_type, json_body,api_name

    def method_get_inputs(self, filter_input_df, method_type, path):
        list_of_inputs = []
        for ind in filter_input_df.index:
            inputs = F"{filter_input_df['param'][ind]}={filter_input_df['value'][ind]}"
            list_of_inputs.append(inputs)
        input_param = '&'.join(list_of_inputs)
        api_path = f"{path}?{input_param}"
        path1 = path.split('/')[-2]
        path2 = path.split('/')[-1]
        final_api_name = path1+'/'+path2
        return api_path, method_type,final_api_name

    def method_post_inputs(self, filter_input_df, method_type, path):
        api_path = path
        list_of_dict = []
        dict_body = {}
        for indx in filter_input_df.index:
            key = filter_input_df['param'][indx]
            value = filter_input_df['value'][indx]
            value_type = filter_input_df['type'][indx]
            final_value = self.cast_by_name(value_type, value)
            if value_type == 'list':
                final_value = list(eval(value))
            new_dict = {key: final_value}
            list_of_dict.append(new_dict)
            for dict_obj in list_of_dict:
                dict_body.update(dict_obj)
            json_body = json.dumps(dict_body)
            path1 =path.split('/')[-2]
            path2 = path.split('/')[-1]
            final_api_name = path1+'/'+path2
        return api_path, method_type, json_body,final_api_name

    @classmethod
    def cast_by_name(cls, type_name, value): 
            return getattr(builtins, type_name)(value)
       
    def get_output(self, id):  
        dict_try, index, new_output_df, list_of_keys, id = self.get_structure_dictionary(id)
        output_json, id = self.get_expected_json(dict_try, index, new_output_df, list_of_keys, id)
        return output_json, id
       

    def execute_httpRequest(self, path, method, body=None):
        domain = os.environ.get("url_base")
        authorization = ''
        content_type = 'application/json'
        headers = {'content-type': content_type,
                   'Authorization':authorization}
        url = f'{domain}{path}'
        if method == 'GET':
            response = requests.get(url, headers=headers)
            if response.status_code == 200 or response.status_code == 201:
                return response.json()
            else:
                return response.reason
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=body)
            if response.status_code == 200 or response.status_code == 201:
                return response.json()
            else:
                return response.reason
    

    def get_structure_dictionary(self, id):
        filter_output_df = self.output_df[self.output_df['test_id'] == id].reset_index()
        new_output_df = filter_output_df[['param', 'value', 'type']].copy()
        list_of_keys = []
        dict_try = {}
        for i in new_output_df['param']:
            param_list = i.split('.')
            result = any(chr.isdigit() for chr in param_list)
            if result!=True:
                list_of_keys.append(i)
                index = 2
            else:
                index = new_output_df.param[new_output_df.param == i].index[0]
                break
        dict_condtion = False
        for i in list_of_keys:
            index_val = new_output_df.param[new_output_df.param == i].index[0]
            dict_val_type = new_output_df['type'][index_val]
            val_for_dict = new_output_df['value'][index_val]
            if dict_val_type == 'dict':
                df = new_output_df.iloc[index:]
                for ele in df['param']:
                    if i in ele:
                        dict_condtion = True
            if dict_val_type == 'list':
                dynamic_dict = {i: []}
                size = val_for_dict.split('=')[1]
                for j in range(int(size)):
                    dynamic_dict[i].append({})
            elif dict_val_type == 'dict':
                dynamic_dict = {i: {}}
            else:
                if dict_val_type == 'bool' and val_for_dict.upper() == 'FALSE':
                    val_for_dict = 0
                elif dict_val_type == 'bool' and val_for_dict.upper() == 'TRUE':
                    val_for_dict = 1
                casted_value = self.cast_by_name(dict_val_type, val_for_dict)
                if dict_val_type == 'str' and val_for_dict == 'None':
                    casted_value = eval(val_for_dict)
                dynamic_dict = {i: casted_value}
            for key, value in dynamic_dict.items():
                if key in dict_try:
                    if isinstance(dict_try[key], list):
                        dict_try[key].append(value)
                    else:
                        dict_try[key] = [dict_try[key], value]
                else:
                    keys = dict_try.copy().keys()
                    if keys:
                        for k in keys:
                            if len(dict_try)!=0 and isinstance(dict_try[k],dict) and dict_condtion:
                                    dict_try.update(dynamic_dict)
                            elif isinstance(dict_try[k],dict) and dict_condtion!=True:
                                dict_try[k].update(dynamic_dict)
                            else:
                                dict_try[key] = value
                    else:
                        dict_try[key] = value
        return dict_try, index, new_output_df, list_of_keys, id

    def get_expected_json(self, dict_try, index, new_output_df, list_of_keys, id):
        count = 0
        expected_length = []
        final_output_df = new_output_df.iloc[index:]
        for ind in final_output_df.index:
            key = final_output_df['param'][ind]
            value = final_output_df['value'][ind]
            value_type = final_output_df['type'][ind]
            if value_type == 'bool' and value.upper() == 'FALSE':
                value = 0
            elif value_type == 'bool' and value.upper() == 'TRUE':
                value = 1
            casted_value = self.cast_by_name(value_type, value)
            if value_type == 'list':
                if "size=" in value or "Size=" in value:
                    casted_value = []
                    indx_value = value
                else:
                    casted_value = list(eval(value))
            if value == 'None':
                casted_value = eval(value)
            if value_type == 'json':
                casted_value = json.dumps(value)
            split_key = (key.split('.'))
            temp_dict_one = {}
            for ele in list_of_keys:
                index_val = new_output_df.param[new_output_df.param == ele].index[0]
                dict_val_type = new_output_df['type'][index_val]
                try:
                    if dict_val_type == 'list' and split_key[0] == ele:
                        try:
                            if dict_try[ele][int(split_key[1])]:
                                if split_key[-3] in dict_try[ele][int(split_key[1])]:
                                    if int(split_key[1]) != int(split_key[-2]) or int(split_key[-2]) != int(indx_value.split('=')[-1]):
                                        count = 0
                                    [expected_length.append(num) for num in split_key[-2] if num not in expected_length]
                                    if count == 0 and len(dict_try[ele][int(split_key[1])][split_key[-3]]) != len(expected_length) and len(dict_try[ele][int(split_key[1])][split_key[-3]]) != int(indx_value.split('=')[-1]):
                                        dict_try[ele][int(split_key[1])][split_key[-3]].append(temp_dict_one)
                                    dict_try[ele][int(split_key[1])][split_key[-3]][int(split_key[-2])].update({split_key[-1]: casted_value})
                                    count += 1
                                elif split_key[-2] in dict_try[ele][int(split_key[1])]:
                                    dict_try[ele][int(split_key[1])][split_key[-2]].append(casted_value)
                                else:
                                    dict_try[ele][int(split_key[1]) ][split_key[-1]] = casted_value
                            else:
                                dict_try[ele][int(split_key[1])][split_key[-1]] = casted_value
                        except KeyError as e:
                            dict_try[list_of_keys[0]][ele][int(split_key[1])][split_key[-1]] = casted_value
                    elif dict_val_type == 'dict' and isinstance(dict_try[split_key[0]], dict):
                        temp_dict = {split_key[-1]: casted_value}
                        dict_try[ele].update(temp_dict)
                except KeyError as e:
                    if dict_val_type == 'dict' and isinstance(dict_try[list_of_keys[0]][split_key[0]], dict):
                        temp_dict = {split_key[-1]: casted_value}
                        dict_try[ele].update(temp_dict)
        expected_output_json = dict_try
        return expected_output_json, id
       

    def compare_dictionaries(self, response_dict, expected_dict, id):
        try:
            status_list = []
            diff_list = []
            rootcause_msg = ""
            for key,value in expected_dict.items():
                filter_id = id-1
                test_name = self.test_df['test_name'][filter_id]
                t_name = test_name.split('_')[-1]
                response_value = response_dict[key]
                index_list =[]
                if isinstance(response_dict[key], list):
                    [index_list.append(value.index(val)) for val in value if val != {}]
                    if len(index_list)==0:
                        if value == response_value:
                            status_list.append(1)
                        else:
                            status_list.append(0)
                            rootcause_msg = rootcause_msg+f'"value changed" at [{key}] field: expected value is "{value}" but displayed as "{response_value}"'+ os.linesep + os.linesep  
                    for indx in index_list:
                        if t_name =='prohibitions' or t_name=='finmagix':
                            test_status = 1 if len(response_dict[key]) == len(expected_dict[key]) else 0
                            status_list.append(test_status)
                            if test_status == 0:
                                diff_list.append((DeepDiff(len(response_dict[key]), len(expected_dict[key]))))  
                        elif value[indx] == response_value[indx]:
                            status_list.append(1)
                        else:
                            status_list.append(0)
                            diff_list.append(DeepDiff(value[indx],response_value[indx]))
                elif isinstance(response_dict[key], dict):
                    for keys in value:
                        index_list_one = []
                        test_response = value[keys]
                        api_response = response_dict[key][keys]
                        [index_list_one.append(test_response.index(val)) for val in test_response if val!= {}]
                        for indx in index_list_one:
                            if t_name=='finmgix':
                                test_status = 1 if len(response_dict[key]) == len(expected_dict[key]) else 0
                                status_list.append(test_status)
                                if test_status == 0:
                                    diff_list.append((DeepDiff(len(response_dict[key]), len(expected_dict[key]))))
                            elif test_response[indx] == api_response[indx]:
                                status_list.append(1)
                            else: 
                                status_list.append(0)
                                diff_list.append(DeepDiff(test_response[indx],api_response[indx]))
                else:
                    if response_dict[key]==value:
                        status_list.append(1)
                    else:
                        status_list.append(0)
                        diff_list.append(DeepDiff(response_dict[key],value))
            for i in diff_list:
                diff_keys = i.keys()
                for k in diff_keys:
                    diff_data = i[k]
                    diff_values = diff_data.keys()
                    for ele in diff_values: 
                        expected_value = diff_data[ele]['old_value']
                        api_resp_val = diff_data[ele]['new_value']
                        ele = ele.split('root')[-1]
                        k = k.replace('s_',' ')
                        rootcause_msg = rootcause_msg+f'"{k}" at {ele} field: expected value is "{expected_value}" but displayed as "{api_resp_val}"'+os.linesep
            rootcause = rootcause_msg   
            status = numpy.prod(status_list)
            if status == 0:
                return "Failed", test_name, rootcause
            else:
                return "Passed", test_name, None
        except Exception as e:
            rootcause = response_dict
            return 'Failed',test_name,rootcause

    def check_validations(self,id):
        logger = self.get_logger()
        validation_message = []
        input_sheet = self.input_df
        output_sheet = self.output_df
        keys_list = []
        df_list = []
        filter_input_sheet = input_sheet[input_sheet['test_id'] == id]
        filter_output_sheet = output_sheet[output_sheet['test_id'] == id]
        df_list.append(filter_input_sheet)
        df_list.append(filter_output_sheet)
        for df in df_list:
            for indx in df.index:
                type = df['type'][indx]
                if type != '':
                    values = df['value'][indx] 
                    param = df['param'][indx]
                    expected_types_format = ['list','str','int','dict','bool','json','float']
                    if type not in expected_types_format:
                        response = {"Message":f"'{type}' value format should match with format shown in list {expected_types_format}"}
                        logger.error(response['Message'])
                        validation_message.append(response)
                    if type == 'bool':
                        result = values.isdigit()
                        if result == True:
                            response = {"Message":f"For '{param}' Boolean value should be in True or False format not in digit."}
                            logger.error(response['Message'])
                            validation_message.append(response)
                    try:
                        if type != 'list' and type != 'dict':
                            if type == 'bool' and values.upper() == 'FALSE':
                                values = 0
                            elif type == 'bool' and values.upper() == 'TRUE':
                                values = 1   
                            self.cast_by_name(type,values)    
                        if type == 'json':
                            json.dumps(values)
                        if type!='int':
                            if type == 'list' and "size=" not in values and "Size=" not in values:
                                list(eval(values))
                    except Exception as e:
                        response = {"Message":f"Provide valid data for '{param}'."}
                        logger.error(response['Message'])
                        validation_message.append(response)
                    if type != 'int' and type!='bool':
                        if "size=" in str(values) or "Size=" in str(values):
                            size_value1 = values
                            size_value = values.split('=')[-1]
                            if int(size_value)!=0:
                                value = int(size_value)-1
                                key = df['param'][indx]
                                result = any(chr.isdigit() for chr in key)
                                if type!='dict' and result!=True:
                                    keys_list.append({key:value})   
                for keys in keys_list:
                    for main_key,object_size in keys.items():
                        list_of_params = []
                        param_list = df['param'].tolist()
                        for ele in param_list:
                            param = ele.split('.')
                            if param[0] == main_key:
                                list_of_params.append(param)    
                        list_obj = list_of_params[-1]
                        param_size = [int(ele) for ele in list_obj if ele.isdigit()]
                        if max(param_size) != object_size:
                            response = {"Message":f"The size of the '{main_key}' objects should be equal to the '{main_key}' parameters."}
                            logger.error(response['Message'])
                            validation_message.append(response)
        return validation_message      


    def generate_df(self):
        path = os.environ.get("source_file")
        print('=========>> JSON')
        with open(file=path,mode='r') as f:
            testcases_json = json.loads(f.read())
            testcases_dict = testcases_json['data']
            test_values_list = []
            input_values_list =[]
            output_values_list = []
            for obj in testcases_dict:
                test_values = []            
                test_col_keys = obj.keys()
                test_columns = [key for key in test_col_keys if key != 'input' if key!= 'output']
                input_columns = []
                for key,value in obj.items():
                    if key != 'input' and key != 'output':
                        test_values.append(value)
                    elif key == 'input':
                        for val in value:
                            input_values = []
                            input_values.append(obj['test_id'])
                            input_columns = list(val.keys())
                            for key,value in val.items():
                                input_values.append(value)
                            input_values_list.append(input_values)
                    else:
                        for val in value:
                            output_values = []
                            output_values.append(obj['test_id'])
                            output_columns = list(val.keys())
                            for key,value in val.items():
                                output_values.append(value)
                            output_values_list.append(output_values) 
                test_values_list.append(test_values) 
            input_columns.insert(0,'test_id')
            output_columns.insert(0,'test_id')   
            test_df = pd.DataFrame(test_values_list,columns=test_columns)
            input_df = pd.DataFrame(input_values_list,columns=input_columns)
            output_df = pd.DataFrame(output_values_list,columns=output_columns)
            return test_df,input_df,output_df,path


    def generate_report(self,report_data_list):
        report_df = pd.DataFrame(report_data_list,columns=['Testcase ID','Testcase Name','Api Name','Testcase Result','RootCause','Validations'])
        date_time = datetime.now().strftime("%d_%m_%Y-%I_%M_%S_%p")
        report_name = self.path.split('/')[-1].split('.')[0]
        file_name = f'{report_name}_report_{date_time}.xlsx'
        domain = os.environ.get("url_base")
        if 'lsccqa' in domain:
            report_sheet_name = os.environ.get('qa_report')
        elif 'lsccdev' in domain:
             report_sheet_name = os.environ.get('dev_report')
        else:
            report_sheet_name = report_name.split('_')[0]+' Report'
        writer = pd.ExcelWriter(f"{self.package_dir}/report/{file_name}",engine='xlsxwriter') 
        report_df.to_excel(writer, sheet_name=report_sheet_name, index=False, na_rep='None')
        for column in report_df:
            column_length = max(report_df[column].astype(str).map(len).max(), len(column))
            if column == 'RootCause':
                column_length=100
            col_idx = report_df.columns.get_loc(column)
            workbook  = writer.book
            worksheet = writer.sheets[report_sheet_name] 
            text_wrap_format = workbook.add_format({'text_wrap': True,'valign': 'left','align': 'top'})
            writer.sheets[report_sheet_name].set_column(col_idx, col_idx, column_length,text_wrap_format)
            header_format = workbook.add_format({'bold': True,'bottom': 1,'bg_color': '#D3D3D3'})
            for col_num, value in enumerate(report_df.columns.values):
                worksheet.write(0, col_num, value, header_format)
        writer.save()
        report_df.to_json(f"{self.package_dir}/report/{report_name}_report_{date_time}",orient='records',lines=True)


    def get_logger(self):
        LOG_FORMAT = '%(asctime)s ----- %(levelname)s: %(message)s'
        basicConfig(filename=f"{self.package_dir}/logs/logfile.log", level=INFO, format=LOG_FORMAT,filemode='w')
        logger = getLogger()
        console = StreamHandler()
        console.setLevel(INFO)
        formatter = Formatter(LOG_FORMAT)
        console.setFormatter(formatter)
        logger.addHandler(console)
        return logger