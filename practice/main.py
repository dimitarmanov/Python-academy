var1 = "string1"
var2 = 2
var3 = True
var4 = 5
var5 = "string2"
sum_vars = var1 + "_" + var5

ar = ["string1", 2, True, 5, "string2"]
obj = {
    "key": "value",
    "key2": "value2",
    "key2": "value2",
    1:23,
    2:False,
    "3":["asd", 23, 555]
}

# int("string")
# str("int")
# bool("string")


if __name__ == '__main__':
    # for a in obj["3"]:
    #     if isinstance(a,int):
    #         print("Hello Integer", a)
    #     else:
    #         print("Not integer")
    #     print(a)
    #  print(ar)
    # print(var2 + var4)
    #
    # if var3 == True:
    #     print(sum_vars)



farms = {
    "farm": {
        "animal":[
            {
                "cow": {
                    "milk": 10
                }
            }
        ]
    }
}

    for a in farms:
        print(a)