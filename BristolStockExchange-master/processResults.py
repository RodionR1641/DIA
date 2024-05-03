import pandas as pd
import string
import matplotlib.pyplot as plt

print(list(string.ascii_uppercase)[0:24])

df = None # global dataframe of average values

#get the average dataframe of average profit over time for each trader type
def average_data_6(numtrials,n_days,order_interval):

    data_frames = [] # list of all data frames we read from CSVs of all trials 
    newNames = { "B":"TIME", "C":"BID", "D":"ASK" ,"H":"GVWY", "L":"INSDP", "P":"SHVR", "T":"SNPR", "X":"ZIC", "AB":"ZIP"}

    #reading all the dataframes
    for i in range(1,numtrials+1):
        
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
    global df
    df = pd.DataFrame(columns=pad_frames[0].columns) #new dataframe with same column structure
    for i in range(max_row):
        #getting average of columns B, H, L, P, T, X, AB
        average_row = get_average(i,pad_frames)
        df.loc[i] = average_row


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
    
    #take any row to change
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

def average_profit4(numtrials):
    for i in range(1,numtrials+1):

        csv_str = "bse_d000_i05_{}_avg_balance.csv".format("000"+str(i))

        avgBalance = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:24],\
                         index_col=False)

        newNames = { "H":"GVWY", "L":"SHVR", "P":"ZIC", "T":"ZIP"}
        #newNames = {"H":"ZIP"}
        avgBalance.rename(columns=newNames,inplace=True)
        avgBalance.plot(x="B",y=["GVWY","SHVR","ZIC","ZIP"], kind="line")
        #avgBalance.plot(x="B",y=["ZIP"])
        plt.xlabel("Time")
        plt.ylabel("Average Profit")
        plt.title("62 ZIP traders over 180 seconds")
        plt.show(block=True)


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
def bidAsk_time(numtrials):

    for i in range(1,numtrials+1):
        
        csv_str = "bse_d000_i05_{}_avg_balance.csv".format("000"+str(i))

        avgBalance = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:24],\
                         index_col=False)

        newNames = {"C":"Bid", "D":"Ask"}
        avgBalance.rename(columns=newNames,inplace=True)

        avgBalance.plot(x="B",y=["Bid","Ask"])
        plt.xlabel("Time")
        plt.title("Best Bid and Ask for 62 ZIP traders")
        plt.show(block=True)

def average_graph6():


    df.plot(x="TIME",y=["GVWY","INSDP","SHVR","SNPR","ZIC","ZIP"], kind="line") 

    plt.xlabel("Time")
    plt.ylabel("Average Profit")
    plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each")
    plt.show(block=True)

def average_equilibrium6():
    df.plot(x="TIME",y=["BID","ASK"], kind="line")

    plt.xlabel("Time")
    plt.ylabel("Best Bid and Ask in system")
    plt.title("500 runs of 6 trader types, 5 sellers and 5 buyers each")
    plt.show(block=True)

# showing history of transactions, crossed graphs in pdf
def show_transactions():
    pass

average_data_6(100,0.01,5)
average_graph6()
average_equilibrium6()
#average_profit6(100,0.01,5)
#bidAsk_time(1)