second= int(input('enter the second: '))
day= (((second//60)//600)//60)
print(day)
hour= ((second//60)//60)
print(hour)
minute = (second//60)
print(minute)
total = day+hour+minute+second
print(total)