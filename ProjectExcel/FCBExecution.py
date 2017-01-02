import sys,os
sys.path.append(os.getcwd())
from MultiProcessing import *
from CreateMasterOutputFile import *
from datetime import datetime
startTime = datetime.now()

# this should come from user..via dialog box.
Imonth=11
Iyear=2016

for filenames,dir in get_all_files_per_directory(getDirName(directory,Iyear,Imonth)):
        start_process_per_directory(filenames,scriptName,dir)

MiddleTime=datetime.now()
print("Total time : for creating output files : ",MiddleTime - startTime)

wbdest=openpyxl.Workbook()
readProcessorFiles(wbdest,getDirName(directory,Iyear,Imonth))
readBusinessList(getDestSheet(wbdest,"Business_List"),getFileName(Businessfilename,Iyear,Imonth))
readPriorTransits(getDestSheet(wbdest,"PriorTransitAmts"),getFileName(PriorTransitName,Iyear,Imonth))
readUSLFiles(getDestSheet(wbdest,"USL"),getFileName(USLFilename,Iyear,Imonth))
wbdest.save(MasterFile)
print('Final Output File is :',MasterFile)
FinishTime=datetime.now()
print("Total time it took for creating Master File : ",FinishTime - MiddleTime)
print("Total time script took : ",FinishTime - startTime)