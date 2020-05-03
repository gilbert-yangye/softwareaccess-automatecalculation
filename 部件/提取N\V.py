import os, sys, re

readtxt = open('/Users/yeyang/Desktop/python.tour/designcon/try.rtf','r')

i = int(input())

fullcontent = readtxt.read()

fullcontent = fullcontent.replace(' ','') #openplaintxt without space
fullcontent = fullcontent.replace('\n','')
fullcontent = fullcontent.replace('\\','')

regexA = re.compile(r'A=(?:-|)\d*(?:\.|)\d*') #variables A
regexB = re.compile(r'B=(?:-|)\d*(?:\.|)\d*') #variables B

wallA = regexA.findall(fullcontent)[i-1] #wall Number i
wallB = regexB.findall(fullcontent)[i-1]

A = wallA.strip('A=')
B = wallB.strip('B=')

print(A)
print(B)
