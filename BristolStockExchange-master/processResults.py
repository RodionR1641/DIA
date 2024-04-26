import pandas as pd
import string
import matplotlib.pyplot as plt

print(list(string.ascii_uppercase)[0:24])

#draw a graph of average profit over time for each trader type
def average_profit5(numtrials):

    for i in range(1,numtrials+1):

        csv_str = "bse_d000_i05_{}_avg_balance.csv".format("000"+str(i))

        avgBalance = pd.read_csv(csv_str,header=None,\
                         names=list(string.ascii_uppercase)[0:24],\
                         index_col=False)

        newNames = { "H":"GVWY", "L":"INSDP", "P":"SHVR", "T":"ZIC", "X":"ZIP"}
        #newNames = {"H":"ZIP"}
        avgBalance.rename(columns=newNames,inplace=True)
        avgBalance.plot(x="B",y=["GVWY","INSDP","SHVR","ZIC","ZIP"], kind="line")
        #avgBalance.plot(x="B",y=["ZIP"])
        plt.xlabel("Time")
        plt.ylabel("Average Profit")
        plt.title("62 ZIP traders over 180 seconds")
        plt.show(block=True)

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

# showing history of transactions, crossed graphs in pdf
def show_transactions():
    pass

#average_profit5(2)
bidAsk_time(1)