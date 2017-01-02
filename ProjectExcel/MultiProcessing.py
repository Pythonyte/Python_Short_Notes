import subprocess,os,openpyxl,re,sys
from datetime import datetime
sys.path.append(os.getcwd())
from FCBLibrary import *

def spawn_processes_for_each_file(filenames,scriptName,dir):
    logfilename=dir+"\\"+dir.split('\\')[-1]+'_LOG'
    logfile= open(logfilename, 'w')
    processes=[]
    processor=dir.split('\\')[-1].upper()
    print('Starting for ====>', processor , '<=====')
    for filename in filenames:
        process=subprocess.Popen(["python",scriptName ,filename,dir],stdout=logfile)
        print('started:DIR==> ',processor,' FILE==> ',filename,' PID:',process.pid)
        processes.append((process,filename,processor))
    return processes,logfile

def wait_for_child_process(processes,filenames):

    for process,filename,processor in processes:
        print('waiting for :DIR==> ',processor,' FILE==> ',filename,' PID:',process.pid)
        returnstatus=process.wait()
        filenames[filename]=returnstatus

    else:
        print("all process done:")

    return filenames


def close_logfile_handle(logfile):
    logfile.close()


def retrun_bad_processes_details(filenameshash):
    arr=[]
    for filename,status in filenameshash.items():
        print('==',status)
        if status != 0:
            arr.append(filename)
    return arr

def start_process_per_directory(filenames,scriptName,dir):
    processes,logfile=spawn_processes_for_each_file(filenames,scriptName,dir)
    filenames=wait_for_child_process(processes,filenames)
    close_logfile_handle(logfile)
    print('Bad Processes are: ',retrun_bad_processes_details(filenames))

def check_additional_filters(processor,file):
    # if file is output file, which is processed.
    if re.search('^OUTPUT',file):return False

    if processor=="PAYMENTECH":
        if re.search("FIN-25",file) and file.split('.')[-1] in  filetypesinfolders[processor]:return True
        else:return False

    if processor=="BAMS":
        if re.search('Bank Deposit Summary',file) and file.split('.')[-1] in  filetypesinfolders[processor]:return True
        else:return False

    # if file type is the one which we need for that processor
    if file.split('.')[-1] in  filetypesinfolders[processor]:return True


def get_all_files_per_directory(directory):
    for (dir,subdir,files) in os.walk(directory):
        if files:
            processor=dir.split('\\')[-1].upper()
            if processor not in filetypesinfolders:continue
            filenames={file : None  for file in files if check_additional_filters(processor,file)}
            yield filenames,dir

