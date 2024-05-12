import pandas as pd
import string
import matplotlib.pyplot as plt

#====================================

#get the average dataframe of average profit over time for each trader type
def average_data_6(numtrials,n_days,order_interval):

    data_frames = [] # list of all data frames we read from CSVs of all trials 

    newNames={ "B":"TIME", "C":"BID", "D":"ASK" ,"H":"GVWY", "L":"INSDP", "P":"SHVR", "T":"SNPR", "X":"ZIC","AB":"ZIP"}
    #reading all the dataframes
    for i in range(1,numtrials+1): # +1 to get the last trial e.g. 200
        
        trial_id = 'bse_d%03d_i%02d_%04d' % (n_days, order_interval, i)


        csv_str = trial_id +"_avg_balance.csv" # getting each CSV

        #need up to 28 columns for 6 traders
        avg_balance_trial = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:28] + ["AA","AB"],\
                         index_col=False)

        avg_balance_trial.rename(columns=newNames,inplace=True)
        
        data_frames.append(avg_balance_trial)
        
    pad_frames = pad_dataframes(data_frames)

    max_row = pad_frames[0].shape[0] # max row of the dataframe 
    #generating the average graph
    data_frame = pd.DataFrame(columns=pad_frames[0].columns) #new dataframe with same column structure
    for i in range(max_row):
        #getting average of columns B, H, L, P, T, X, AB
        average_row = get_average(i,pad_frames)
        data_frame.loc[i] = average_row
    return data_frame


def get_average(row_num,pad_frames):
    
    column_values = {"TIME":0,"BID":0,"ASK":0,"GVWY":0,"INSDP":0,"SHVR":0,"SNPR":0,"ZIC":0,"ZIP":0}
    
    #total of each column we care about to then make an average of all dataframes
    for frame in pad_frames:
        row = frame.loc[row_num]
        column_values["TIME"] += row["TIME"]
        column_values["BID"] += row["BID"]
        column_values["ASK"] += row["ASK"]
        column_values["GVWY"] += row["GVWY"]
        column_values["INSDP"] += row["INSDP"]
        column_values["SHVR"] += row["SHVR"]
        column_values["SNPR"] += row["SNPR"]
        column_values["ZIC"] += row["ZIC"]
        column_values["ZIP"] += row["ZIP"]
    
    divisor = len(pad_frames)

    for key in column_values:
        column_values[key] /= divisor # making each value an average
    
    #take first row to change
    row = pad_frames[0].loc[row_num]
    new_row = row.copy()
    #replacing the values with the averages now
    
    new_row["TIME"] = column_values["TIME"]
    new_row["BID"] = column_values["BID"]
    new_row["ASK"] = column_values["ASK"]
    new_row["GVWY"] = column_values["GVWY"]
    new_row["INSDP"] = column_values["INSDP"]
    new_row["SHVR"] = column_values["SHVR"]
    new_row["SNPR"] = column_values["SNPR"]
    new_row["ZIC"] = column_values["ZIC"]
    new_row["ZIP"] = column_values["ZIP"]
    # now returning an average row

    return new_row

# get average data of traders differentiated by 5 distance values
def average_data_distance(numtrials,n_days,order_interval):
    data_frames = [] # list of all data frames we read from CSVs of all trials 

    newNames={ "B":"TIME", "C":"BID", "D":"ASK" ,"H":"Distance_1", "L":"Distance_2", "P":"Distance_3", 
              "T":"Distance_4", "X":"Distance_5"}
    #reading all the dataframes
    for i in range(1,numtrials+1): # +1 to get the last trial e.g. 200
        
        trial_id = 'bse_d%03d_i%02d_%04d' % (n_days, order_interval, i)


        csv_str = trial_id +"_avg_balance.csv" # getting each CSV

        #need up to 28 columns for 6 traders
        avg_balance_trial = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:24],\
                         index_col=False)

        avg_balance_trial.rename(columns=newNames,inplace=True)
        
        data_frames.append(avg_balance_trial)
        
    pad_frames = pad_dataframes(data_frames)

    max_row = pad_frames[0].shape[0] # max row of the dataframe 
    #generating the average graph
    data_frame = pd.DataFrame(columns=pad_frames[0].columns) #new dataframe with same column structure
    for i in range(max_row):
        #getting average of columns B, H, L, P, T, X
        average_row = get_average_distance(i,pad_frames)
        data_frame.loc[i] = average_row
    return data_frame

def get_average_distance(row_num,pad_frames):
    column_values = {"TIME":0,"BID":0,"ASK":0,"Distance_1":0,"Distance_2":0,"Distance_3":0,
                     "Distance_4":0,"Distance_5":0}
    
    #total of each column we care about to then make an average of all dataframes
    for frame in pad_frames:
        row = frame.loc[row_num]
        column_values["TIME"] += row["TIME"]
        column_values["BID"] += row["BID"]
        column_values["ASK"] += row["ASK"]
        column_values["Distance_1"] += row["Distance_1"]
        column_values["Distance_2"] += row["Distance_2"]
        column_values["Distance_3"] += row["Distance_3"]
        column_values["Distance_4"] += row["Distance_4"]
        column_values["Distance_5"] += row["Distance_5"]
    
    divisor = len(pad_frames)

    for key in column_values:
        column_values[key] /= divisor # making each value an average
    
    #take first row to change
    row = pad_frames[0].loc[row_num]
    new_row = row.copy()
    #replacing the values with the averages now
    
    new_row["TIME"] = column_values["TIME"]
    new_row["BID"] = column_values["BID"]
    new_row["ASK"] = column_values["ASK"]
    new_row["Distance_1"] = column_values["Distance_1"]
    new_row["Distance_2"] = column_values["Distance_2"]
    new_row["Distance_3"] = column_values["Distance_3"]
    new_row["Distance_4"] = column_values["Distance_4"]
    new_row["Distance_5"] = column_values["Distance_5"]
    # now returning an average row

    return new_row


def pad_dataframes(data_frames):
    max_row = 0
    for data_frame in data_frames:
        row_size = data_frame.shape[0]-1# rows start at index 0
        if(row_size > max_row):
            max_row = row_size
    
    for i in range (0,len(data_frames)):
        data_frame = data_frames[i]

        row_size = data_frame.shape[0]-1
        if(row_size<max_row):
            remaining = max_row - row_size
            last_row = data_frame.iloc[-1] #last row
            new_rows = pd.DataFrame([last_row] * remaining) # create the remaining copies of last row
            #to fill in the dataframe
            new_df = pd.concat([data_frame,new_rows], ignore_index=True)
            data_frames[i] = new_df
    return data_frames


#draw a graph of best bid and ask over time
def bidAsk_time(numtrials,n_days,order_interval):

    for i in range(1,numtrials+1):
        
        csv_str = 'bse_d%03d_i%02d_%04d' % (n_days,order_interval, i) + '_avg_balance.csv'

        avgBalance = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:24],\
                         index_col=False)

        newNames = {"C":"BID", "D":"ASK"}
        avgBalance.rename(columns=newNames,inplace=True)

        avgBalance.plot(x="B",y=["BID","ASK"])
        plt.xlabel("Time")
        plt.title("Best Bid and Ask for 6 trader types, 5 sellers and 5 buyers each")
        plt.show(block=True)



def average_graph6(data_frame, time_delay_test=False, **kwargs):

    if(time_delay_test):
        data_frame.plot(x="TIME",y=["Distance_1","Distance_2","Distance_3","Distance_4","Distance_5"], kind="line")
        plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each with time delays. Showing effects on "+
                    "performance by distance to exchange")
    else:
        data_frame.plot(x="TIME",y=["GVWY","INSDP","SHVR","SNPR","ZIC","ZIP"], kind="line") 
        plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each")    

    plt.xlabel("Time")
    plt.ylabel("Average Profit")
    
    if(len(kwargs) > 0):
        for key,value in kwargs.items():
            if(key=="noise"):
                plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each with noise = {}".format(value))
            elif(key=="market_shock"):
                plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each with market shock")

    plt.show(block=True)

def average_equilibrium(data_frame, **kwargs):
    data_frame.plot(x="TIME",y=["BID","ASK"], kind="line")

    plt.xlabel("Time")
    plt.ylabel("Best Bid and Ask in system")

    if(len(kwargs) == 0):
        #normal graph without display effects of noise/uncertainty
        plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each")
    else:
        for key,value in kwargs.items():
            if(key=="market_shock"):
                plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each with market shock")
            elif(key=="time_delay_test"):
                plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each with time delays")

    plt.show(block=True)

# showing history of transactions, crossed graphs in pdf
def show_transactions():
    pass

def display_noise_expr(df_list):
    # have a list of df_s
    # for each trader -> model the 

    traders = ["GVWY","INSDP","SHVR","SNPR","ZIC","ZIP"]
    noise = ["no_noise","5_FR","5_RR","15_FR","15_RR"] # FR = fixed range, RR = random range
    for trader in traders:

        for i, df in enumerate(df_list):
            x = df["TIME"]
            y = df[trader]

            plt.plot(x,y, label=noise[i]) # plotting the performance for that trader at that level of noise
        
        plt.xlabel("Time")
        plt.ylabel("Performance")
        plt.title("Performance of {} with different levels of noise".format(trader))
        plt.legend()
        plt.show(block=True)

def display_noise_eq(df_list):
    # for each level of noise, display the equilibrium
    noise = ["no_noise","5_FR","5_RR","15_FR","15_RR"] # FR = fixed range, RR = random range

    for i, df in enumerate(df_list):
        df.plot(x="TIME",y=["BID","ASK"], kind="line")
        
        plt.xlabel("Time")
        plt.ylabel("Best Bid and Ask in system")
        plt.title("Average bid and ask over time for {} noise".format(noise[i]))
        plt.show(block=True)

#====================================