#Write python program to read data from CSV, Excel, and Text located in local Machines. (Iris Dataset).
import pandas as pd

csv_data=pd.read_csv('C:/users/jashw/Desktop/PYTHON PROGRAMS/iris.csv')
print("CSV DATA: ",csv_data.head())
excel_data=pd.read_excel('C:/users/jashw/Desktop/PYTHON PROGRAMS/iris.xlsx')
print("EXCEL DATA: ",excel_data.head())
text_data=pd.read_csv('C:/users/jashw/Desktop/PYTHON PROGRAMS/iris.txt',sep='\t')
print("TEXT DATA: ",text_data.head())

