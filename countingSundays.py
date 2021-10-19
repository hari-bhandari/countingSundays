import datetime
months=[' '',January','February','March','April','May','June','July','August','September','October','November','December']
def daysInAMonth(month,leap):
    if(month==months[4] or month==months[6] or month==months[9] or month==months[11]):
        return 30
    if(month==months[1] or month==months[3] or month==months[5] or month==months[7] or  month==months[8] or  month==months[10] or month==months[12] ):
        return 31
    if(month==months[2]):
        return 28 if leap else 29
def isLeapYear(year):
    if(year%100==0):
        if(year%400):
            return True
        else:
            return False
    if(year%4):
        return True 
    return False

def countSundays(startDate,endDate):
    totalSundays=0
    startDateInArray=startDate.split('/')
    endDateInArray=endDate.split('/')
    
