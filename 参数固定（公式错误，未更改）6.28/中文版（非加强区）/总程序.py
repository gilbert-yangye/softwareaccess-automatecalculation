#!usr/bin/python
# coding: utf-8


while True:
    print('想计算某一个特定墙板请输入‘1’；\n想计算数据库中所有墙板，并分别放在不同Excel工作表（可以计算不同的标准层），请输入‘2’；\n想计算数据库中所有墙板，并统一放同一份Excel工作表内（同一个标准层），请输入‘3’；\n想整理所有墙柱的最大As及对应楼层，请输入‘4’')

    whichcode = input()
    if whichcode == ('1'):
        import singlewall
        run = singlewall
        break
    
    elif whichcode ==('2'):
        import allfloors
        run = allfloors
        break

    elif whichcode == ('3'):
        import standardfloor
        run = standardfloor
        break
    
    elif whichcode == ('4'):
        import masterwall
        run = masterwall
        break
    
    else:
        print('请重新输入')
        continue

print('计算完成')

