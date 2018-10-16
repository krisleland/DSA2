'''
Created on Oct 6, 2018

@author: krist
'''
import csv

class Package(object):
    '''
    classdocs
    '''


    def __init__(self, ID, address, due_time, arrival_time, truck, partners):
        '''
        Constructor
        '''
        self.ID = ID
        self.address = address
        self.due = due_time
        self.arrival = arrival_time
        self.truck = truck
        self.partners = partners
        self.delivered = False
        
def create_package_list():
    package_list = []
    with open('packagefile.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            due_time = ''.join(c for c in row[5] if c.isdigit())
            if due_time == "":
                due_time = 300
            else:
                due_time = (((float(due_time) - 800) / 100 % 1) + int((float(due_time) - 800) / 100)) * 18
            ID = row[0]
            address = row[1]
            if row[7] != "":
                if "truck" in row[7]:
                    truck = ''.join(c for c in row[7] if c.isdigit())
                    arrival_time = 0
                    partners = None
                elif "Delayed" in row[7]:
                    arrival_time = ''.join(c for c in row[7] if c.isdigit())
                    arrival_time = (((float(arrival_time) - 800) / 100 % 1) + int((float(arrival_time) - 800) / 100)) * 18
                    truck = None
                    partners = None
                else:
                    partners = [''.join(c for c in row[7] if c.isdigit()) for x in row[7].split(',')]
                    truck = None
                    arrival_time = 0
            else:
                partners = None
                truck = None
                arrival_time = 0
            print(due_time, arrival_time)
            package_list.append(Package(ID, address, due_time, arrival_time, truck, partners))
    #for package in package_list:
        #print(package.address, due_time, arrival_time, truck)      
    return package_list
                
                