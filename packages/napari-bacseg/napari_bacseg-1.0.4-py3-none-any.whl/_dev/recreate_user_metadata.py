# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:35:20 2023

@author: turnerp
"""


import pandas as pd
import pathlib

path = r"\\physics\dfs\DAQ\CondensedMatterGroups\AKGroup\Piers\AKSEG\Images\PT\PT_file_metadata.txt"


meta = pd.read_csv(path, sep= ",", dtype=object)


# user_meta = {column: meta[column].unique().tolist() for column in meta.columns if "meta" in column}



# user_initial = "PT"
# database_name = "AKSEG"
# database_directory = "\\physics\dfs\DAQ\CondensedMatterGroups\AKGroup\Piers\AKSEG"


# txt_meta_path = r"\\physics\dfs\DAQ\CondensedMatterGroups\AKGroup\Piers\AKSEG\Metadata\AKSEG User Metadata [PT].txt"

# print(txt_meta_path)

# txt_meta = f"# {database_name} User Metadata: {user_initial}\n"

# for key, value in user_meta.items():
    
#     txt_meta += f"\n# User Meta [{key.replace('user_meta', '')}] (add new entries below):"

#     for item in value:
#         txt_meta += f"\n{item}"

#     txt_meta += "\n"


#     with open(txt_meta_path, "w") as f:
#         f.write(txt_meta)
