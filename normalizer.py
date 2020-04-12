import pandas as pd 
import numpy as np 


count=0

month = "June"

path_aug_goodcasts = "/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Goodcasts/"+month+"Goodcasts.xls"
path_aug_breakouts = "/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts_LFCcorner/Breakouts_" + month +  ".xls"

"""path_june_goodcasts = "/home/shreyas/College/Project/filtered_data_goodcasts_June.xls"
path_june_breakouts = "/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts/JuneBreakout.xls"
"""
data_aug_goodcasts = pd.read_excel(path_aug_goodcasts)
data_aug_breakouts = pd.read_excel(path_aug_breakouts)

"""data_june_goodcasts = pd.read_excel(path_june_goodcasts)
data_june_breakouts = pd.read_excel(path_june_breakouts)"""


"""max_vals_goodcasts_may  =  data_may_goodcasts.max()
max_vals_breakouts_may =  data_may_breakouts.max()"""

max_vals_goodcasts_aug =  data_aug_goodcasts.max(axis=0)
max_vals_breakouts_aug =  data_aug_breakouts.max()


"""
min_vals_goodcasts_may  =  data_may_goodcasts.min()
min_vals_breakouts_may =  data_may_breakouts.min()"""

min_vals_goodcasts_aug =  data_aug_goodcasts.min()
min_vals_breakouts_aug =  data_aug_breakouts.min()



range_vals = []

max_val_feature = []
min_val_feature = []

for i in range(len(max_vals_breakouts_aug)):

    max_val = max(max_vals_breakouts_aug[i],max_vals_goodcasts_aug[i])
    min_val = min(min_vals_breakouts_aug[i],min_vals_goodcasts_aug[i])

    range_vals.append(max_val-min_val)

    max_val_feature.append(max_val+ 0.2*(max_val-min_val))
    min_val_feature.append(min_val - 0.2*(max_val-min_val))

maximum = np.array(max_val_feature)
minimum = np.array(min_val_feature)


"""applied_good_may = data_may_goodcasts.apply(lambda x: (2*x -maximum-minimum)/(maximum-minimum),axis=1)
applied_breakout_may = data_may_breakouts.apply(lambda x:(2*x -maximum-minimum)/(maximum-minimum),axis=1)
"""

applied_good_aug = data_aug_goodcasts.apply(lambda x:(2*x -maximum-minimum)/(maximum-minimum),axis=1)
applied_breakout_aug = data_aug_breakouts.apply(lambda x:(2*x -maximum-minimum)/(maximum-minimum),axis=1)



"""applied_good_may.to_excel("/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts/normalized_goodcasts_may_.xls",index = False)
applied_breakout_may.to_excel("/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts/normalized_breakouts_may.xls",index = False)
"""

applied_good_aug.to_excel("/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts_LFCcorner_normalized/normalized_goodcasts_" + month+".xls",index = False)
applied_breakout_aug.to_excel("/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Breakouts_LFCcorner_normalized/normalized_breakout_"+month+".xls",index = False)



