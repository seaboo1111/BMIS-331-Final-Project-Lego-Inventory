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
  lego_df.replace(r"^\s*$", np.nan, regex=True, inplace=True)
  # Drop rows with any NaN values to remove mostly blank rows
  lego_df.dropna(inplace=True)

def save_new_csv(lego_inventory_df):
    lego_inventory_df.to_csv("lego_sets_inventory.csv", index=False)

# Load the Lego and lego inventory CSV file as data frame
lego_df = pd.read_csv("lego_sets_and_themes.csv")
lego_inventory_df = pd.read_csv("lego_sets_inventory.csv")
#prints curent inventory
print("Lego Inventory")
print(lego_inventory_df)

# calls fuction to remove unneeded url column
remove_url_column()

# calls fuction to remove mostly blank rows
remove_mostly_blank_rows()

# sort lego df and lego inventory df by theme ascending
lego_df = lego_df.sort_values("theme_name", ascending = True)

# prints the list of all lego sets
print("list of all lego sets")
print(lego_df)



# This initializes The main loop so that sets can be added to the lego inventory
done = "no"

while done != "yes":
  # checks if user wants to remove or add from inventory
  add_or_remove = input("Do you want to add or remove set from inventory? type add or remove ").lower()
  # to add a row to the inventory
  if add_or_remove == "add":
    # Asks the user which set number they want added to the inventory.
    set_number = input("What's that number would you like to add? Don't forget to add the sub number at the end -# ")
    # locates the set in lego_df
    entry = lego_df.loc[lego_df['set_number'] == set_number]
    # adds the row with the set number to inventory
    lego_inventory_df = pd.concat([lego_inventory_df, entry])
    # Print the updated lego inventory
    print(lego_inventory_df)
    # save the updated lego inventory
    save_new_csv(lego_inventory_df)

  # to remove a row from the inventory
  elif add_or_remove == "remove":
    # These lines remove the item from inventory
    set_number = input("What's that number would you like to remove? Don't forget to add the sub number at the end -# ")
    lego_inventory_df = lego_inventory_df.drop(lego_inventory_df[lego_inventory_df['set_number'] == set_number].index)
    # Print the updated lego inventory
    print(lego_inventory_df)
    # save the updated lego inventory
    save_new_csv(lego_inventory_df)

  # print if user does a cmd beside add and remove.
  else:
    print("invalid input")
  # This checks if the user is done
  done = input("Are you done entering lego sets into the inventory? yes or no ").lower()

# prints the inventory for the final time before closing program
print(lego_inventory_df)