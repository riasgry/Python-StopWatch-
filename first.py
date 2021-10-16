from time import sleep

def function_time(start):
    hour=0
    minute = 0
    second = 0
    
    while start==True:
        second+=1
        if(second==60):
            minute=minute+1
            second=0
            if(minute==60):
                hour=hour+1
                minute=0
        print(hour,':',minute,':',second)
        sleep(1)
        if(hour==1):
            break
# def function_counttime():

  
x=input('Start?')
if(input=='y'or'Y'):
    function_time(start=True)
else:
    print('Have a Nice Day')