import math
while True:
    shape=input('what is the name of ur shape: ')
    if shape== 'exit':
        print('alright lets leave it')
        break
    if shape == 'circle':
        r= int(input('what is the radius of ur circle:'))
        pi=math.pi
        area=pi*r*r
        print('are of ur circle is:'+str(area)+'cm sq.')
    elif shape== 'square':
        x=int(input('what is the length of ur sq:'))
        area_sq= pow(x,2)
        print('area of ur sq:'+str(area_sq)+'cm sq.')
    elif shape== 'rectangle':
        l,b=map(int,input('what is length and breadth of your rect.:').split())
        area_rect= l*b
        print('area of your rect:'+str(area_rect)+'cm sq')
    else:
        print('-idc abt other shapes')