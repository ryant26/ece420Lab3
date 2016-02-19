from openpyxl import Workbook
import common

wb = Workbook()
ws = wb.active

columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
headers = ['Threads', 'Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5', 'Average']

# Setup Headers
for i in range(7):
	ws[columns[i]+'1'] = headers[i]

common.run_datagen(5)
common.run_main(5)
print("runtime: ",common.get_runtime())
common.cleanup()


wb.save("stats.xlsx")