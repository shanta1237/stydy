'''you live 4 mile fom university ths bus drive at 25mph
but spend 2 minute at each of the 10 stops on  the way
how long will the bus jornmey take
alternatively , you could run to university. you jog the first 7mph
them run next twi at 15mph; before jogging at last at 7 mph again. will this be quicker or slower than the bus?
'''
living_mile_apart = 4
drive_velociy = 25
time_taken = ((living_mile_apart/drive_velociy)+60)
#2 minute in each stop
time_spend= 20
total_time= time_taken+time_spend
total_time=(f"Total time taken  by bus in {total_time}")
jog_one=((1/7)*60)
jog_two = ((2/15)*60)
jog_three = ((1/7)*60)
total_walk_time = jog_one+jog_two+jog_three
print(f"Time Taken by running is {total_walk_time}")
if(total_time > total_walk_time):
    print("Taking bus is slower than faster")
else:
    print("Taking bus is quicker than run")
