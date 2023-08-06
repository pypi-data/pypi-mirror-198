import csv
import os
import json 
import sys

def check_time(start, end):
    def go(time):
        time = (time[0] * 60) + time[1]
        return time > start and time < end
    return go

check_january   = check_time((9) * 60       , (16) * 60 + (30)) #9:00 to 16:30
check_february  = check_time((8) * 60 + (30), (17) * 60 + (30)) #8:30 to 17:30
check_march     = check_time((7) * 60 + (30), (18) * 60 + (15)) #7:30 to 18:15
check_april     = check_time((7) * 60 + (15), (20) * 60)        #7:15 to 20:00
check_may       = check_time((6) * 60 + (15), (20) * 60 + (45)) #6:15 to 20:45
check_june      = check_time((6) * 60       , (21) * 60 + (30)) #6:00 to 21:30
check_july      = check_time((6) * 60 + (15), (21) * 60 + (30)) #6:15 to 21:30
check_august    = check_time((7) * 60       , (20) * 60 + (30)) #7:00 to 20:30
check_september = check_time((7) * 60 + (45), (19) * 60 + (30)) #7:45 to 19:30
check_october   = check_time((8) * 60 + (30), (18) * 60 + (30)) #8:30 to 18:30
check_november  = check_time((8) * 60 + (30), (16) * 60 + (30)) #8:30 to 16:30
check_december  = check_time((9) * 60       , (16) * 60)        #9:00 to 16:00

values = {
    "january"   : { "day": 0, "night": 0},
    "february"  : { "day": 0, "night": 0},
    "march"     : { "day": 0, "night": 0},
    "april"     : { "day": 0, "night": 0},
    "may"       : { "day": 0, "night": 0},
    "june"      : { "day": 0, "night": 0},
    "july"      : { "day": 0, "night": 0},
    "august"    : { "day": 0, "night": 0},
    "september" : { "day": 0, "night": 0},
    "october"   : { "day": 0, "night": 0},
    "november"  : { "day": 0, "night": 0},
    "december"  : { "day": 0, "night": 0},
}

def check(f, time, val, month):
    if f(time):
        values[month]["day"] += val
    else:
        values[month]["night"] += val

def remove(file_name):
    os.remove(file_name) if os.path.exists(file_name) else None 

def main():
    remove("january.csv")
    remove("february.csv")
    remove("march.csv")
    remove("april.csv")
    remove("may.csv")
    remove("june.csv")
    remove("july.csv")
    remove("august.csv")
    remove("september.csv")
    remove("october.csv")
    remove("november.csv")
    remove("december.csv")
    
    try:
        x = sys.argv[1]
    except IndexError:
        raise Exception("Please enter a file name.")

    with open(sys.argv[1]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        first_line = True 
        header     = [] 
        for row in csv_reader:
            if first_line:
                first_line = False
                header     = row
                continue
            
            date    = row[0].split("-")
            time    = [int(i) for i in row[1].split(":")]
            val     = float(row[2])
    
            match int(date[1]):
                case 1:
                    check(check_january  , time, val, "january")
                case 2:
                    check(check_february , time, val, "february")
                case 3:
                    check(check_march    , time, val, "march")
                case 4:
                    check(check_april    , time, val, "april")
                case 5:
                    check(check_may      , time, val, "may")
                case 6:
                    check(check_june     , time, val, "june")
                case 7:
                    check(check_july     , time, val, "july")
                case 8:
                    check(check_august   , time, val, "august")
                case 9:
                    check(check_september, time, val, "september")
                case 10:
                    check(check_october  , time, val, "october")
                case 11:
                    check(check_november , time, val, "november")
                case 12:
                    check(check_december , time, val, "december")
                case _:
                    raise Exception("Month is invalid, please check your sheet.")
        
        for month in values:
            for time in values[month]:
                values[month][time] = round(values[month][time], 2)

        print(json.dumps(values, indent=2))

if __name__ == "__main__":
    main()