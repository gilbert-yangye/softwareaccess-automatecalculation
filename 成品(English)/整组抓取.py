#coding=<utf8>
import os, sys, re, codecs


while True:
    print('\n--------------------------\nplease enter the wall number')
    i=int(input())
    As = []
    
    for n in range(1,10):
        try:
            readtxt = codecs.open('/Users/yeyang/Desktop/python.tour/designcon/data/WPJ'+str(n)+'.txt','r','gbk')
            fullcontent = readtxt.read()
        
            fullcontent = fullcontent.replace(' ','') #openplaintxt without space
            fullcontent = fullcontent.replace('\n','')
            fullcontent = fullcontent.replace('\\','')
        
            regexwall = re.compile(r'N-WC=.+?WS_XF')
            wallinfo = regexwall.findall(fullcontent)
        
            try:
                targetwall = wallinfo[i-1]
            except:
                print(str(n)+' th floor out of index')
                As.insert(int(n-1),-10086)                
                continue
            
            try:
                regexN = re.compile(r'N=(?:-|)\d*(?:\.|)\d*') #variables A
                regexV = re.compile(r'V=(?:-|)\d*(?:\.|)\d*') #variables B
                wallN = regexN.findall(targetwall)[1] #wall Number i
                wallV = regexV.findall(targetwall)[1]
        
                N = wallN.strip('N=')
                V = wallV.strip('V=')
                N = float(N)
                V = float(V)
                As.insert(int(n-1), int(1000*((max(1.3*0,1*1.1*V)-0.8*(-N))/0.6-0*0)/360)) #0needs more stipulation
            except:
                print('exit writing try loop'+str(n))
                As.insert(int(n-1),-10086)
                pass

        except:
            print(str(n)+' floor doesn\'t exist')
            pass
                
    print('As list = '+str(As))       
    maxAs = max(As)
    print ('Maximum As='+ str(maxAs))
    maxAsfloor = As.index(maxAs)+1
    print ('on '+ str(maxAsfloor)+' floor')
    continue

