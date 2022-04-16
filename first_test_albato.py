import requests
import mod


code = mod.update_group
headers = mod.headers
url = 'https://api-test.albato.ru' + code[0]
URL = set(url)
s = ('0123456789')

if code[1] == 'post':
    method = requests.post
elif code[1] == 'get':
    method = requests.get
elif code[1] == 'put':
    method = requests.put
elif code[1] == 'delete':
    method = requests.delete


# method exists
if code[2]:
    test = method(url, json=code[2], headers=headers)


else:
    test = method(url, headers=headers)


print('#' * 15, test.status_code, test.json())

assert test.status_code != 404, "Method doesn't exist - Test failed"


print('Method exists - Test OK')


# Entity found
if code[2]:
    test = method(url, json=code[2], headers=headers)


else:
    test = method(url, headers=headers)


if not test.json():
    if not test.json()['success']:
        print('#' * 15, test.status_code, test.json())
        assert test.json()[
            'errors'][0]['message'] != 'Сущность не найдена', 'Entity not found - Test failed'

print('#' * 15, test.status_code, test.json())
print('Entity found - Test OK')
# with authorization
if code[2]:
    test = method(url, json=code[2], headers=headers)

    print('#' * 15, test.status_code, test.json())
    print('Authorized - Test OK') if test.json() else print('Authorized - Test failed 1')

else:
    test = method(url, headers=headers)

    print('#' * 15, test.status_code, test.json())
    print('Authorized - Test OK') if test.json()[
        'success'] else print('Authorized - Test failed 2')

# without authorization
if code[2]:
    test = method(url, json=code[2])

    print('#' * 15, test.status_code, test.json())
    print(
        'UnAuthorized - Test OK') if test.status_code in (400, 401, 404) else print('UnAuthorized - Test failed 1')


else:
    test = method(url)

    print('#' * 15, test.status_code, test.json())
    print(
        'UnAuthorized - Test OK') if test.status_code in (400, 401, 404) else print('UnAuthorized - Test failed 2')


if code[2] or not URL.isdisjoint(set('1234567890')):

    # my own data
    test = method(url, json=code[2], headers=headers)

    print('#' * 15, test.status_code, test.json())
    print('My own data - Test OK') if test.json() else print('My own data - Test failed')

    # not my own data
    if not URL.isdisjoint(s):
        test = method(url[:-1], json=code[2], headers=headers)

        print('#' * 15, test.status_code, test.json())
        print(
            'Not my own data - Test OK') if test.status_code in (400, 404, 401) else print('Not my own data - Test failed')
    else:
        print("Not my own data - Test aren't relevant")

    # non-existent data
    if not URL.isdisjoint(s):
        test = method(url + '2132', json=code[2], headers=headers)

        print('#' * 15, test.status_code, test.json())
        print(
            'Non-existent data - Test OK') if test.status_code in (400, 404, 401) else print('Non-existent data - Test failed')
    else:
        print("Non-existent data  - Test aren't relevant")

else:
    print("Data - Tests aren't relevant")


# response
test = method(url, json=code[2], headers=headers)


if code[3]:
    test = method(url, json=code[2], headers=headers)
    print('#' * 15, test.status_code, test.json())
    p = set(code[3])

    if type(test.json()) == list and len(test.json()) != 0:
        print('Response - Test OK') if set(test.json()
                                           [0]) == p else print('Response - Test failed 1')

    else:
        if len(test.json()['data']) != 0:
            if type(test.json()['data']) == list:
                print('Response - Test OK') if set(test.json()
                                                   ['data'][0]) == p else print('Response - Test failed 2')

            elif type(test.json()['data']) == dict:
                print('Response - Test OK') if set(test.json()
                                                   ['data']) == p else print('Response - Test failed 3')
        else:
            print('Response - Test OK')


else:
    print("Test response aren't relevant")

