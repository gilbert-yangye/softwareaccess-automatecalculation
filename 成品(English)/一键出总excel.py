# coding: utf-8
import os, sys, re, xlwt, codecs
from xlwt import Workbook

wb = Workbook(encoding='utf8')

for n in range(1,10):
    try:
        print('working on floor '+ str(n))
        readtxt = codecs.open('/Users/yeyang/Desktop/python.tour/designcon/data/WPJ'+str(n)+'.txt','r','gbk')
#    readtxt = open('/Users/yeyang/Desktop/python.tour/designcon/WPJ'+str(n)+'.rtf','r') #open data file

        As = []
    
        name = str('floor'+str(n))
        sheet = wb.add_sheet(name)#creat excel file for txt1
        sheet.write(0,0,'wall number')
        sheet.write(0,1,'N')
        sheet.write(0,2,'V')
        sheet.write(0,3,'As')
    
#        print('title keyed in')
        
        fullcontent = readtxt.read()

        fullcontent = fullcontent.replace(' ','') #openplaintxt without space
        fullcontent = fullcontent.replace('\n','')
        fullcontent = fullcontent.replace('\\','')
    
        regexwall = re.compile(r'N-WC=.+?WS_XF')
        wallinfo = regexwall.findall(fullcontent) #global wall information
        
        for i in range(1,len(wallinfo)):#max 100 walls
#            print(str(i)+'wall')
            targetwall = wallinfo[i-1]
        
            try:
                regexN = re.compile(r'N=(?:-|)\d*(?:\.|)\d*') #variables N
                regexV = re.compile(r'V=(?:-|)\d*(?:\.|)\d*') #variables V
                wallN = regexN.findall(targetwall)[1] #wall Number i
                wallV = regexV.findall(targetwall)[1]
        
                N = wallN.strip('N=')
                V = wallV.strip('V=')
                N = float(N)
                V = float(V)
                As.insert(int(i-1), int(1000*((max(1.3*0,1*1.1*V)-0.8*(-N))/0.6-0*0)/360)) # 0 needs more stipulation
                sheet.write(i,0,str(i))
                sheet.write(i,1,str(N))
                sheet.write(i,2,str(V))
                sheet.write(i,3,str(As[i-1]))
                
            except:
                sheet.write(i,0,i)
                sheet.write(i,3,'fault')
                As.insert(int(i-1), 'N/A')
                pass
#            print(str(i)+'wall finished')
    
    except:
        print(str(n)+' floor doesn\'t exist')
        pass
    
wb.save('trythis2.xls')
print('finished')
