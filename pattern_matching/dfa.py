import sys
import graphviz

file = sys.argv[1]
dfa_name = sys.argv[2]
ofile = open(file,"r")
rows = ofile.readlines()
lines= []
for row in rows:
        nrow = row.strip().split()
        lines.append(nrow)
if  len(lines) == 0:
    dfa = graphviz.Digraph() 
    dfa.node("0",peripheries='2') #to set the acceptance state
    dfa_file = open(dfa_name, 'w')
    dfa_file.write(str(dfa))
    print(dfa)

    
else:
    pattern = lines[0][0]

    def ff(inpt):
        back = {1:0}
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


    def dfaf():
        delta = {}
        for j in range(1,len(pattern)+1):
            #j-1 to correct python indexing 
            delta[(j-1),pattern[j-1]] = j
        for a in ["A","G","T","C"]:
            if a != pattern[0]:
                delta[(0,a)] = 0
        for j in range(1,len(pattern)):
            for a in ["A","G","T","C"]:
                if a != pattern[j]: 
                    delta[(j,a)] = delta[(ff(j),a)]
        print(delta)

        dfa = graphviz.Digraph() 
        dfa.node(str(len(pattern)),peripheries='2')
        for key in delta.keys():

            if delta[key] != 0:
                dfa.edge(str(key[0]),str(delta[key]),key[1])
            
        dfa_file = open(dfa_name, 'w')
        dfa_file.write(str(dfa))

        print(dfa)
       

    dfaf()
    

