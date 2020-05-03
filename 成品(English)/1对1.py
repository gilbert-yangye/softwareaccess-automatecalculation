import os, sys, re


#i = int(input())
i=int(1)

As = []
for n in range(1,3):

    readtxt = open('/Users/yeyang/Desktop/python.tour/designcon/WPJ'+str(n)+'.rtf','r')

    fullcontent = readtxt.read()

    fullcontent = fullcontent.replace(' ','') #openplaintxt without space
    fullcontent = fullcontent.replace('\n','')
    fullcontent = fullcontent.replace('\\','')

    regexN = re.compile(r'N=(?:-|)\d*(?:\.|)\d*') #variables A
    regexV = re.compile(r'V=(?:-|)\d*(?:\.|)\d*') #variables B

    wallN = regexN.findall(fullcontent)[i-1] #wall Number i
    wallV = regexV.findall(fullcontent)[i-1]

    N = wallN.strip('N=')
    V = wallV.strip('V=')
    N = float(N)
    V = float(V)
    print(N)
    print(V)
    print(n)

    As.insert(int(n-1), int(1000*((max(1.3*0,1*1.1*V)-0.8*(-N))/0.6-0*0)/360)) #0needs more stipulation
    print(As)

    pass
maxAs = max(As)
print ('As='+ str(maxAs))
manAsfloor = As.index(maxAs)+1
print (manAsfloor)
'''

maxAs =max(int(As))
maxAsfloor = As9
print (maxAs)
print ('floor ' + '''
