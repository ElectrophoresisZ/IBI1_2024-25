'''
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！") 
'''

import sys

for arg in sys.argv[1:]:
    print(f'{arg}')
