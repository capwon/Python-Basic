# 10개의 자연수를 리스트에 입력 받아 그 중 가장 큰수를 출력
# 힌트(리스트에 가장 큰값을 가지고오는 함수가 있음)
# def solution(nums):
#     print(max(nums))
#     return max(nums)

# nums = list(map(int, input().split()))
# solution(nums)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 8명의 키를 리스트에 입력 받아, 가장 큰 키와 가장 작은 키의 차이를 출력(입력은 숫자만 입력)
# 힌트(리스트에 가장 큰값과 가장 작은 값을 가지고오는 함수가 있음)
# def solution(nums):
#     # print(max(nums)-min(nums))
#     return max(nums)-min(nums)

# nums = list(map(int, input().split()))
# solution(nums)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 12개의 자연수를 입력 받아 리스트에 저장하고, 짝수 중 가장 큰 수와 홀수 중 가장 작은 수를 리턴
# 짝수 홀수 구분 가능
# 리스트에서 최대값, 최소값 알 수 있음
# def solution(nums):
#     # print(nums)
#     even = []
#     odd = []

#     for i in nums:
#         if(i % 2 == 0):
#             even.append(i)
#         else:
#             odd.append(i)
#     # print(even)
#     # print(odd)

#     return max(even), min(odd)

# nums = list(map(int, input().split()))
# solution(nums)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 10개의 정수를 입력 받아 100미만의 수 중 가장 큰 수와 100 이상의 수 중 가장 작은 수를 리턴

# def solution(nums):
#     large=[]
#     small=[]

#     for i in nums:
#         if (i<100):
#             small.append(i)
#         else:
#             large.append(i)
    
#     # print(max(small),min(large))
#     return max(small), min(large)

# nums = list(map(int, input().split()))
# solution(nums)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 10개의 정수를 입력 받아 리스트에 저장한 후 내림차순으로 정렬하여 리턴
# nums = list(map(int, input().split()))
# nums.sort(reverse =True)
# print(nums)

# def solution(nums):
#     nums.sort(reverse =True)

#     return nums

# nums = list(map(int, input().split()))
# solution(nums)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 