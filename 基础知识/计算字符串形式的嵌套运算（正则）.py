import re
origin = '1 - 2 *( (60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

while True:
    result = re.split('\(([^()]+)\)',origin,1)
    if len(result) == 3:
        print(result[1])
        before,content,after = result
        r = eval(content)
        new_str = before + str(r) + after
        origin = new_str
    else:
        print(eval(origin))
        break
