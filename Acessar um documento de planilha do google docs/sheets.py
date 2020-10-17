import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]


creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

client = gspread.authorize(creds)

sheet = client.open("documento").sheet1

data = sheet.get_all_records()

row = sheet.row_values(2)
col = sheet.col_values(2)
print(col)

cell = sheet.cell(2,3).value

print(cell)

insertRow = ["1", "web", "ementa"]

sheet.update_cell(3,1, "7")



