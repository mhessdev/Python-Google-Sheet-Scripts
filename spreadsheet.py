#!/usr/bin/env python 

#allows you to get the spreadsheet i think https://gspread.readthedocs.io/en/latest/
import gspread 
#makes the print look nicer
import pprint 

#somthing for oauth
from oauth2client.service_account import ServiceAccountCredentials 


scope  = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] # not sure what scope does
creds  = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope) #connect credentials
client = gspread.authorize(creds) #this is the actualy api client

sheet  = client.open('Chloe Test').sheet1 #sets the sheet for the data

#variables
pp    = pprint.PrettyPrinter() # defines pretty printer so you can use it
#data = sheet.get_all_records() #gets all records
#data = sheet.row_values(2) #gets all values for a row of the sheet
#data = sheet.col_values(2) #gets all values for a col of the sheet
data  = sheet.cell(2, 2).value #gets value from single cell

#print for some reason returns like this [{u'Col 3': u'Data 3', u'Col 1': u'Data 1', u'Col 2 ': u'Data 2 '}]
#pprint returns like this [{u'Col 1': u'Data 1', u'Col 2 ': u'Data 2 ', u'Col 3': u'Data 3'}]
#not sure why pp returns the data in order i assume its somthing in the package
#but why would print not just do that by default

pp.pprint(data)

########
#this updates a cell
#sheet.update_cell(2, 2, 'NEW DATA')

#shows proof
#data  = sheet.cell(2, 2).value #gets value from single cell
#pp.pprint(data)
########

########
#creating row
row = ['NewData1', 'NewData2', 'NewData3'] #data to be set
index = 3 #sets the row that i should be inserted to
#sheet.insert_row(row, index) #inserts data (data, index of new row)
########

########
#deleting data
sheet.delete_row(3) #deletes the row via index
########








