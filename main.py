from dotenv import load_dotenv
import os
import requests
import pandas as pd
import pymysql

def main():
	''' GET ENVIRONMENT VARIABLES AND SECRETS '''
	load_dotenv() # Load .env
	dbhost = os.getenv('DBHOST', "")
	dbuser = os.getenv('DBUSER', "")
	dbpassword = os.getenv('DBPASSWORD', "")
	database = os.getenv('DATABASE', "")
	table = os.getenv('TABLE', "")

	''' DOWNLOAD & READ XLSX FILE '''
	file_name = './data/Financial Sample.xlsx'

	url = 'https://go.microsoft.com/fwlink/?LinkID=521962'
	downloaded_file = requests.get(url)
	open(file_name, 'wb').write(downloaded_file.content)

	xlsx_file = pd.ExcelFile(file_name)

	# Create dictionary to store data by sheet
	df = {sheet_name: xlsx_file.parse(sheet_name) for sheet_name in xlsx_file.sheet_names}

	# Transform to insert into MYSQL table
	df['Sheet1']['Date'] = df['Sheet1']['Date'].astype(str)

	# Create column list
	temp_list_col = df['Sheet1'].columns.tolist() # One sheet named 'Sheet1'
	list_col = [] 
	for col in temp_list_col:
		list_col.append(col.strip().replace(' ', '_').lower())
	cols = '`,`'.join([str(i) for i in list_col])

	''' CONNECT TO THE DATABASE '''
	connection = pymysql.connect(
		host=dbhost,
		user=dbuser,
		password=dbpassword,
		db=database)

	# Create cursor
	cursor = connection.cursor()

	# Insert DataFrame recrds one by one.
	for i, row in df['Sheet1'].iterrows():
		sql = 'INSERT INTO `'+table+'` (`'+cols +'`) VALUES ('+'%s,'*(len(row)-1)+'%s)'
		# row represents the data points in DataFrame
		cursor.execute(sql, tuple(row))
		
		# The connection is not autocommitted by default, so we must commit to save our changes
		connection.commit()

if __name__ == '__main__':
	main()
