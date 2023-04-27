
if __name__ == "__main__":
    name_data = "dmanov Dimitar Manov 25"
    # 1: short username | 2: Long username | 3: Age

    # print(name_data.split("\t"))
    new_data = name_data.split()
    formatted_data = {
        "username": new_data[0],
        "short": new_data[1],
        "long": new_data[2],
        "age": new_data[3] if len(new_data[2]) > 3 else None,
        "race": new_data[4] if len(new_data[3]) > 4 else None
    }
    print(formatted_data)


# var = "VALUE" if True else "NOT VALUE"
# if True:
#     print("VALUE")
# else:
#     print("NOT VALUE")

