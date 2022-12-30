from os.path import exists as file_exists
import hashlib
import re
import os
pattern = re.compile("([^.+](?=[^\s@]*@g(oogle)?mail\.com))")
test_list =open('/content/sample_data/mystring.txt')
unique_list=[]
unique_list2=[]
ch = '.'

#select from .txt only gmail/googlemail email addresses and remove all dots 

for line in test_list:
  for match in re.findall(pattern, line):
        if line not in unique_list:
              unique_list.append(line)
              list_of_str = [elem.replace(ch,'')for elem in unique_list]
              without_space = ''.join(list_of_str)

              with open('/content/sample_data/mystring2.txt','w+') as f:
               f.write(without_space) 
#remove all Google domains from selected email adresses 

with open(r'/content/sample_data/mystring2.txt', 'r') as infile, \
     open(r'/content/sample_data/mystring3.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("@googlemailcom", "@gmailcom")
    data = data.replace("@gmailcom", "")

    outfile.write(data) 

#find duplicated usernames 

output_file_path = "/content/sample_data/mystring4.txt"
input_file_path = "/content/sample_data/mystring3.txt"

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
final_print = open('/content/sample_data/mystring4.txt')
if os.path.getsize('/content/sample_data/mystring4.txt') > 0:

  s1= 'username:'+''.join(final_print.read())
  s2='I found these usernames abusing Gmail alias using DOT technique:\n'
  s3 = "domain : @gmail.com OR googlemail.com"
  s4="\n these user has created more than one account using the same Google UUID"

  results = print(s2,s1,s3,s4)
  with open('/content/sample_data/results.txt', 'w') as f:
    f.write(str.results)
    print(results)



else:

  print('No gmail alias found!')
#clean-up of files 

os.remove('/content/sample_data/mystring2.txt')
os.remove('/content/sample_data/mystring3.txt')
os.remove('/content/sample_data/mystring4.txt')
