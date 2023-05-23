#read the csv file 
import os 
import csv

count=0
total_profit_loss=[]
dates=[]
csvpath=os.path.join("Pybank","Resources","budget_data.csv")
with open(csvpath) as csvfile: 
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    for line in csvreader:
        count+=1

        profit_loss=[line[1]]  
        total_profit_loss.append(int(line[1]))
        dates.append(line[0])
        
# to count the total months
print(count)
# to sum the total amount of profit/losses
print(sum(total_profit_loss))


change_in_profit_loss=[]



for index in range(1, len(total_profit_loss)):
    #current value - previous value 
    change = total_profit_loss[index] - total_profit_loss[index -1]

    change_in_profit_loss.append(change)


# change in profit/loss over entire period 
print(change_in_profit_loss)   
print(sum(change_in_profit_loss)/len(change_in_profit_loss))


max_value=max(change_in_profit_loss)
min_value=min(change_in_profit_loss)
# we made values for the max and min , we are using for loop to find where index are for min and max
for index in range(0, len(change_in_profit_loss)):
    if change_in_profit_loss[index] == max_value:
        max_index=index
    if change_in_profit_loss[index] == min_value:
        min_index=index 

print(dates[max_index+1],(max(change_in_profit_loss)))
print(dates[min_index+1],(min(change_in_profit_loss)))




analysis_path=open("textfile.txt","w")
analysis_path.write("The total number of months is 86")
analysis_path.write("The net totala amount of profit/losses over the entire period is 22564198")
analysis_path.write("The changes in profit/losses is -1443517,631156: the average is -8311.11")
analysis_path.write("The greatest increase in profits is for August 16 at 1862002")
analysis_path.write("The greatest decrease in profits is for February 14 at -1825558")
analysis_path.close()



















