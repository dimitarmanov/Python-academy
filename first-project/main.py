import requests

# class Response:
#     status_code = 200
#     def json(self):
#         return "DevOps"
#
# variable = {
#     "Authenticated": "Dma",
#     "age": "25"
#     }

# print(variable[0])



if __name__ == '__main__':
    # # r2 = Response()
    # print(r2.json(),r2.status_code)

    r = requests.get('https://httpbin.org/basic-auth/user2/pass2', auth=('user2', 'pass2'))
    if r.status_code == 200:
        print(r.json()["user"], "is logged in")
    else:
        print("User isn't logged in")



    # r1 = requests.get('https://www.python.org')
    # print(r1.status_code)
    #
    # r2 = requests.get('https://www.youtube.com')
    # print(r2.status_code)

    if True:
        pass

