'''
    ---------------------------------------------------------------------------
    OpenCap processing: batchDownload.py
    ---------------------------------------------------------------------------

    Copyright 2022 Stanford University and the Authors
    
    Author(s): Antoine Falisse, Scott Uhlrich
    
    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use this file except in compliance with the License. You may obtain a copy
    of the License at http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from utils import download_session
import os

# List of sessions you'd like to download. They go to the Data folder in the 
# current directory.

sessionList = ['8c4c4d76-7207-427f-aa9f-68b35d68e314']

import pandas as pd 

dataframe = pd.read_csv('./Data/OpenCap-Data-Links-Master-Sheet1.csv')
ppe_keys = dataframe['e'].str.contains("PPE1008") == True  
ppe_values = dataframe[ppe_keys]
links = list(ppe_values['Link'])

sessionList = [link.split('/')[-1] for link in links]

# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'OtherData')

for session_id in sessionList:
    
    datapath = os.path.join(downloadPath,"OpenCapData_" + session_id)

    if os.path.exists(datapath):
        continue

    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    try: 
        download_session(session_id,sessionBasePath=downloadPath,downloadVideos=True)
    except Exception as e:
        print(f"Couldn't donwload:{session_id} Err:{e}") 