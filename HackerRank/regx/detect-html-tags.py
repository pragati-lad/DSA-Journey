# Enter your code here. Read input from STDIN. Print output to STDOUT

# find tags 
# remove dupes
# arrange lexicographically

import re  # is obv a labrary 

n = int(input()) # how many lines of input user will give 

# need somthing to store the tags we find
# lets use a set to store the tag names because a set automatically removes duplicates.
# so storing tags and removing dupe tags is happning simultanuously
tags = set()
  
for i in range(n):
    line = input() # user will actually give input here 
    # use .findall function from re 
    collected_tags = re.findall(r'<\s*/?\s*([a-zA-Z0-9]+)',line)#tag names can include numbers.
    
#Everything outside the () in this regex is just to locate where the tag name is.
#Only what's inside the () is what we actually capture (extract).

    tags.update(collected_tags)#puts all element that we collected in set so that it will remove dupe
    
# now lets arrenge lexicographically
arrenged_tags = sorted(tags)

# now to print the tags with ";"
print(";".join(arrenged_tags))
