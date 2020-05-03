#3 output


import xlwt
from xlwt import Workbook

As = (7888.1)

wb = Workbook(encoding='utf-8')

for i in range(1,3):
    name = str('floor'+str(i))
    sheet= wb.add_sheet(name)
    sheet.write(1,0,"dierhangdiyilie")

wb.save('trythis.xls')
