import os
import platform

#Determine OS and set path variable
if platform.system()!='Windows':
    mcuPath = os.path.join(os.getcwd(), 'common\mcu-list.txt')
elif platform.system()=='Windows':
    mcuPath = os.path.join(os.getcwd(), 'common\\mcu-list.txt')

mculist = set(line.strip() for line in open(mcuPath))