def set_clock(time, buttons):
    times = time.split(':')
    if int(times[0])<10 : times[0] = '0'+times[0]
    for i in buttons:
        if i == 'H' : times[0] = int(times[0]) + 1
        else : times[1]= int(times[1]) + 1
    if times[1] == 60 : times[1] = '00'
    ans = str(times[0])+':'+str(times[1])
    return ans
    
clock = input()
newclock = set_clock(clock, ['M', 'M', 'H', 'M', 'M', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H', 'H'])
print(newclock)
