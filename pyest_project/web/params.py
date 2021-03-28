'''
@文件名    :   params.py    
@邮箱好    ：   helinfengxs@163.com
@Author   :    helinfeng
------------      -------    --------    -----------
创建时间    :  2021/3/14 23:45
'''
# 获取当前脚本所在文件夹路径
import os
import yaml

datas = None
curPath = os.path.dirname(os.path.realpath(__file__))
# 获取yaml文件路径
yamlPath = os.path.join(curPath+""+"\\lib\\case", "case.yaml")
with open(yamlPath,encoding='utf8') as f:
    datas = yaml.load(f,Loader=yaml.FullLoader)
print(datas)