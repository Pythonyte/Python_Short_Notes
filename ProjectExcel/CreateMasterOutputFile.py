import sys,os,re,openpyxl
sys.path.append(os.getcwd())
from FCBLibrary import *



def readExcelfiles(Sourcefilename,destSheet):
    wbsoruce = openpyxl.load_workbook(Sourcefilename)
    wssource = wbsoruce.worksheets[0]
    for row in wssource.iter_rows():
        destSheet.append([cell.value for cell in row])


def getDestSheet(wb,sheetname):
    if sheetname in wb.sheetnames:
        return wb[sheetname]
    else:
         return wb.create_sheet(sheetname, 0)

def readBusinessList(destSheet,Sfilename):
    for row in readBusinessxlsx(Sfilename):
        destSheet.append(row)

def readPriorTransits(destSheet,Sfilename):
    for row in readPriorxlsx(Sfilename):
        destSheet.append(row)

def readUSLFiles(destSheet,Sfilename) :
    for row in readUSL(Sfilename):
        destSheet.append(row)

def readProcessorFiles(wbdest,SdirName):
    for (dir,subdir,files) in os.walk(SdirName):
        if files:
            processor=dir.split('\\')[-1].upper()
            if processor not in TabNames:continue
            filenames=[dir+"\\"+file for file in files if re.search('^OUTPUT',file)]
            print('Start reading all files of :',processor,":\n",filenames,"\n\n")

            for file in filenames:
                print("proceeding for :",file)
                readExcelfiles(file,getDestSheet(wbdest,TabNames[processor]))


