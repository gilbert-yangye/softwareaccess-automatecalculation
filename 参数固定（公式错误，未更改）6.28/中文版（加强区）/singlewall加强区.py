#coding=<utf8>
import os, sys, re, codecs

print('请输入文件路径')
path = input()
print('最大的层数编号是多少？（若WPJ33.OUT是最大的文件，则输入33）')
maxn = int(int(input())+1)

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
                
                N = wallN.strip('N=')
                V = wallV.strip('V=')
                V = V.strip('-')
                N = float(N)
                V = float(V)
                H = float(wall[16:20])
                b = float(wall[11:15])
                H = H*1000
                b = b*1000

                Vm = (0.4*1.43*H*b+0.1*N+0.8*360*101*H/200/1000)/0.85
                maxVm = max(1*1.1*V,1.3*Vm)
                As.insert(int(i-1), int(1000*((100-0.8*(-N))/0.6-0*0)/360))
                 #此处更改公式
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

