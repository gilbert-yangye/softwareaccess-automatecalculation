#!usr/bin/python
# coding: utf-8


while True:
    print('非加强区请输入‘1’；加强区请输入‘2’')
    whicharea = input()
    
    if whicharea == ('1'):
        print('已选择非加强区')
        print('单个墙柱查询,请输入‘1’；\n计算标准层中最大的As，请输入‘2’；\n计算标准层所有As，请输入‘3’；\n计算自然层所有数据，请输入‘4’')
        whichcode = input()

        if whichcode == ('1'):
            import single
            run = single
            break
        
        elif whichcode ==('2'):
            import maxstandard
            run = maxstandard
            break

        elif whichcode == ('3'):
            import standard
            run = standard
            break
        
        elif whichcode == ('4'):
            import natural
            run = natural
            break
    
        else:
            print('请重新输入')
            continue

    elif whicharea == ('2'):
        print('已选择加强区')
        print('单个墙柱查询,请输入‘1’；\n计算标准层中最大的As，请输入‘2’；\n计算标准层所有As，请输入‘3’；\n计算自然层所有数据，请输入‘4’')
        whichcode = input()

        if whichcode == ('1'):
            import singles
            run = singles
            break
    
        elif whichcode ==('2'):
            import maxstandards
            run = maxstandards
            break

        elif whichcode == ('3'):
            import standards
            run = standards
            break
    
        elif whichcode == ('4'):
            import naturals
            run = naturals
            break
    
        else:
            print('请重新输入')
            continue
        

print('计算完成')

