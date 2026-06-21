from sheets import get_users_sheet

sheet = get_users_sheet()

print(sheet.row_values(1))