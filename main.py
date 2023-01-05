#!/usr/bin/env python


from os.path import exists as file_exists
import hashlib
import re
import os
import configparser
import sys

config = configparser.ConfigParser()
config.read("config.ini")
settingscfg = config["path"]

pattern = re.compile("([^.+](?=[^\s@]*@g(oogle)?mail\.com))")

unique_list=[]
unique_list2=[]
ch = '.'
config = configparser.ConfigParser()
config.read("config.ini")
settingscfg = config["path"]

def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

print('Welcome to GDot!\n please remember to compile the blank input.txt with the emails list you eant to analyze...')
while True:
    question = (input('Have you compiled the blank input.txt with the emails list you want to analyze? (y: Yes, n: No)'))
    question = question.lower()
    if question == "n":
       print("Please compile the input.txt file and come back to me!")
       sys.exit(1) 
    elif question == "y":
        print("Great let's do it!")
        break
    else:
        print("Sorry I don't understand, try again")
         
 
    
if not is_non_zero_file(config.get("path", "input")) :
        
        print("Error: you have to compile the input.txt file before to proceed!")
        sys.exit(1) 
         
else:

        #select from .txt only gmail/googlemail email addresses and remove all dots 
        test_list = open(config.get("path", "input"),"r")
        for line in test_list:
              for match in re.findall(pattern, line):
                  
                    if line not in unique_list:
                          unique_list.append(line)
                          list_of_str = [elem.replace(ch,'')for elem in unique_list]
                          without_space = ''.join(list_of_str)

                          with open(config.get("path", "temp"),'w+') as f:
                                f.write(without_space)

        if not is_non_zero_file(config.get("path", "temp")):

                             
           print('no gmail alias found in the list, great!')
           sys.exit(1) 
                        
                       
        #remove all Google domains from selected email adresses 

        with open(config.get("path", "temp"),'r')  as infile, \
              open(config.get("path", "temp1"),'w+') as outfile:
              data = infile.read()
              data = data.replace("@googlemailcom", "@gmailcom")
              data = data.replace("@gmailcom", "")

              outfile.write(data) 

        #find duplicated usernames 

        output_file_path = (config.get("path", "temp2"),'r') 
        input_file_path = (config.get("path", "temp1"),'r') 

        completed_lines_hash = set()

        output_file = open(output_file_path, "w+")

        for line in open(input_file_path, "r"):

          hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()

          if hashValue not in completed_lines_hash:
            
            completed_lines_hash.add(hashValue)
          else:
            output_file.write(line)

output_file.close()

#print usernames with Google alias abuse 
final_print = open(config.get("path", "temp2"),'r') 
if os.path.getsize((config.get("path", "temp2"),'r') > 0):

  s1= 'username:'+''.join(final_print.read())
  s2="I found these usernames abusing Gmail alias using DOT technique:\n"
  s3 = "domain : @gmail.com OR googlemail.com"
  s4="\n these user has created more than one account using the same Google UUID"

  results = print(s2,s1,s3,s4)
  with open(config.get("path", "output"), 'w+') as f:
    f.write(str.results)
    print(results)

else:

  print('No gmail alias found!')
            
#clean-up of files 

os.remove(config.get("path", "temp"))
os.remove(config.get("path", "temp1"))
os.remove(config.get("path", "temp2"))


