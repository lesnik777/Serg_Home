def shorten_to_date(long_date):
    sort1=long_date.split(',')
    return sort1[0]       
print(shorten_to_date("Monday February 2, 8pm"))
