# f. Write all the output to a text file at location: /home/output/result.txt 
# (inside your container).
import sys

stdoutOrigin=sys.stdout 
sys.stdout = open("/home/data/result.txt", "w")


#importing libraries
import os
from collections import Counter
# a. List name of all the text file at location: /home/data
addr = "/home/data/"
list = os.listdir(addr)
    
print("Files at Location: ", addr, 'are: ')
print(list)

# b. Read the two text files and count total number of words in each text files


total_words =0
words_file1 = 0
words_file2 = 0

with open('/home/data/IF.txt', 'r') as file:
    for line in file:
        words = line.split()
        words_file1 += len(words)
print('Number ofwords in IF.txt is',words_file1)

print('\n')
with open('/home/data/Limerick-1.txt', 'r') as file:
    for line in file:
        words = line.split()
        words_file2 += len(words)
print('Number ofwords in Limerick.txt is',words_file2) 

total_words = words_file1 + words_file2
print("Number of words:")
print(total_words)


# d. List the top 3 words with maximum number of counts in IF.txt.  
# Include the word counts for the top 3 words.

print("\n Top 3 words in IF.txt")
most_occur=0
Counter_dict = {}
with open('/home/data/IF.txt', 'r') as file:
    data = file.read()
    split_it = data.split()
    Counter_dict = Counter(split_it)
    most_occur = Counter_dict.most_common(3)
print(most_occur)


# e. Find the IP address of your machine
print('\n')
import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr)   



# f. Write all the output to a text file at location: /home/output/result.txt 
# (inside your container).
sys.stdout.close()
sys.stdout=stdoutOrigin

# g. Upon running your container, it should do all the above stated steps and print 
# the information on console from result.txt file and exit.


# os.mkdir('/home/output/') #### this command for creating directory
# os.system('touch /home/output/result.txt')

# import sys
# with open('/home/output/result.txt', 'r') as f:
#     contents = f.read()
#     print(contents)