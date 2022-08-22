# -*- coding: utf-8 -*-
# @Time    : 2022/8/22 17:19
# @Author  : mollie
# @FileName: test_allure.py
# @Software: PyCharm
import pytest

class TestCase:
    def test_01(self):
        print('---用例01---')
        assert 1
    def test_02(self):
        print('---用例02---')
        assert 1
    def test_03(self):
        print('---用例03---')
        assert 0
if __name__ == '__main__':
    pytest.main(['-s'])