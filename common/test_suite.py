
from testcases.test_register import Register_Test
from common.contants import *
import os
import unittest
import HTMLTestRunnerNew
from common.context import *

# suite_register=unittest.TestSuite()
# loader=unittest.TestLoader()
# suite_register.addTest(loader.loadTestsFromTestCase(Register_Test))

discover=unittest.defaultTestLoader.discover(testcases_dir,"test_*.py")
reports=os.path.join(reports_dir,'reports.html')
with open(reports,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                     verbosity=2,
                                     title='测试注册类',
                                     description='注册类测试结果',
                                     tester='海绵宝宝')
    runner.run(discover)
