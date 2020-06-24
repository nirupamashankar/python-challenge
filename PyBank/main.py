#import os and csv 
import os
import csv


# define path for csv file
csvpath = os.path.join("Resources", "Budget_data.csv")

#create lists to store reqd data
month = []
profit_loss = []
profitloss_change = []
average_change = []
greatest_increase = {} 
greatest_decrease = {}
ind = 0  

#open reqd file, file has a header
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv.header = next(csvreader)

    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

#calculate number of months
month_count = len(month)

#calculate net profit/loss
    
total_profitloss = sum(profit_loss)

# calculate month to month change in profit/loss and store value
for ind, v in enumerate(profit_loss):
        if ind +1 < month_count:
            x = (profit_loss[ind+1] - v)
            profitloss_change.append(x)

#calculate average change
average_change = round(sum(profitloss_change)/(month_count - 1), 2)

#calculate maximum increase and decrease
greatest_increase = max(profitloss_change)
greatest_decrease = min(profitloss_change)

#locate index of month - reset index to correct for previous index change
Max_month = profitloss_change.index(greatest_increase) +1 
Min_month = profitloss_change.index(greatest_decrease) +1

#print all calculations in required format
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: {total_profitloss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month[Max_month]} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month[Min_month]} (${greatest_decrease})")

#create text file
f = open("Financial_ananlysis.txt", "x")

#write to text file
f.write("Financial Analysis\n")
f.write("-----------------------------\n")
f.write(f"Total Months: {month_count}\n")
f.write(f"Total: {total_profitloss}\n")
f.write(f"Average Change: ${average_change}\n")
f.write(f"Greatest Increase in Profits: {month[Max_month]}\n")
f.write(f"Greatest Decrease in Profits: {month[Min_month]}\n")
