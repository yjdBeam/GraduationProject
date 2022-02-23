#CalStatistics

def getNum():#获取用户不定长的一组数据
    nums = []
    num = input("请输入数字，空格结束：")
    while num != " ":
        nums.append(eval(num))
        num = input("请输入数字，空格结束：")
    return nums


def mean(nums): #计算平均值
    s = 0
    for num in nums:
        s += num
    m = s / len(nums)
    return m

def dev(nums): #计算方差
    sdev = 0
    for num in nums:
        sdev += (num-mean(nums))**2
    d = sdev / (len(nums)-1)
    return d

def median(nums): #计算中位数
    sorted(nums)
    size = len(nums)
    if size % 2 == 0:
        med = (nums[size//2-1] + nums[size//2])/2
    else:
        med = nums[size//2]
    return med


n = getNum()
print("平均值:{:.2f};方差:{:.2f};中位数:{:.2f}".format(mean(n),dev(n),median(n)))
