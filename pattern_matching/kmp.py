import sys

file = sys.argv[1]

matrix = open(file,"r")
rows = matrix.readlines()
lines= []
for row in rows:
        nrow = row.strip().split()
        lines.append(nrow)


if len(lines) == 1 or len(lines) == 0:
    print(-1)

else:

    seq = lines[0][0]
    #account for when there is no second line 

    pattern = lines[1][0]


    def ff(inpt):
        back = {0:0,1:0}
        i = 0
        for j in range(2,len(pattern)+1):
            i = back[j-1]
            while pattern[j-1] != pattern[i] and i>0:
                i = back[i]
            if pattern[j-1] != pattern[i] and i==0:
                back[j]= 0
            else:
                back[j]= i+1
        return back[inpt]



    def kmp():
        result = []
        states = range(len(pattern)+1)
        i = 0 #i is equal to the state
        j = 1
        while j <= len(seq):
            
            if seq[j-1] == pattern[i]:
                j= j+1
                i = i + 1
                if i == states[-1]:
                    result.append((j-1)-len(pattern)) 
                    
                    i = ff(states[-1]) 
            else:
                i = ff(i)
                if i == 0 and seq[j-1] != pattern[i]: 
                    j = j+1
        if result == []:
            print(-1)
        else:
            print(result)
        

    kmp()



