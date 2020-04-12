import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

breakout_index = 0
prev_breakout_index = 0
num_samples = 180
path = "/home/shreyas/Documents/Final_year/finalyear/datasets/All_data/Final_data/May/"
month = "may"
filename_breakout = path + "normalized_breakouts_" + month + ".xls"

#filename_goodcast = path + "normalized_goodcasts_" + month + ".xls"
#filename_aug = "normalized_breakout_aug.xls"

sample = 0
num_intervals_gc = 0
num_intervals_bo = 0

def split_goodcast(filename, num_intervals_gc):
    data = pd.read_excel(filename)
    data = pd.DataFrame(data)
    data = data.values.tolist()

    nan_index = [-1]
    sizes = []
    data_required = []

    for i in range(0,len(data)):
        if(np.isnan(data[i][0])):
            nan_index += [i]

    for i in range(0, len(nan_index)-1):
        sizes += [nan_index[i+1] - nan_index[i] - 2]

    for i in range(1,len(nan_index)):
        print(i)
        for index in range(nan_index[i-1]+1, nan_index[i],10):
            print(index)
            if(nan_index[i] == index + 1):
                continue
            data_required = data[index:index+10]
            num_intervals_gc += 1
            pd.DataFrame(data_required).to_csv(path + "10_normalized_goodcasts/"  + str(num_intervals_gc) + ".csv", header=False, index=False)

    for index in range(nan_index[-1] + 1, nan_index[-1] + 1 + 1200, 10):
        data_required = data[index:index+10]
        num_intervals_gc += 1
        pd.DataFrame(data_required).to_csv(path + "10_normalized_goodcasts/" + str(num_intervals_gc) + ".csv", header=False, index=False)

def split_breakout_to_180_samples(breakout_index, num_samples, filename, num_intervals_bo):
    data = pd.read_excel(filename)
    data = pd.DataFrame(data)
    data_refined = data.values.tolist()

    for i in range(0,len(data)):
        try:
            data_val = [round(data_refined[i][0]), round(data_refined[i+1][0]), data_refined[i+2][0], data_refined[i+3][0]]
            if((data_val[0] - data_val[1] >=1)):
                prev_breakout_index = breakout_index
                breakout_index = i
                if(breakout_index-10>0 and (breakout_index - prev_breakout_index >500)):    #Check for breakout index being too close and getting non repeating values
                    num_intervals_bo += 1
                    new_samples = data_refined[(breakout_index - 10 - num_samples):(breakout_index - 10)]
                    pd.DataFrame(new_samples).to_csv(path + "10_normalized_breakouts/"+ str(num_intervals_bo) + ".csv", header=False, index=False)
                    print("yo", len(new_samples), str(breakout_index - 10 - num_samples), str(breakout_index-10))

        except ValueError:
            continue

        except IndexError:
            continue


def split_breakout_to_30_samples(sample):
    for i in range(1,7):
        data = pd.read_csv("normalized/" + month + "/breakouts_groups/" + str(i) + ".csv", header=None)
        data = pd.DataFrame(data)

        data_refined = data.values.tolist()

        for row in range(0,len(data_refined),10):
            if(len(data_refined[row:row+30])!=30):
                continue
            else:
                sample += 1
                row_sample = data_refined[row:row+30]
                pd.DataFrame(row_sample).to_csv("normalized/" + month + "/breakouts/" + str(sample) + ".csv", header=False, index=False)

def split_breakout_to_10_samples(sample):
    for i in range(1,4):
        data = pd.read_csv(path + "10_normalized_breakouts/"+ str(i) + ".csv", header=None)
        data = pd.DataFrame(data)

        data_refined = data.values.tolist()

        for row in range(0,len(data_refined),4):
            if(len(data_refined[row:row+10])!=10):
                continue
            else:
                sample += 1
                row_sample = data_refined[row:row+10]
                pd.DataFrame(row_sample).to_csv(path + "check/"  + str(sample) + ".csv", header=False, index=False)

if(__name__=='__main__'):
    #split_goodcast(filename_goodcast, num_intervals_gc)
    split_breakout_to_180_samples(breakout_index, num_samples, filename_breakout, num_intervals_bo)
    split_breakout_to_10_samples(sample)
