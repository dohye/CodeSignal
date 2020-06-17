# discription :
# Given a year, return the century it is in. 
# The first century spans from the year 1 up to and including the year 100, 
# the second - from the year 101 up to and including the year 200, etc.

# solution
def centuryFromYear(year):
    
    century = divmod(year, 100)
    
    if century[1] == 0:
        return century[0]
    
    else:
        return century[0] + 1

  
        
# other solutions
def centuryFromYear(year):
    return (year + 99) // 100
    
def centuryFromYear(year):
    return math.ceil(year/100)
    
def centuryFromYear(year):
    return (year-1)//100+1
    
