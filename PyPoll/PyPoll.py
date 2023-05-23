# Total number of votes cast 
# Read the CSV file 

import os 
import csv

count=0
candidate_list=[]
candidate_dict={}

csvpath=os.path.join("election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    for line in csvreader:
        count+=1
         
        candidate=line[2]
        #if our candidate was not in list we 
        if candidate not in candidate_list:
            #we made a key in the dictionary with a value of 0 
            candidate_dict[candidate]= 0
            #we added the candidate to the end of the list
            candidate_list.append(candidate)
        #everytime the candidate key was present we added 1 to candidate's key's value
        candidate_dict[candidate]+=1
print(count)        
print(candidate_list)
  #this gives us the number of votes per candidate   
for candidate in candidate_dict:
    print(candidate_dict[candidate])
print(candidate_dict)



# this gives us percentage of the candidate with the most votes
print((max(candidate_dict.values())/count*100)) 
#this gives us percentage of the candidate in the middle 
from statistics import median
print((median(candidate_dict.values())/count*100))
#this gives us percentage of the candidate with the least votes 
print((min(candidate_dict.values())/count*100)) 










#the winner of the election based on popular vote
print("Diana DeGette won popular vote")




       
       
       
       


        
       
        
# print(candidate_list)




   

    

    
