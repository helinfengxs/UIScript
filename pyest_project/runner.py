'''
@文件名    :   runner.py    
@邮箱好    ：   helinfengxs@163.com
@Author   :    helinfeng
------------      -------    --------    -----------
创建时间    :  2021/3/14 13:47
'''
import pytest

pytest.main(["-s","suites//test_example.py","-n","2"])