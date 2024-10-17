# General form 
# List Comprehension - [item for item in list if test] 

# Reading from list data in two files and finding the common number

with open ('Day26/file1.txt') as file1:
    nums1=file1.readlines()
    new_list1 = [int(item.strip()) for item in nums1]
    # print(new_list1)

with open ('Day26/file2.txt') as file1:
    nums2=file1.readlines()
    new_list2 = [int(item.strip()) for item in nums2]
    # print(new_list2)

common_nums=[i for i in new_list1 if i in new_list2]
# print(common_nums)



