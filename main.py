#import datetime for date calculations
from datetime import datetime, date

# Import pandas module to process csv files
import pandas as pd

# Import regex module - regex built using https://regex-generator.olafneumann.org/
import re

def useRegex(input):
    pattern = re.compile(r"[a-zA-Z]+([0-9]+(-[0-9]+)+)")
    return pattern.match(input)


# ask user to input csv file --- commented out for testing with line 18
# print('enter file path to csv file')
# filePath = input()
# myCSV = pd.read_csv(filePath)

# declare csv file and read via pandas.read_csv
myCSV = pd.read_csv('WW-DLMBA-180322.csv')
# create variable that lists external id column as a dataframe in pandas
# df = pd.DataFrame(myCSV, columns=['External Id'])
# or....
# create dataframe with everything in 
df = pd.DataFrame(myCSV)



''' 
This function validates the external ID column. 
It uses regex to check correct format and then checks date section is in the future
'''

def validateExternalID(dataframe):
  for column, row in dataframe.items(): #iterate through columns and rows in df
  # print(f"column: {column}")
    if column == 'External Id': # checks string data for each column to find the ex id column
      #print(len(row)) # print statement just to catch how many rows and make sure the below results are enough
      for idx in range(0,len(row)): # iterates through each row in the table - idx is the number and we use range from 0 - to the length(or amount) of rows in the table
        # print(idx)  # prints index number of row

        # print(useRegex(row[idx]))

        if useRegex(row[idx]) is None:
          print("Invalid External ID")
        else:
          print("Valid External ID entered...")
          print(row[idx]) # prints row information at given index
          validateDate(row[idx])

    else: # else statement to close for loop
      print("something went wrong")
      # print(f"row: {row}")
      break

'''
This function is used inside the validateExternalID function to parse and check the dates are valid
'''

def validateDate(externalID):

  #define variable and slice date string from external id
  idDate = externalID[6:12]

  # print(f"idDate is {idDate}")

  #parse string to date string
  dateObject = datetime.strptime(idDate, "%d%m%y")
  # print(f"Converted date is {dateObject}")
  #todays date for comparison
  today = datetime.now()

  '''  
  Check if booking is in the past and print result. 
  Better way to do this is a try, except statement which would throw up an error if date is invalid.
  '''

  if dateObject.date() >= today.date():
    print("Booking is for the future, valid.")
  else:
    print(dateObject.date())
    print(f"Booking is in the past. {externalID} is invalid.")




validateExternalID(df)
