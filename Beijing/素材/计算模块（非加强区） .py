#formula
import codecs, re

print('请输入计算公式路径')

formulapath = input()

N = -89.49

V = 4.11

readformula = codecs.open(formulapath+'/计算公式.rtf','r','gbk')
formula = readformula.read()

regexγre= re.compile(r're=(?:-|)\d*(?:\.\d*|)')
regexj= re.compile(r'j=(?:-|)\d*(?:\.\d*|)')
regexfy= re.compile(r'fy=(?:-|)\d*(?:\.\d*|)')
regexFv= re.compile(r'Fv=(?:-|)\d*(?:\.\d*|)')
regexAn= re.compile(r'An=(?:-|)\d*(?:\.\d*|)')

γre= regexγre.findall(formula)[0]
fy= regexfy.findall(formula)[0]
γj= regexj.findall(formula)[0]
Fv= regexFv.findall(formula)[0]
An= regexAn.findall(formula)[0]

γre= float(γre.strip('re='))
fy= float(fy.strip('fy='))
γj= float(γj.strip('j='))
Fv= float(Fv.strip('Fv='))
An= float(An.strip('An='))

Vjd = γj*V*γre
As = int(1000*((Vjd-0.8*(-N))/0.6-Fv*An)/fy)

print(As)

