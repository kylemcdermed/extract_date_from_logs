# time stamp, log_level, message, ip-address
import csv
import datetime 
import random
import re

log_levels = ['INFO','ERROR','WARNING','DEBUG']
messages = ['System boot successful','Failed to connect to datebase',
            'Memory usage is high','User authentication attempt receieved']

ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
message_pattern = r'INFO|ERROR|WARNING|DEBUG'


# create csv file with rows
with open("log_file.csv",mode='w',newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['time stamp','log_level','message','ip-address'])


# create date for rows
with open("log_file.csv",mode='a',newline='') as csv_file:
    writer = csv.writer(csv_file)
    for _ in range(0,100):
        random_date = datetime.datetime(random.randint(2000,2025),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(0,23),
                                        random.randint(0,59),
                                        random.randint(0,59)).strftime('%Y-%m-%d %H:%M:%S')
        log_level = random.choice(log_levels)
        message = random.choice(messages)
        ip_address = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

        writer.writerow([random_date,log_level,message,ip_address])

'''
# read data from rows
with open("log_file.csv",mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for r in reader:
        print(r)
'''

# read all ip-address and error messages using re.findall
with open("log_file.csv",mode='r') as csv_file:
    reader = csv.reader(csv_file)
    for r in reader:
        
        row_text = ' '.join(r)
        
        ip_matches = re.findall(ip_pattern,row_text)
        message_matches = re.findall(message_pattern,row_text)

        if ip_matches and message_matches:
            print(ip_matches,', '.join(message_matches))
