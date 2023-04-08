# import the pandas library
import pandas as pd
# import the os library
import os

# set the directory where the files are located
directory = './'

# loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx'):
        # read the Excel file
        df = pd.read_excel(os.path.join(directory, filename))

        # drop any rows with all NaN values
        df.dropna(how='all', inplace=True)

        # save the updated dataframe to a new Excel file
        df.to_excel(os.path.join(directory, 'updated_' + filename), index=False)
