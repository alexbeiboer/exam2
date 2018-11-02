cross_street = input('What cross street are you on?')
#Receive the users input which is a number
cross_street = float(cross_street)
# change from a number to a character
def street(bus_stop):
    if cross_street > 91:
        return ('Go to 96th St and take the cross town bus')
    elif cross_street < 90:
        return ('Go to 86th St and take the cross town bus')
    elif cross_street > 80:
        return('Go to 86th St and take the cross town bus')
    elif cross_street < 70:
        return('FAIL')
print(street(cross_street))
