from Framework.utils import excel_utils

file = "F:\\SQA\\Batch10\\Projects\\AutomationBITM10\\Framework\\data\\test_data.xlsx"
sheet= "Sheet1"

print(excel_utils.row_count(file, sheet))
print(excel_utils.column_count(file,sheet))
print(excel_utils.read_data(file, sheet,2, 1))