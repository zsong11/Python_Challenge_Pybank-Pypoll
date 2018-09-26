import csv
import os

input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Analysis", "Analysis.txt")

month_count = 1
total = 0
end_balance = 0
dict_table = {}
monthly_change = []

with open(input_file) as data:
    table = csv.reader(data)
    header = next(table)
    first_row = next(table)

    total += float(first_row[1])
    end_balance = float(first_row[1])

    for row in table:
        month_count += 1
        total += float(row[1])
        
        change = float(row[1]) - end_balance
        end_balance = float(row[1])

        monthly_change += [change]
        dict_table[str(row[0])] = change

g_increase = max(monthly_change)
g_decrease = min(monthly_change)
average_change = sum(monthly_change) / (month_count - 1)

for k, v in dict_table.items():
    if v == g_increase :
        increase_text = k

for k, v in dict_table.items():
    if v == g_decrease :
        decrease_text = k

result = (
    f"\nFinancial Analysis\n"
    f"**************************************\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: ({increase_text}) (${g_increase})\n"
    f"Greatest Decrease in Profits: ({decrease_text}) (${g_decrease})\n")
 
print(result)

with open(output_file, "w") as txt_file:
    txt_file.write(result)
        

