import csv,openpyxl,re,os,sys
sys.path.append(os.getcwd())
from FCBLibrary import *
from datetime import datetime
from operator import itemgetter

IDsHash=getIdsHash(getFileName(Businessfilename,2016,11))

def returnInputs(Sfilename,dir):
    OfileName=dir+"\\OUTPUT"+Sfilename.split('.')[0]+'.xlsx'
    Sfilename=dir+"\\"+Sfilename
    processor=dir.split('\\')[-1].upper()
    Sfiletype=Sfilename.split('.')[-1]
    return OfileName,Sfilename,Sfiletype,processor


def flip_amount(row):
    # used in EU AMEX REPORTS
    # to change fee and discount amount (-ve to +ve)
    row[3]=-1*float(row[3].replace(',',''))
    row[4]=-1*float(row[4].replace(',',''))
    return row


def Filter_US_AMEX_REPORTS(dataarr,processor):
    activities=['SUBMISSIONS','ADJUSTMENTS','CHARGEBACKS']
    breakers=['SUMMARY TOTALS','TOTALS']
    pdates=['SETTLEMENT DATE']
    pdate_index=2
    activities_location_index=0
    breakersIndex=0
    consider_date=None
    going_on_date=None
    going_on_activity=None
    filteredData=[]
    activity=''
    pdate=None
    print("====>",IDsHash['AMEX'],"<===")

    for count,row in enumerate(dataarr):

        if not row : continue
        if len(row)>=1:
            activity=row[activities_location_index].upper()
            breaker=row[breakersIndex].upper()
        if len(row)>3:
            pdate=row[pdate_index].upper()

        if  breaker in breakers:going_on_activity=None

        if consider_date:
            going_on_date=row[pdate_index]
            consider_date=None

        if (going_on_activity is not None):
            if going_on_activity in ['SUBMISSIONS']:
                del row[0]
                row.insert(0,going_on_date)  #insert on any useless column
#datetime.strptime(going_on_date,'%m/%d/%Y')
            if row[data_to_pick_for_output[processor][going_on_activity]['id']] in [str(x) for x in IDsHash['AMEX']]:
                row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']]=datetime.strptime(row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']],data_to_pick_for_output[processor][going_on_activity]['sdateformat'])
                filteredData.append(itemgetter(*data_to_pick_for_output[processor][going_on_activity]['columns'])(row))

        if activity in activities:going_on_activity=activity
        if pdate in pdates:consider_date=True

    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def Filter_CA_AMEX_REPORTS(dataarr,processor):
    activities=['SUBMISSIONS','ADJUSTMENTS','CHARGEBACKS']
    breakers=['SUMMARY TOTALS','TOTALS']
    pdates=['SETTLEMENT DATE']
    pdate_index=0
    activities_location_index=0
    breakersIndex=0
    consider_date=None
    going_on_date=None
    going_on_activity=None
    filteredData=[]
    activity=''
    pdate=None
    print("====>",IDsHash['AMEX'],"<===")

    for count,row in enumerate(dataarr):

        if not row : continue
        if len(row)>=1:
            activity=row[activities_location_index].upper()
            breaker=row[breakersIndex].upper()
        if len(row)>3:
            pdate=row[pdate_index].upper()

        if  breaker in breakers:going_on_activity=None

        if consider_date:
            going_on_date=row[pdate_index]
            consider_date=None

        if (going_on_activity is not None):
            if going_on_activity in ['SUBMISSIONS']:
                del row[0]
                row.insert(0,going_on_date)  #insert on any useless column
#datetime.strptime(going_on_date,'%m/%d/%Y')
            if row[data_to_pick_for_output[processor][going_on_activity]['id']] in [str(x) for x in IDsHash['AMEX']]:
                row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']]=datetime.strptime(row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']],data_to_pick_for_output[processor][going_on_activity]['sdateformat'])
                filteredData.append(itemgetter(*data_to_pick_for_output[processor][going_on_activity]['columns'])(row))

        if activity in activities:going_on_activity=activity
        if pdate in pdates:consider_date=True

    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def check_for_data_EU(row,processor):
    return True if len(row)>2 else False

def Filter_EU_AMEX_REPORTS(dataarr,processor):
    activities=['SUBMISSIONS','ADJUSTMENTS','CHARGEBACKS']
    breakers=['SUMMARY TOTALS','TOTALS']
    pdates=['SETTLEMENT DATE']

    # as only for submission it is needed
    pdate_index=0

    activities_location_index=0
    breakersIndex=0
    consider_date=None
    going_on_date=None
    going_on_activity=None
    filteredData=[]
    activity=''
    pdate=None
    print("====>",IDsHash['AMEX'],"<===")

    for count,row in enumerate(dataarr):

        if not row : continue
        if len(row)>=1:
            activity=row[activities_location_index].upper()
            breaker=row[breakersIndex].upper()
        if len(row)>3:
            pdate=row[pdate_index].upper()

        if  breaker in breakers:going_on_activity=None

        if consider_date:
            going_on_date=row[pdate_index]
            consider_date=None

        if (going_on_activity is not None):
            if going_on_activity in ['SUBMISSIONS']:
                del row[0]
                row.insert(0,going_on_date)  #insert on any useless column
            #print(going_on_activity,data_to_pick_for_output[processor][going_on_activity]['id'],row[0:3])
            if row[data_to_pick_for_output[processor][going_on_activity]['id']] in [str(x) for x in IDsHash['AMEX']]:
                row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']]=datetime.strptime(row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']],data_to_pick_for_output[processor][going_on_activity]['sdateformat'])
                filteredRow=list(itemgetter(*data_to_pick_for_output[processor][going_on_activity]['columns'])(row))
                print(filteredRow)
                filteredData.append(flip_amount(filteredRow))

        if activity in activities:going_on_activity=activity
        if pdate in pdates:consider_date=True

    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData


def Filter_UK_AMEX_REPORTS(dataarr,processor):
    print("in Filter_UK_AMEX_REPORTS")
    activities=['SUBMISSIONS','ADJUSTMENTS','CHARGEBACKS']
    breakers=['SUMMARY TOTALS','TOTALS']
    pdates=['SETTLEMENT DATE']
    pdate_index=0
    activities_location_index=0
    breakersIndex=0
    consider_date=None
    going_on_date=None
    going_on_activity=None
    filteredData=[]
    activity=''
    pdate=None
    print("====>",IDsHash['AMEX'],"<===")

    for count,row in enumerate(dataarr):

        if not row : continue
        if len(row)>=1:
            activity=row[activities_location_index].upper()
            breaker=row[breakersIndex].upper()
        if len(row)>3:
            pdate=row[pdate_index].upper()

        if  breaker in breakers:going_on_activity=None

        if consider_date:
            going_on_date=row[pdate_index]
            consider_date=None

        if (going_on_activity is not None):
            if going_on_activity in ['SUBMISSIONS']:
                del row[0]
                row.insert(0,going_on_date)  #insert on any useless column

            if row[data_to_pick_for_output[processor][going_on_activity]['id']] in [str(x) for x in IDsHash['AMEX']]:
                print(going_on_activity,row)
                row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']]=datetime.strptime(row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']],data_to_pick_for_output[processor][going_on_activity]['sdateformat'])
                filteredData.append(itemgetter(*data_to_pick_for_output[processor][going_on_activity]['columns'])(row))

        if activity in activities:going_on_activity=activity
        if pdate in pdates:consider_date=True

    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData


def Filter_DE_AMEX_REPORTS(dataarr,processor):
    print("in Filter_DE_AMEX_REPORTS")
    activities=['SUBMISSIONS','ADJUSTMENTS','CHARGEBACKS']

    breakers=['SUMMARY TOTALS','TOTALS']
    pdates=['SETTLEMENT DATE']
    pdate_index=0
    activities_location_index=0
    breakersIndex=0
    consider_date=None
    going_on_date=None
    going_on_activity=None
    filteredData=[]
    activity=''
    pdate=None
    print("====>",IDsHash['AMEX'],"<===")

    for count,row in enumerate(dataarr):

        if not row : continue
        if len(row)>=1:
            activity=decodingValues[row[activities_location_index].upper()]
            breaker=decodingValues[row[breakersIndex].upper()]
        if len(row)>3:
            pdate=row[pdate_index].upper()

        if  breaker in breakers:going_on_activity=None

        if consider_date:
            going_on_date=row[pdate_index]
            consider_date=None

        if (going_on_activity is not None):
            if going_on_activity in ['SUBMISSIONS']:
                del row[0]
                row.insert(0,going_on_date)  #insert on any useless column

            if row[data_to_pick_for_output[processor][going_on_activity]['id']] in [str(x) for x in IDsHash['AMEX']]:
                print(going_on_activity,row)
                row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']]=datetime.strptime(row[data_to_pick_for_output[processor][going_on_activity]['sdateIndex']],data_to_pick_for_output[processor][going_on_activity]['sdateformat'])
                filteredData.append(itemgetter(*data_to_pick_for_output[processor][going_on_activity]['columns'])(row))

        if activity in activities:going_on_activity=activity
        if pdate in pdates:consider_date=True

    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData



def Filter_FR_AMEX_REPORTS(dataarr,processor):
    print("in Filter_FR_AMEX_REPORTS")
def Filter_AU_AMEX_REPORTS(dataarr,processor):
    print("in Filter_AU_AMEX_REPORTS")


def Filter_BAMS(dataarr,processor):
    #deepika
    filteredData=[]
    for count,row in enumerate(dataarr):
        if row[data_to_pick_for_output[processor]['id']] in IDsHash['BAMS']:
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def Filter_BILLDESK(dataarr,processor):
    #deepika
    filteredData=[]
    for count,row in enumerate(dataarr):
        if row[data_to_pick_for_output[processor]['id']] in IDsHash['BILL DESK']:
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def Filter_DISCOVER(dataarr,processor):
    print("in Filter_DISCOVER")
    filteredData=[]
    for count,row in enumerate(dataarr):

        if row[data_to_pick_for_output[processor]['id']] in IDsHash['DISCOVER']:
            if type(row[0]) == datetime and (type(row[4]) == float or type(row[4]) == int)           and (type(row[6]) == float or type(row[6]) == int):
                filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData


def Filter_HDFC(dataarr,processor):
    #deepika
    filteredData=[]
    for count,row in enumerate(dataarr):
        if row[data_to_pick_for_output[processor]['id']] in IDsHash['HDFC']:
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def Filter_NETEASE(dataarr,processor):
    #deepika
    filteredData=[]
    for count,row in enumerate(dataarr):
        if row[data_to_pick_for_output[processor]['id']] in [str(x) for x in IDsHash['NETEASE CUP']]:
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
        elif row[data_to_pick_for_output[processor]['id']] in [str(x) for x in IDsHash['NETEASE CMB']]:
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData

def Filter_PAYMENTECH(dataarr,processor):
    #deepika
    filteredData=[]
    for count,row in enumerate(dataarr):
        if row[data_to_pick_for_output[processor]['id']] in IDsHash['PTECH TD ID'] or row[data_to_pick_for_output[processor]['id']] in IDsHash['PTECH FTI ID'] or row[data_to_pick_for_output[processor]['id']] in IDsHash['PTECH BU ID'] :
            filteredData.append(itemgetter(*data_to_pick_for_output[processor]['columns'])(row))
    filteredData.insert(0,data_to_pick_for_output[processor]['heading'])
    return filteredData



def set_configurations():
    global readfile_of_given_type
    readfile_of_given_type['csv']=readcsv
    readfile_of_given_type['xlsx']=readxlsx
    readfile_of_given_type['xlsm']=readxlsm
    cleansing_of_given_processor["DE AMEX REPORTS"]=Filter_DE_AMEX_REPORTS
    cleansing_of_given_processor["EU AMEX REPORTS"]=Filter_EU_AMEX_REPORTS
    cleansing_of_given_processor["US AMEX REPORTS"]=Filter_US_AMEX_REPORTS
    cleansing_of_given_processor["FR AMEX REPORTS"]=Filter_FR_AMEX_REPORTS
    cleansing_of_given_processor["AU AMEX REPORTS"]=Filter_AU_AMEX_REPORTS
    cleansing_of_given_processor["UK AMEX REPORTS"]=Filter_UK_AMEX_REPORTS
    cleansing_of_given_processor["CA AMEX REPORTS"]=Filter_CA_AMEX_REPORTS
    cleansing_of_given_processor["BAMS"]=Filter_BAMS
    cleansing_of_given_processor["BILLDESK"]=Filter_BILLDESK
    cleansing_of_given_processor["DISCOVER"]=Filter_DISCOVER
    cleansing_of_given_processor["HDFC"]=Filter_HDFC
    cleansing_of_given_processor["NETEASE"]=Filter_NETEASE
    cleansing_of_given_processor["PAYMENTECH"]=Filter_PAYMENTECH

if __name__ == "__main__":

    print("In FilterFile:")
    set_configurations()
    OfileName,Sfilename,Sfiletype,processor=returnInputs(sys.argv[1],sys.argv[2])
    print("====File operations Starting for======>",Sfilename,"\n",OfileName)
    dataarr=readfile_of_given_type[Sfiletype](Sfilename)
    dataarr=cleansing_of_given_processor[processor](dataarr,processor)
    writeOutput(dataarr,OfileName)

