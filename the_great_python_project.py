#!/bin/python3

import time
import json
from cryptography.fernet import Fernet
import mysql.connector
import csv 
from script_for_csv import *
import script_for_csv

try:
#opening the credentials JSON file for the correct username and password of mysql DB user
    with open('credentials.json','r') as cred_jf:
        dict_format = json.load(cred_jf)
        username = dict_format['username']
        passwd = dict_format['password'].encode('utf-8')

#########################################################################################

#Now encrpyting the password for a secure transmission
    key = Fernet.generate_key() #generated the key for encryption
    object_of_key = Fernet(key) #converted the key into object format
    enc = object_of_key.encrypt(passwd) #Encrpytion Successful
    dec = object_of_key.decrypt(enc) #Decryption successful
    mysql_passwd = dec.decode('utf-8') #Decoded from bytes format to normal string

#########################################################################################

#Connecting to the database using its credentials which are stored in another json file
    al_nafi_db = mysql.connector.connect(
            host = "192.168.0.105",
            user = username,
            password = mysql_passwd,
            database = "alnafi"
            )

    time.sleep(1)

    print(csv_file_creation()) #Now a report of the current disk/FileSystem usage has been created in current directory

    list_of_row_in_tuples = []

    with open("FS_report.csv",'r') as cfile:
        cfile = csv.reader(cfile)
        for line in cfile:
            list_of_row_in_tuples.append(tuple(line))

    query = """ INSERT INTO disk_data (file_system,type,size,used,avail,use_in_percent,mount_point,ip_address,hostname,datetime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """ #A query string to allocate the data dynamically

    cur = al_nafi_db.cursor(buffered=True) #setting the cursor for query execution

    time.sleep(3)

    cur.executemany(query, list_of_row_in_tuples) #executing the query with the dynamically allocated values inside our list of tuples as rows

    al_nafi_db.commit() #Saving the changes made during this connection

    #ask the user to display the current updated data from the alnafi database
    while True:
        ask = input("Do you want to display the updated version of \"alnafi\" database here? [Y/n]").lower()
        if ask == "y" or ask == "yes":
            time.sleep(1)
            cur.execute(""" SELECT * FROM disk_data """)
            result = cur.fetchall()
            for row_as_tuple in result:
                print(row_as_tuple)
            break
        elif ask == "n" or ask == "no":
            break
        else:
            print("Error: Enter a valid option!")

    al_nafi_db.close() #closing the connection which was started early in this script

    print(f"\t\t\tThe Report of this system ({script_for_csv.os_flavor()}) has been stored on the MySQL Database Server")
except Exception as e:
    print("Unfortunately something went wrong:\n\t", e)
