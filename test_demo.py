from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9223"
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}

    # self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'b0zqS-JeW7hxCDzNmBILz_4nr4f_z6faHHBk_Yob8A5DaX_i5DdgJPb0O6j6qg9wa1ZnYuU8KIAyF1DqvxYuA91SHd6CnuOKrWlOe1Ud9OmFGVMMXRSzZu3W3HaChKGSaUPfzvt3pKI0bpCS_JIoZbwB1895ps6iXOmovA3m8Qn1Cfx0iWSUkXXWnSWDwtYCCijhln_qbgbFfcUhik54mniiMJYG9ReXtY0xTwLdOZq1lncWIQvb5U3-89Bz7subVucCZfkjKRU0sZQxCzV_Lw'},
            {
                'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
                'value': '5_t-Q_WXOqoe6-9N_1WladKOYDzhxk5_oXgTEZRCMZSm-HMrQSS06KBdiNeBG7RJ'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
                'value': 'a8611802'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
             'secure': False, 'value': '1688851075546278'}, {'domain': '.work.weixin.qq.com',
                                                             'httpOnly': False,
                                                             'name': 'wxpay.vid', 'path': '/',
                                                             'secure': False,
                                                             'value': '1688851075546278'}, {
                'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                'secure': False,
                'value': '1970325045129850'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref',
                                               'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com',
                                                                                                  'expiry': 2147385600,
                                                                                                  'httpOnly': False,
                                                                                                  'name': 'pgv_pvid',
                                                                                                  'path': '/',
                                                                                                  'secure': False,
                                                                                                  'value': '4831127024'},
            {
                'domain': '.work.weixin.qq.com', 'expiry': 1621408770, 'httpOnly': False,
                'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                'value': '1589856573,1589872647'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True,
                                                    'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'},
            {
                'domain': '.qq.com', 'expiry': 1591514873, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/',
                'secure': False, 'value': '176427519@qq.com'}, {'domain': '.work.weixin.qq.com',
                                                                'expiry': 159254810388021, 'httpOnly': False,
                                                                'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False,
                                                                'value': 'zh'}, {'domain': '.work.weixin.qq.com',
                                                                                 'httpOnly': False,
                                                                                 'name': 'wwrtx.logined',
                                                                                 'path': '/', 'secure': False,
                                                                                 'value': 'true'}, {
                'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False,
                'value': '7221490281'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid',
                                         'path': '/', 'secure': False, 'value': '2720091508460100'},
            {'domain': '.qq.com',
             'expiry': 2147385600,
             'httpOnly': False,
             'name': 'pgv_pvi',
             'path': '/',
             'secure': False,
             'value': '3043866624'}, {
                'domain': '.qq.com', 'expiry': 2147483649488712, 'httpOnly': False, 'name': 'ptcz', 'path': '/',
                'secure': False, 'value': 'c0bcbcee87554615b0d450203c191d02af95332c3f4085b939784f7bd2a8a4bf'}, {
                'domain': '.qq.com', 'expiry': 2147483647698707, 'httpOnly': False, 'name': 'RK', 'path': '/',
                'secure': False, 'value': '0CQlkKWIMM'}]
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
