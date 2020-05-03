#coding=<utf8>
import os, sys, re, codecs, xlwt
from xlwt import Workbook

print('请输入文件路径')
path = input()
print('请输入计算公式路径')
formulapath = input()
print('最大的层数编号是多少？（若WPJ33.OUT是最大的文件，则输入33）')
maxn = int(int(input())+1)

readformula = codecs.open(formulapath+'/计算公式（非加强区）.rtf','r','gbk')
formula = readformula.read()

regexfc= re.compile(r'fc=(?:-|)\d*(?:\.\d*|)')
regexγre= re.compile(r're=(?:-|)\d*(?:\.\d*|)')
regexj= re.compile(r'j=(?:-|)\d*(?:\.\d*|)')
regexfy= re.compile(r'fy=(?:-|)\d*(?:\.\d*|)')
regexFv= re.compile(r'Fv=(?:-|)\d*(?:\.\d*|)')
regexAn= re.compile(r'An=(?:-|)\d*(?:\.\d*|)')

fc= regexfc.findall(formula)[0]
γre= regexγre.findall(formula)[0]
fy= regexfy.findall(formula)[0]
γj= regexj.findall(formula)[0]
Fv= regexFv.findall(formula)[0]
An= regexAn.findall(formula)[0]

fc= float(fc.strip('fc='))
γre= float(γre.strip('re='))
fy= float(fy.strip('fy='))
γj= float(γj.strip('j='))
Fv= float(Fv.strip('Fv='))
An= float(An.strip('An='))

wb = Workbook(encoding='utf8')

sheet = wb.add_sheet('sheet 1') #创建excel表格—‘name’
sheet.write(0,0,'墙柱编号')
sheet.write(0,1,'自然层号')
sheet.write(0,2,'N')
sheet.write(0,3,'V')
sheet.write(0,4,'H')
sheet.write(0,5,'b')
sheet.write(0,6,'As')


breakflag = False

for i in range(1,100000):
    As = []
    listn = []
    listv = []
    listh = []
    listb = []
    
    try:
        if i >= wallamount+1:
            breakflag = True
            break
        else:
            pass
    except:
        pass

    
    for n in range(1,maxn):
        try:
            readtxt = codecs.open(path+'/WPJ'+str(n)+'.OUT','r','gbk')#
            fullcontent = readtxt.read()
        
            fullcontent = fullcontent.replace(' ','') 
            fullcontent = fullcontent.replace('\n','')
            fullcontent = fullcontent.replace('\\','')
        
            regexwall = re.compile(r'N-WC=.+?WS_XF')
            wallinfo = regexwall.findall(fullcontent)
            wallamount = len(wallinfo)

            try:
                targetwall = wallinfo[i-1]
            except:
                As.insert(int(n-1),-10086)                
                continue
                
            try:
                
                regexN = re.compile(r'N=(?:-|)\d*(?:\.|)\d*')
                regexV = re.compile(r'V=(?:-|)\d*(?:\.|)\d*')
                regexH = re.compile(r'B.H.Lwc.m.=\d+(?:\.|)\d+.\d*(?:\.|)\d*.\d*(?:\.|)\d*')
                wallN = regexN.findall(targetwall)[1]
                wallV = regexV.findall(targetwall)[1]
                wall = regexH.findall(targetwall)[0]

                N = wallN.strip('N=')
                V = wallV.strip('V=')
                V = V.strip('-')
                N = -float(N)
                V = float(V)
                H = float(wall[16:20])
                b = float(wall[11:15])
                H = H*1000
                b = b*1000

                #此处更改计算公式
                N = min(0.6*fc*b*H/1000,N)
                Vjd = γj*V*γre
                As.insert(int(n-1), int(1000*((Vjd-0.8*N)/0.6-Fv*An)/fy))
                
                listn.insert(int(n-1),N)
                listv.insert(int(n-1),V)
                listh.insert(int(n-1),H)
                listb.insert(int(n-1),b)
                
            except:
                As.insert(int(n-1),-10086)
                listn.insert(int(n-1),-10086)
                listv.insert(int(n-1),-10086)
                listh.insert(int(n-1),-10086)
                listb.insert(int(n-1),-10086)
                
                
                pass
                
        except:
            As.insert(int(i-1),-10086)
            listn.insert(int(i-1),-10086)
            listv.insert(int(i-1),-10086)
            listh.insert(int(n-1),-10086)
            listb.insert(int(n-1),-10086)            
            pass
    
    maxAs = max(As)
    maxAsfloor = As.index(maxAs)+1
    maxN = listn[maxAsfloor-1]
    maxV = listv[maxAsfloor-1]
    maxH = listh[maxAsfloor-1]
    maxb = listb[maxAsfloor-1]
    sheet.write(i,0,str(i))
    sheet.write(i,1,str(maxAsfloor))
    sheet.write(i,2,str(maxN))
    sheet.write(i,3,str(maxV))
    sheet.write(i,4,str(maxH))
    sheet.write(i,5,str(maxb))
    sheet.write(i,6,str(maxAs))
    continue
    
wb.save('标准层表(最大As)（非加强区）.xls')
print('完成整理')
