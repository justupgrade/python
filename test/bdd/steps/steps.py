from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from app.code.bank.app import app, BANK
from app.code.bank.account import Account


@step(u'Given I create following account:')
def given_i_create_following_account(step):
    for row in step.hashes:
        a = Account(row['account_number'], row['balance'])
        BANK.add_account(a)


@step(u'Given I create account "([^"]*)" with balance of "([^"]*)"')
def given_i_create_account_group1_with_balance_of_group2(step, acc_nr, balance):
    account = Account(acc_nr, balance)
    BANK.add_account(account)


@step(u'And I visit the homepage')
def and_i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)
    # assert_equal(world.response.text, u'Hello World!')


@step(u'When I enter the account number "([^"]*)"')
def when_i_eneter_the_account_number_group1(step, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)


@step(u'Then I see the balance of "([^"]*)"')
def then_i_see_the_balance_of_group1(step, expected_balance):
    assert_in("Balance: {}".format(expected_balance), world.form_response.text)
