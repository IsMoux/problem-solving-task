from collections import defaultdict
 
# initializing Matrix
test_list = ["is best", "is is ", "gfd"]
 
# printing original list
print("The original list is : " + str(test_list))
 
temp = defaultdict(int)
 
# memoizing count
for sub in test_list:
    for wrd in sub.split():
        temp[wrd] += 1
 
# getting max frequency
res = max(temp, key=temp.get)
 
# printing result
print("Word with maximum frequency : " + str(res))
