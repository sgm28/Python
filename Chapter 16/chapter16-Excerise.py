import datetime  
import time
#import doubleDaySolution



class Time:
    """Represents the time of day.

        attributes: hour, mintue, second
    """


'''
def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second


    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum
'''

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    assert valid_time(t1) and  valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False

    if time.minute >= 60 or time.second >= 60:
        return False
    return True



    


def print_time(time):
    return "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

'''

    1. Use the datetime module to write a program that gets the current date and prints the day of
    the week.
'''
def dayOfTheWeek():

    #Incorrect 
    #month, date, year = input("Please enter today's date separated my commas: (month), (date), (year)").split()
    #month = int(month)
    #date = int(date)
    #year = int(year)
    #todayDate = datetime.date(year, month, date)
    todayDate = datetime.date.today()
    #return "Day of the week is " + str(todayDate.weekday())
    print("Day of the week is " + str(todayDate.weekday()))
    print("Today is: ", todayDate.strftime('%A'))
    

'''
    2. Write a program that takes a birthday as input and prints the user’s age and the number of
    days, hours, minutes and seconds until their next birthday.
'''
def nextBirthday():
    month, date, year = input("Please enter your birthday 1 seperated by space (month, day, year): ").split()
    #print(month, date, year)

    #birthday = datetime.date(int(year), int(month), int(date))
    

    #today = datetime.date.today()
    

    # added this section 12/21/2023

    birthday = datetime.datetime(int(year), int(month), int(date))
    today = datetime.datetime.today()

    # if the birthday has pass, calculate the next birthday
    if today > birthday:
        birthday = datetime.datetime(today.year+1, birthday.month, birthday.day)
    
    time_to_birthday = abs(birthday - today)

    print("The number of days until your next birthday is:", time_to_birthday.days)

    #hours = time_to_birthday.days * 24

    #minutes = hours * 60

    #seconds = minutes * 60

    #print(time_to_birthday.days, hours, minutes, seconds)


'''

3.  For two people born on different days, there is a day when one is twice as old as the other.
    That’s their Double Day. Write a program that takes two birth dates and computes their
    Double Day.

'''

    ##################################################################

def doubleDay(youngerBirthday, olderBirthday):

    ##########THURSDAY DEC 22, 2003###################################
    
    # Making sure the older birthday is older birthday and the younger birthday
    # is the younger birthday
    # the older date is less than the younger date
    # the younger date is greater than the older date
    # assert make sure the invariant is true
    #assert youngerBirthday > olderBirthday
    
        
    


    ###################################################################
    #Logic: The day the younger birthday, is the older birthday age, is the day older birthday will be twices as old as the younger birthday
    # Brother was born July 23 2002 and I was 9 years old. When brother reaches the age of 9, I will be eighteen years old.
    # I will be twice the age of my brother
    difference = abs(olderBirthday - youngerBirthday)
   # print(difference.days / 365)
    twiceAsOld = youngerBirthday + difference
    print(type(twiceAsOld))
    hours = twiceAsOld.day * 24
    minutes = hours * 60
    seconds = minutes * 60
    #print(typeof(twiceAsOld))
    print(twiceAsOld.day, hours, minutes, seconds)
    print(twiceAsOld.month, twiceAsOld.day, twiceAsOld.year)



'''

    4. For a little more challenge, write the more general version that computes the day when one
    person is n times older than the other.

'''
def nTimesOlder(youngerBirthday, olderBirthday):
    ''' n.  You will n days older when younger birthday reaches older birthday age'''
    numberDaysOlder = int(input("You will be n (double/tripple/quadriple) days older when younger birthday reaches older birthday age"
                                +" How many n do you want to be? 1 means double, 2 means tripple, etc. : "))
    '''
    Calculate the diffrence then add n times
    n  = 1 means double
    n = 2 means tripple
    n = 3 mean quadrupple
    '''
    difference = abs(olderBirthday - youngerBirthday)
    difference = difference * numberDaysOlder
    twiceAsOld =  youngerBirthday + difference
    hours = twiceAsOld.day * 24
    minutes = hours * 60
    seconds = minutes * 60
    #print(typeof(twiceAsOld))
    #print(twiceAsOld.day, hours, minutes, seconds)
    print(twiceAsOld.month, twiceAsOld.day, twiceAsOld.year)

    


    
    
    

    
''''
start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0
done = add_time(start, duration)
#print(print_time(done))
'''

#Excersie 1
#print(dayOfTheWeek())
#dayOfTheWeek()


#Excersie 2
#nextBirthday()


#Exercise 3
month, day, year = input("Please enter the birthday 1 of younger person seperated by space (month, day, year): ").split()
birthday1 = datetime.date(int(year), int(month), int(day))
#birthday1 = datetime.date(1993, 8, 16)


month, day, year = input("Please enter your birthday 2  of older person seperated by space (month, day, year) : ").split()
birthday2 = datetime.date(int(year), int(month), int(day))


doubleDay(birthday1, birthday2)

#Exercise 4
month, day, year = input("Please enter the birthday 1 of younger person seperated by space (month, day, year): ").split()
birthday1 = datetime.date(int(year), int(month), int(day))



month, day, year = input("Please enter your birthday 2  of older person seperated by space (month, day, year) : ").split()
birthday2 = datetime.date(int(year), int(month), int(day))

nTimesOlder(birthday1, birthday2)







