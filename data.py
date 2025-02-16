import json
import csv
import datetime
import re

def extract_data(jsonfilename, fields):
    ''' 
    Given a json file, produces a dictionary of reddit post data (post date, text)
    Input:
        jsonfilename: name of file containing data to be read in 
        fields: list of attributes to be extracted from json file
    Output:
        dictionary
    '''
    content_list = []
    data_dict = {}

    with open(jsonfilename, 'r') as jsonl_file:
        for line in jsonl_file:
            parsed_line = json.loads(line)
            content_list.append(parsed_line)

    for index, content in enumerate(content_list):
        data_dict[f'Post {index}'] = tuple(content[field] for field in fields if field in content)

    return data_dict

def clean_data(data_dict):
    ''' 
    Given a dictionary mapping index numbers to unix date 
    and text information, produces a new dictionary mapping 
    translated dates to tokenized strings
    Input:
        data_dict: a dictionary
    Output:
        cleaned_dict: a dictionary
    '''
    cleaned_dict = {}
    for index, content in data_dict.items():
        date, text = content
        converted_date = datetime.datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
        cleaned_text = re.sub(r'[0-9]', ' ', text)
        cleaned_text = re.sub(r'[^\w\s]', ' ', cleaned_text)
        cleaned_text = cleaned_text.replace('\n', ' ').strip()#.split()
        cleaned_dict[converted_date] = cleaned_text
    return {k: v for k, v in cleaned_dict.items() if v and v != "removed"}

def to_csv(csvfilename, clean_data_dict):
    ''' 
    Given a dictionary mapping dates to tokenized strings,
    writes a CSV file mapping the same pairs
    Input:
        csvfilename: a string representing the name of the
        output csv
        clean_data_dict: a dictionary
    '''
    with open(csvfilename,'w',newline='') as f:
        output = csv.writer(f, delimiter=':')
        for line, content in clean_data_dict.items():
            output.writerow([line, content])