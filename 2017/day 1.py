from itertools import groupby

with open('input1.txt') as file:
    nums = file.read()

#soluzione 1
print(sum(int(g[0])*(len([*g[1]])-1) for g in groupby(nums))+
      (int(nums[0])if nums[0]==nums[-1] else 0))
#soluzione 2
print(sum(int(nums[num])*2 for num in range(len(nums)//2)
          if nums[num]==nums[num+len(nums)//2]))
