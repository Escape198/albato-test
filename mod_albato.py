import requests


url = 'https://api-test.albato.ru'

# get token
auth_token = ['/user/auth', 'post',
              {'email': 'email', 'password': 'password'}]
requests_auth = requests.post(url + auth_token[0], data=auth_token[2])
token = requests_auth.json()['data']['authToken']
headers = {'Authorization': 'Bearer {}'.format(token),
           'Content-Type': 'application/json',
           }

# ==== methods ====
# auth
restore_password = ['/user/auth/restore-password',
                    'post', {'email': 0}, {}]
exit = ['/user/auth', 'delete', {'authToken': token}, {}]
update_token = ['/user/auth', 'put', {'Authorization': token},
                {'authToken': 0, 'authTokenExpirationDateTime': 0}]
change_confirmation = ['/user/auth/confirm-restore-password',
                       'post', {'token': token, 'password': 0}, {}]  # need token change confirmation
add_user = ['/user/auth/sign-up', 'post',
            {'email': 0, 'password': 0, 'phone': 0}, {'id': 0, 'active': 0}]


# balance
balance_history = ['/user/balance/history', 'get', {}, {}]


# banner
banner = ['/banner', 'get', {}, {}]
mark_banner = ['/banner/mark-as-read/5', 'post', {}, {}]


# billing
prolong_services = ['/billing/prolong-services', 'get', {}, {'id': 0, 'currency': 0, 'months': 0, }]
order_checkout = ['/billing/order-checkout/49', 'post',
                  {'paymentType': 1, 'autoPayment': 1, 'payFromBalance': 100}, {}]  # need active order
cancel_plan = ['/billing/cancel-plan', 'post', {}, {}]
apply_promocode = ['/billing/apply-promocode-to-order/:id',
                   'post', {'promocode': ''}, {}]  # need active order
checkout = ['/billing/checkout', 'post', {'id': 41, 'months': 3}, {}]
create_prolong_checkout = ['/billing/prolong-checkout', 'post',
                           {'months': 3}, {}]  # need order 'Не удалось оформить заказ услуг'
services = ['/billing/services', 'get', {}, {'id': 0, 'type': 0, 'currency': 0, 'title': 0, 'bundlesLimit': 0,
                                             'bundleDataLimit': 0, 'transactionsLimit': 0, 'credentialsLimit': 0,
                                             'extraCredentialPrice': 0, 'monthlyPrice': 0, 'trxOverheadPrice': 0,
                                             'isFree': 0, 'months': 0}]
bank_invoices = ['/billing/bank-invoices', 'get', {}, {}]


# BillingOrder
order = ['/billing/order/:id', 'get', {}, {}]  # need active order


# bundle
restore_bundle = ['/bundle/restore', 'post',
                  {'ids': [108224, 108223]}, {'id': 0, 'status': 0, 'deleted': 0, 'error': 0}]
play_bundle = ['/bundle/play', 'post', {'ids': '108224'}]  # need trigger :3
transactions_bundle = ['/bundle/transactions', 'get',
                       {}, {'bundleId': 0, 'planPeriod': 0, '24h': 0}]
copy_bundle = ['/bundle/copy/108224', 'post', {'title': 'copy'}, {'newBundleId': 0}]
pause_bundle = ['/bundle/pause', 'post', {'ids': []}]  # to play first
cancel_historic_run = ['/bundle/108224/historic-run/cancel',
                       'post', {}]  # need try with historic run
move_bundle = ['/bundle/move-to-group/571', 'post',
               {'ids': [108224, 108223]}, {'groupId': 0, 'ids': 0}]
available_frequency = ['/bundle/108224/available-frequency', 'get',
                       {}, {}]  # ! response
edit_bundle = ['/bundle/108224', 'put', {'title': 'test',
                                         'groupId': '571', 'startDate': '2022-03-22'}, {'historicRunConfig': 0, 'id': 0, 'groupId': 0, 'status': 0, 'blocked': 0, 'title': 0, 'dateCreated': 0, 'dateDeleted': 0, 'dateUpdated': 0, 'launchMode': 0, 'frequency': 0, 'startDate': 0, 'endDate': 0, 'timeIntervalFrom': 0, 'timeIntervalTo': 0, 'daysOfWeek': 0, 'daysOfMonth': 0, 'historicRun': 0, 'historicRunType': 0}]  # remove 'steps'
create_bundle = ['/bundle', 'post', {'title': 'test', 'groupId': '571'}, {'historicRunConfig': 0, 'id': 0, 'groupId': 0, 'status': 0, 'blocked': 0, 'title': 0, 'dateCreated': 0, 'dateDeleted': 0,
                                                                          'dateUpdated': 0, 'launchMode': 0, 'frequency': 0, 'startDate': 0, 'endDate': 0, 'timeIntervalFrom': 0, 'timeIntervalTo': 0, 'daysOfWeek': 0, 'daysOfMonth': 0, 'historicRun': 0, 'historicRunType': 0}]
get_bundle = ['/bundle', 'get', {}, {'historicRunConfig': 0, 'id': 0, 'groupId': 0, 'status': 0, 'blocked': 0, 'title': 0, 'dateCreated': 0, 'dateDeleted': 0, 'dateUpdated': 0,
                                     'launchMode': 0, 'frequency': 0, 'startDate': 0, 'endDate': 0, 'timeIntervalFrom': 0, 'timeIntervalTo': 0, 'daysOfWeek': 0, 'daysOfMonth': 0, 'historicRun': 0, 'historicRunType': 0}]
test_run_bundle = ['/bundle/test-run/bundle/108224', 'get', {}]  # !
test_run_action = ''
delete_bundle = ['/bundle/delete', 'post',
                 {'ids': [108224, 108223]}, {'id': 0, 'status': 0, 'deleted': 0, 'error': 0}]


# bundle data
bundle_data = ''
copy_data = ['/bundle/data/copy/:id', 'post', {}]  # !
edit_data = ''
create_data = ['/bundle/data', 'post', {'bundleId': '',
                                        'type': '', 'level': '', 'credentialId': ''}]  # !
delete_data = ''


# bundle group
add_group = ['/bundle/group', 'post', {'name': 'test'}]
get_group = ['/bundle/group', 'get', {}]
update_group = ['/bundle/group/594', 'put', {'name': 'test'}]
get_groupid = ['/bundle/group/594', 'get', {}]
delete_group = ['/bundle/group/591', 'delete', {}]


# bundle history
rerun = ''
bundle_history = ''


# bundle templates
template_setting = ''
get_template = ''
create_template = ''


# credential
oauth_credential = ''


# credentials
# 20 Telegram, 135 Gmail, 31 Email, 23 Facebook
trello_oauth_redirect = ''
meta_credentials = ['/credentials/23/meta', 'get', {},
                    {'hasWebhookCatcher': 0, 'canBeTested': 0, 'fields': 0, 'scenarios': 0}]
update_user_data = ['/credentials/23/15739/update-user-data', 'post', {}, {'updateStatus': 0}]
credentials = ['/credentials', 'get', {},
               {'id': 0, 'partnerId': 0, 'updateDateTime': 0, 'fields': 0, 'updateStatus': 0}]
get_credential = ['/credentials/23/15739', 'get', {},
                  {'id': 0, 'partnerId': 0, 'updateDateTime': 0, 'fields': 0, 'updateStatus': 0}]
test_credential = ['/credentials/23/15739/test', 'get', {}, {'result': 0, 'message': 0}]
edit_credential = ['/credentials/23/15739', 'put', {'title': 'Test'}, {
    'id': 0, 'partnerId': 0, 'updateDateTime': 0, 'updateStatus': 0, 'fields': 0}]
create_credential = ['/credentials/23', 'post', {'title': 'Test 2132'}, {
    'id': 0, 'partnerId': 0, 'updateDateTime': 0, 'updateStatus': 0, 'fields': 0}]
delete_credential = ['/credentials/23/15745', 'delete', {}, {}]


# credentials wizard
update_credentials_wizard = ''
get_credentials_wizard = ''
create_credentials_wizard = ''
save_credentials_wizard = ''


# error
error = ''


# event history
events_steps = ''
events = ''


# ip
get_ip = ''


# instruments
#
#
#
#
#


# notifications
notifications_mark_as_read = ''
notifications_mark_as_deleted = ''
user_notifications = ''


# partner
get_partner_list = ['/partners', 'get', {}, {'id': 0, 'parentId': 0,
                                             'label': 0, 'shortName': 0, 'hasCredential': 0, 'info': 0}]



