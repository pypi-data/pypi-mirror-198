import requests
import json

def update_item(apiKey,apiUrl,board_id,item_id, **columnValuesDict):  
    request_headers = {"Authorization" : apiKey}
    for key in columnValuesDict:
        columns_Dict = {
        key: columnValuesDict[key],
        }  
        vars = {
       'item_id' : int(item_id),
        'board_id' : int(board_id),
         'columnVals' : json.dumps(columns_Dict)
         } 
        query =  'mutation ( $board_id: Int!, $item_id: Int!,  $columnVals: JSON!) {change_multiple_column_values (board_id: $board_id, item_id: $item_id, column_values: $columnVals) {id}}'
        data = {'query' : query,'variables' : vars}
        requests.post(url=apiUrl, json=data, headers=request_headers)

def  create_item(apiKey,apiUrl,board_id,item_name, **columnValuesDict):  
    request_headers = {"Authorization" : apiKey}
    vars = {
       'item_name' : item_name,
        'board_id' : int(board_id),
         'columnVals' : json.dumps(columnValuesDict)
         } 
    query =  'mutation ( $board_id: Int!, $item_name: String!,  $columnVals: JSON!) {create_item (board_id: $board_id, item_name: $item_name, column_values: $columnVals) {id}}'
    data = {'query' : query,'variables' : vars}
    requests.post(url=apiUrl, json=data, headers=request_headers)

