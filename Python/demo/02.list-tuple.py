#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list
nums = [1, 44, 55]
print(nums)
print(nums[-1])

nums.append(12)
print(nums)
nums.insert(1, "O_o")
print(nums)
nums.pop(1)
print(nums)

# tuple -> 不可改变只针对第一层数据
nums2 = (1) # 得到的是一个数
print(nums2)
nums2 = (1, )
print(nums2)
nums2 = (1, 2, [3])
# nums2[0] = 4 报错
print(nums2)
nums2[2][0] = 4
print(nums2)
