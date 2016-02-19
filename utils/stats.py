from openpyxl import Workbook

wb = Workbook()
ws = wb.active

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
headers = ['Threads', 'Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5', 'Average']

for i in range(7):
	ws[columns[i]+'1'] = headers[i]

wb.save("tst.xlsx")