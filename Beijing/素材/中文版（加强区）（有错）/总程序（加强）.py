#!usr/bin/python
# coding: utf-8


while True:
    print('单个墙柱查询,请输入‘1’；\n计算标准层中最大的As，请输入‘2’；\n计算标准层所有As，请输入‘3’；\n计算自然层所有数据，请输入‘4’')

    whichcode = input()
    if whichcode == ('1'):
        import 单个墙柱查询
        run = 单个墙柱查询
        break
    
    elif whichcode ==('2'):
        import 标准层最大As
        run = 标准层最大As
        break

    elif whichcode == ('3'):
        import 标准层所有数据
        run = 标准层所有数据
        break
    
    elif whichcode == ('4'):
        import 自然层所有数据
        run = 自然层所有数据
        break
    
    else:
        print('请重新输入')
        continue

print('计算完成')

