'''
@文件名    :   test_blog.py
@邮箱好    ：   helinfengxs@163.com
@Author   :    helinfeng
------------      -------    --------    -----------
创建时间    :  2021/3/13 22:18
'''
import allure
import pytest

from web import webkeys
from params import datas
@allure.feature("UI自动化测试测试项目")
class Test_blog:

    def setup_class(self):
        '''
        初始化浏览器，打开浏览器
        '''
        self.web = webkeys.WebKey()

    def setup(self):
        '''
        用例开始前执行
        :return:None
        '''
        self.web.openBrowser()
    def teardown(self):
        '''
        用例结束
        :return:
        '''

        self.web.closeBorwser()
    @allure.story("登陆测试用例集")
    @pytest.mark.parametrize('listcases',datas['loginpage'])
    @allure.testcase("http://www.helinfengxs.com/admin")
    def test_login(self,listcases):
        allure.dynamic.title(listcases['title'])
        allure.dynamic.description(listcases['title'])
        '''
        登陆用例
        return: None
        '''
        testcases = listcases['case']
        try:
            for case in testcases:
                listcase = list(case.values())

                with allure.step(listcase[0]):
                    fun = getattr(self.web,listcase[1])
                    values = listcase[2:]
                    fun(*values)
            int('a')
        except Exception as e:
            allure.attach(self.web.driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            pytest.fail("用例执行失败")

    @allure.story("图片上传用例集")
    @pytest.mark.parametrize('listcases',datas['uploadimage'])
    @allure.testcase("http://www.helinfengxs.com/admin/upload")
    def test_uploadImage(self,listcases):
        pass
    def teardown_class(self):
        '''
        关闭浏览器
        :return:
        '''
        self.web.closeBorwser()
        print("用例执行完成")
