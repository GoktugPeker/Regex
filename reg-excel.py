import openpyxl
import re

workbook=openpyxl.load_workbook(r"C:\Users\peker\Desktop\Regex\Regex\Employees.xlsx")

# print(workbook.sheetnames)

sheet=workbook["EmployeeData"]
# print(sheet.dimensions)


# for row in sheet.values:
#     print(row)


data=[]
for row in sheet.values:
    a,b,c,d,e,f,g=row
    data.append(f"{a};{b};{c};{d};{e};{f};{g}")

# print(data)

employees="\n".join(data)

print(employees)



