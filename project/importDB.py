import openpyxl
# import sqlalchemy


def org():
	pass
def team():
	pass
def individual():
	pass

import sqlite3
con = sqlite3.connect("QuizSite0.3/project/db.sqlite")
cur = con.cursor()

	

# from . import db

wbook = openpyxl.load_workbook('QuizSite0.3/project/DB.xlsx', data_only=True)

# Populate Org
'''worksheet = wbook['Orginization']
isFirst = True
entries = []
for record in worksheet.rows:
	if isFirst:
		isFirst = False	
	elif record[0].value!=None:
		entries += [[cell.value for cell in record[:4]]]

sql = 'INSERT INTO orginization VALUES\n'
for entry in entries:
	sql = sql + f"""({entry.pop(0)}, "{entry.pop(0)}", "{entry.pop(0)}", "{entry.pop(0)}"),\n"""

cur.execute(sql[:-2])
'''


# Populate Team
worksheet = wbook['Team']
isFirst = True
entries = []

# Populate Indiviual

config = [
	{
		'func':org,
		'wbook':wbook['Orginization'],
		'recordlen':4
		

	}
]


for table in config:
	worksheet = table['wbook']
	isFirst = True
	entries = []
	for record in worksheet.rows:
		if isFirst:
			isFirst = False	
		elif record[0].value!=None:
			entries += [[cell.value for cell in record[:table['recordlen']]]]

con.commit()





# # worksheet = openpyxl.load_workbook('DB.xlsx').active

# itemData = None
# countData = None

# combinedData = []

# output = {}

# for column in worksheet.columns:
# 	if column[0].value == item_column:
# 		itemData = column
# 	elif column[0].value == count_column:
# 		countData = column

# if itemData == None:
# 	print(f"\nThe column with header '{item_column}' was not found in {filename}.\n")
# 	exit()
# elif count_column == None:
# 	print(f"\nThe column with header '{count_column}' was not found in {filename}.\n")
# 	exit()

# # Is there a method for this?
# for row in range(len(itemData)):
# 	try:
# 		data = [str(itemData[row].value), float(countData[row].value)]
# 		combinedData += [data]
# 	except:
# 		pass

# for row in combinedData:
# 	try:
# 		output[row[0]] += row[1]
# 	except:
# 		output[row[0]]  = row[1]

# print(f'{item_column},{count_column}')

# for key in sorted(output):
# 	print(f'{key},{int(output[key])}')
