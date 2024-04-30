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

def save_new_csv(lego_inventory_df):
    lego_df.to_csv('lego_sets_inventory.csv', index=False)

# Load the Lego CSV file as data frame
lego_df = pd.read_csv('lego_sets_and_themes.csv')



# calls fuction to remove unneeded url column
remove_url_column()

# calls fuction to remove mostly blank rows
remove_mostly_blank_rows()

# prints the list of all lego sets
print(lego_df)

# sort lego df by theme ascending
lego_df = lego_df.sort_values("theme_name", ascending = True)

# This initializes the data frame so that that is has header data in it
lego_inventory_df = pd.DataFrame(columns=["set_number", "set_name", "year_released", "number_of_parts", "theme_name"])

# This initializes The main loop so that sets can be added to the lego inventory7
done = "no"
while done != "yes":
  # Asks the user which set number they want added to the inventory.
  set_number = input("What's that number would you like to add? Don't forget to add the sub number at the end -# ")
  # locates the set in lego_df
  entry = lego_df.loc[lego_df['set_number'] == set_number]
  # adds the row with the set number to inventory
  lego_inventory_df = pd.concat([lego_inventory_df, entry])
  # Print the updated lego inventory
  print(lego_inventory_df)
  # Print the updated lego inventory
  save_new_csv(lego_inventory_df)
  # This checks if the user wants to stop adding to the inventory
  done = input("Are you done entering lego sets into the inventory? yes or no ").lower()

print(lego_inventory_df)