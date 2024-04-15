#import libraies that we need for the project.
import pandas as pd
import numpy as np

# function for removing the url column
def remove_url_column():
  # Specify the url column to be removed
  column_to_remove = 'image_url'
  # Remove the url column
  lego_df.drop(column_to_remove, axis=1, inplace=True)

# This function removes mostly blank rows when called
def remove_mostly_blank_rows():
  # Replace blank spaces with NaN to remove mostly blank rows them
  lego_df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
  # Drop rows with any NaN values to remove mostly blank rows
  lego_df.dropna(inplace=True)

def save_new_csv(lego_df):
    lego_df.to_csv('lego_sets_inventory.csv', index=False)

# Load the Lego CSV file as data frame
lego_df = pd.read_csv('lego_sets_and_themes.csv')

# calls fuction to remove unneeded url column
remove_url_column()

# calls fuction to remove mostly blank rows
remove_mostly_blank_rows()

# sort lego df by theme ascending
lego_df = lego_df.sort_values('theme_name', ascending = True)


# Print the new lego dataframe
print(lego_df)

