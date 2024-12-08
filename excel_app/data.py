import openpyxl
from datetime import datetime
from openpyxl import Workbook, load_workbook
# Create a new workbook
wb = Workbook()
ws = wb.active
ws.title = "Products"
ws.append(["Name", "Fee in RS ", "class", "Age", "Grade"])
ws.append(["Nishan", 800, 8, 21, "A" ])
ws.append(["Ram", 1000,  10, 22, "B" ])
ws.append(["Samir", 1000, 10, 20, "A" ])
ws.append(["Satish", 800, 8, 21, "A" ])
ws.append(["Bijay", 800, 8, 19, "B" ])
ws.append(["Anish",1000, 10, 19, "C" ])
ws.append(["yuvraj", 1000, 10, 20, "B" ])
ws.append(["sandesh", 800, 8, 18, "C" ])
ws.append(["Bishal", 800, 8, 20, "A" ])
ws.append(["Rohit", 800, 8, 17, "B" ])
ws.append(["Sudip", 1000, 10, 19, "A" ])
wb.save('data.xlsx')