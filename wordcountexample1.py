
str1 = "Hello World Hello World Luminar Technolab"

list1 = str1.split(" ")

wordcounts = {}

for w in list1:
    if w in wordcounts.keys():
        wordcounts[w] += 1
    else:
        wordcounts[w] = 1

# d = {}
# count =0
# for w in wordcounts.values():
#     count = wordcounts[w]
#     if w in d.values():
#         count += 1
#     else:
#         count = 1

for w in wordcounts.keys():
    print("%s = %d " % (w, wordcounts[w]))




# comprehensions in python
#
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [i*i for i in nums]

# i = 1
# i*i = 1
# [1]
# i = 2
# i*i = 4
# [1,4]
# i = 3
# i*i = 9
# [1,4,9]..
print(nums2)

nums3 = [i for i in range(1, 10)]
print(nums3)

words = [(w, 1) for w in str1.split(" ")]
print(words)

wordcounts = {x:list1.count(x) for x in list1}

print(wordcounts)




