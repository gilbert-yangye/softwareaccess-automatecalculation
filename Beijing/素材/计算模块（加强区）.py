#formula
import codecs, re

print('请输入计算公式路径')

formulapath = input()

N = -89.49

V = 4.11

H = 800

b = 200

readformula = codecs.open(formulapath+'/计算公式.rtf','r','gbk')
formula = readformula.read()

regexft= re.compile(r'ft=(?:-|)\d*(?:\.\d*|)')
regexAwA= re.compile(r'Aw.A=(?:-|)\d*(?:\.\d*|)')
regexFyv= re.compile(r'Fyv=(?:-|)\d*(?:\.\d*|)')
regexAsv= re.compile(r'Asv=(?:-|)\d*(?:\.\d*|)')
regexs= re.compile(r's=(?:-|)\d*(?:\.\d*|)')
regexγre= re.compile(r're=(?:-|)\d*(?:\.\d*|)')
regexj= re.compile(r'j=(?:-|)\d*(?:\.\d*|)')
regexfy= re.compile(r'fy=(?:-|)\d*(?:\.\d*|)')
regexFv= re.compile(r'Fv=(?:-|)\d*(?:\.\d*|)')
regexAn= re.compile(r'An=(?:-|)\d*(?:\.\d*|)')

ft= regexft.findall(formula)[0]
AwA= regexAwA.findall(formula)[0]
Fyv= regexFyv.findall(formula)[0]
Asv= regexAsv.findall(formula)[0]
s= regexs.findall(formula)[0]
γre= regexγre.findall(formula)[0]
ηj= regexj.findall(formula)[0]
fy= regexfy.findall(formula)[0]
γj= regexj.findall(formula)[1]
Fv= regexFv.findall(formula)[0]
An= regexAn.findall(formula)[0]

ft= float(ft.strip('ft='))
AwA= float(AwA.strip('Aw/A='))
Fyv= float(Fyv.strip('Fyv='))
Asv= float(Asv.strip('Asv='))
s= float(s.strip('s='))
γre= float(γre.strip('re='))
ηj= float(ηj.strip('j='))
fy= float(fy.strip('fy='))
γj= float(γj.strip('j='))
Fv= float(Fv.strip('Fv='))
An= float(An.strip('An='))

Vm = ((0.4*ft*b*H/1000)+((-N)*AwA)+(0.8*Fyv*Asv*H/s/1000))/γre
Vjd = γj*V*γre
maxV = max(ηj*Vm,Vjd)
As = int(1000*((maxV-0.8*(-N))/0.6-Fv*An)/fy)

print(0.4*ft*b*H/1000)
print((-N)*AwA)
print(0.8*Fyv*Asv*H/s/1000)
print(maxV)
print(Vm)
print(ft,AwA,Fyv,Asv,s,γre,fy,Fv,An,ηj,γj)
print(As)

