#coding=<utf8>
import os, sys, re, codecs

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

while True:
    print('\n--------------------------\n请输入想计算的墙号（纯整数数字，例如N-WC=17，则输入17），或任意字符退出')
    i=int(input())
    As = []
    
    for n in range(1,maxn):
        try:
            readtxt = codecs.open(path+'/WPJ'+str(n)+'.OUT','r','gbk')
            fullcontent = readtxt.read()
        
            fullcontent = fullcontent.replace(' ','') 
            fullcontent = fullcontent.replace('\n','')
            fullcontent = fullcontent.replace('\\','')
        
            regexwall = re.compile(r'N-WC=.+?WS_XF')
            wallinfo = regexwall.findall(fullcontent)
        
            try:
                targetwall = wallinfo[i-1]
            except:
                print(str(n)+' 号自然层中无此墙')
                As.insert(int(n-1),-10086)                
                continue
            
            try:
                regexN = re.compile(r'N=(?:-|)\d*(?:\.|)\d*') 
                regexV = re.compile(r'V=(?:-|)\d*(?:\.|)\d*')
                regexH = re.compile(r'B.H.Lwc.m.=\d+(?:\.|)\d+.\d*(?:\.|)\d*.\d*(?:\.|)\d*')
                wallN = regexN.findall(targetwall)[1] 
                wallV = regexV.findall(targetwall)[1]
                wall = regexH.findall(targetwall)[0]
        
                H = float(wall[16:20])
                b = float(wall[11:15])
                H = H*1000
                b = b*1000
                N = wallN.strip('N=')
                V = wallV.strip('V=')
                V = V.strip('-')
                N = -float(N)
                V = float(V)

                #此处更改计算公式
                N = min(0.6*fc*b*H/1000,N)                
                Vjd = γj*V*γre
                As.insert(int(n-1), int(1000*((Vjd-0.6*N)/0.6-Fv*An)/fy)) 
            except:
                print('该墙号不存在于楼层'+str(n))
                As.insert(int(n-1),-10086)
                pass

        except:
            print(str(n)+' 号自然层不存在')
            As.insert(int(n-1),-10086)
            pass
                
    print('As 清单 = '+str(As))       
    maxAs = max(As)
    print ('As 最大值='+ str(maxAs))
    maxAsfloor = As.index(maxAs)+1
    print ('As最大值在 '+ str(maxAsfloor)+' 号自然层')
    continue

