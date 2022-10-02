import pandas as pd 
import requests
import json
ids = pd.read_csv('ids.csv')
def do(x):
    res = requests.get(f"https://ntrs.nasa.gov/api/citations/{x}")
    if res.status_code==200:
        with open(f"meta/{x}_meta.json",'w') as f:
            json_obj = json.dumps(res.json())
            f.write(json_obj)

ids['ids'].apply(do)
# https://ntrs.nasa.gov/api/citations/1
# https://ntrs.nasa.gov/api/citations/1/downloads
# https://ntrs.nasa.gov/api/citations/1/downloads/1:
