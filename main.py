import pandas as pd 
import requests
ids = pd.read_csv('ids.csv')
def do(x):
    res = requests.get(f"https://ntrs.nasa.gov/api/citations/{x}/downloads/{x}.txt")
    if res.status_code==200:
        with open(f"Data/{x}.txt",'w') as f:
            f.write(str(res._content))
ids['ids'].apply(do)
# https://ntrs.nasa.gov/api/citations/1
# https://ntrs.nasa.gov/api/citations/1/downloads
# https://ntrs.nasa.gov/api/citations/1/downloads/1