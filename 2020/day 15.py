def game(start, stop):
    count = len(start)
    last = 0
    pos = {start[i]:i for i in range(count)}
    while count < stop-1:
        if last in pos:
            temp = pos[last]
            pos[last] = count
            last = count-temp
        else:
            pos[last] = count
            last = 0
        count+=1
    return last



#soluzione 1
print(game([1,20,8,12,0,14], 2020))

#soluzione 2
print(game([1,20,8,12,0,14], 3*10**7))


"Soluzione brute force"
##nums = [1,20,8,12,0,14]
##while len(nums)<2020:
##    if nums[-1] in nums[:-1]:
##        ind = nums[-2::-1].index(nums[-1])
##        nums.append(ind+1)
##    else:
##        nums.append(0)
