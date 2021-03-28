'''
@文件名    :   runner.py    
@邮箱好    ：   helinfengxs@163.com
@Author   :    helinfeng
------------      -------    --------    -----------
创建时间    :  2021/3/14 22:45
'''
import os

import pytest
pytest.main(["-s","test_blog.py","--alluredir","./temp"])
os.system("allure generate ./temp -o ./report --clean")