This updateMondayItemLib lib helps you updating monday.com items or create new items on monday board.You just need to import library and pass required parameters.In following example I am updating status and log but you can pass as many paramters as required to update in columnValuesDict.

**Usage : **

import requests

import json

import os

import updateMondayItemLib

from updateMondayItemLib import update_testcase_status

apiKey = "test"
apiUrl = "https://api.monday.com/v2"
board_id = "2965157767"
item_id =  "3232338084"
columnValuesDict=  {"status1":"PASS", "long_text":"548"}


update_item(apiKey,apiUrl,board_id,item_id, **columnValuesDict)
create_item(apiKey,apiUrl,board_id,item_name, **columnValuesDict)

**Package is uploded on pypi as well you can just install and use it. **

https://pypi.org/project/updateMondayItemLib/

pip install updateMondayItemLib
