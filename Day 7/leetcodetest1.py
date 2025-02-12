def maximumSum(nums):
    def sumofdigits(n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    m = []
    l = len(nums)
    if l == 1:
        return -1

    for i in range(l):
        for j in range(i + 1, l):
            if sumofdigits(nums[i]) == sumofdigits(nums[j]):
                m.append(nums[i] + nums[j])

    if not m:
        return -1

    return max(m)

nums = list(map(int, input().split()))
print(maximumSum(nums))