# Converts an input file into a saved json dict

import os
import json
import pandas as pd

if __name__ == '__main__':
    # Put in file and path here
    fid = ''
    path = r"C:\Users\zrr81\Downloads"
    
    # Change path, import to df, output columns
    os.chdir(path)
    df = pd.read_csv(fid, index_col=False)
    columns = (list(df.columns))
    # print(columns)
    # kill()
    
    # Load into dict
    data_dict = {}
    for index, row in df.iterrows():
        data_dict[row['merchant_uuid']] = row['merchant_name']
        
    # Save dict to file
    js_dict = json.dumps(data_dict)
    with open('merchant_map.json', 'w+') as f:
        f.write(js_dict)