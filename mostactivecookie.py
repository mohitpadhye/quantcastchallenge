import sys
from datetime import date, datetime, time

def errorMessage():
    print("Invalid Entry. Please enter a valid entry.")


def findCookies(args):
    #check if input is valid
    if len(args) != 4 or args[2] != '-d':
        errorMessage()
        exit(1)
    cookie_log = open(args[1], 'r')
    date_time = datetime.strptime(args[3], "%Y-%m-%d")
    #dictionary to store cookies
    cookies_occurences = {}
    for line in cookie_log.readlines():
        cookie, timestamp = line.split(',')
        timestamp = timestamp.replace('\n', '')
        tmp_datetime = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')
        #populate dictionary
        if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):
            if cookie in cookies_occurences:
                cookies_occurences[cookie] += 1
            else:
                cookies_occurences[cookie] = 1
    #find which cookies are most active
    maxOccured = max(cookies_occurences.values(), key=lambda x: x)
    for cookie, occurences in cookies_occurences.items():
        if occurences == maxOccured:
            print(cookie)


if __name__ == "__main__":
    findCookies(sys.argv) #pass argument from CLI to function