import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

with open('updated_rank.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

with open('links.dat', newline='') as csvfile:
    input_file = list(csv.reader(csvfile))



scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name(input_file[0][0], scope)

docid = input_file[1][0]

client = gspread.authorize(credentials)
ss = client.open_by_key(docid)


ss.values_update(
    'Resultado_Programa!A1', 
    params={'valueInputOption': 'RAW'}, 
    body={'values': data}
)

link = 'https://docs.google.com/spreadsheets/d/'+docid+'/'
print('Link da planilha atualizada: {}'.format(link))

