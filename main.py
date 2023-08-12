import pandas as pd
import finviz

# Read the CSV file containing premarket trading data for a specific date
DF = pd.read_csv(f'america_2023-08-11.csv')

# Create a list of tickers from the 'Ticker' column of the DataFrame
tickerlist = list(DF.Ticker)

# Initialize an empty list to store stock data dictionaries
mylst = []

# Initialize counters for progress tracking
counter = 0
maxiter = DF.shape[0]

# Loop through each ticker in the ticker list
for ticker in tickerlist:
    counter += 1

    # Print progress information
    print(f"{counter} out of {maxiter}  -  {ticker}")

    try:
        # Attempt to retrieve stock data from finviz
        mydict = finviz.get_stock(ticker)
        mylst.append(mydict)
    except:
        # If an error occurs, retry once before skipping and printing an error message
        try:
            mydict = finviz.get_stock(ticker)
            mylst.append(mydict)
        except:
            # Print an error message if both attempts fail
            print('***ERROR')
            pass

# Create a DataFrame from the collected stock data dictionaries
DFtotal = pd.DataFrame(mylst)

# Save the first 78 columns of the DataFrame to a CSV file
DFtotal.iloc[:, 0:78].to_csv('finviz.csv')
