#Import necessary libraries and modules
import csv
from communication import *
from message import *

# Initialize a communication instance
com=Communication() 
topic0=topic_msg()

#Open the CSV file and write the header row to the CSV file
csvfile_w=open('logger.csv', 'w', newline='')
writer = csv.DictWriter(csvfile_w, fieldnames=['number','data'])
writer.writeheader()  

#Write data to the CSV file
count=0        
while count<200:
    if com.update_topic==True:
        com.update_topic= False
        topic0.decode(com.msg_topic)
        data=topic0.temperature
        print('data',data)
        writer.writerow({'number':count,'data':data})
        count=count+1

#Close the CSV file 
csvfile_w.close()



