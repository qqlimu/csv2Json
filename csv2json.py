#encoding=utf-8
import csv
import json
def csvToJson(csvfile):
    csvfile = open(csvfile,'r')
    jsonfile = open('temp.json','w')
    fieldnames = ("day_id","金币余额","在线时长","经验值积分")
    reader=csv.DictReader(csvfile,fieldnames)
    for row in reader:
        json.dump(row,jsonfile)
        jsonfile.write('\n')
    csvfile.close()
    jsonfile.close()
def transfer(jsonfile):
    temp = open('temp.json', 'r')
    re=open(jsonfile,'w')
    re.write('['+'\n')
    content=temp.readlines()
    line =0
    while line <( len(content)-1):
        re.write(content[line]+',')
        line = line+1
    re.write(content[line])
    re.write(']'+'\n')
    re.close()
if __name__=='__main__':
    csvfile = raw_input('csvfileName:')
    jsonfile = raw_input('resultJsonName:')
    csvToJson(csvfile)
    transfer(jsonfile)