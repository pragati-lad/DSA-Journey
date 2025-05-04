# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())   # so the code knows when to stop taking input 
count = 0

for hackerrank in range(0,N):
    all_same_case = input().lower()  # for case insensitivity
    if "hackerrank" in all_same_case:
        count += 1
        
print(count)  
