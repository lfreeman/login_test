# -*- coding: utf-8 -*-
__version__ = '0.1'

from datetime import datetime
from lxml import html
import requests
import logging
import time

class LoginTestLib(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def setup_login_test_environment(self):
        self.account, self.email = self.generate_random_email_account()

    def clean_login_test_environment(self):
        pass

    def setup_login_test(self):
        pass

    def clean_login_test(self):
        pass

    def generate_random_email_account(self):
        domain = 'mailinator.com'
        account = 'klctD0' + datetime.now().strftime("%y%m%d%H%M%S")
        email = '%s@%s' % (account, domain)
        return [account, email]

    def verification_email_is_received(self, account):
        time.sleep(30)
        url = 'http://%s.mailinator.com' % account
        page = requests.get(url)
        tree = html.fromstring(page.text)
        email_links = tree.xpath('//a/@href')
        full_link = 'http://mailinator.com' + email_links[-1]
        logging.debug(full_link)
        email_page = requests.get(full_link)
        tree = html.fromstring(email_page.text)
        link = tree.xpath('//a/@href')[-1]
        assert 'www.interviewstreet.com/recruit2/useraccount/activateEmail/' in link
        page = requests.get(link)

