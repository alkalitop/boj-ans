import sys
N = int(sys.stdin.readline())
nums = []
for i in range(0, N):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in range(0, N):
    print(nums[i])
