import pandas as pd 

path = "/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts/"

months = ["AprilBreakout","MayBreakout","AugustBreakout","JuneBreakout","JulyBreakout"]

cols = []

for month in months:

    path_final = path+month

    df = df = pd.read_excel(path_final+ ".xls" , sheet_name= 'breakouts')


    cols.append(len(df.columns))
