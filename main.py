import openpyxl
wb = openpyxl.load_workbook('Юнимед.xlsx')
ws = wb['Лист1']

observation = {}
codes = ''

for i in range(2, ws.max_row):
    codes = codes + '\'' + ws.cell(i, 1).value + '\', '
    observation[ws.cell(i, 1).value] = ws.cell(i, 2).value

with open('Юнимед.txt', 'w') as f:
    f.write(codes[:-2])

print(observation['10-002'])

