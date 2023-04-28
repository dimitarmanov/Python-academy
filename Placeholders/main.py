import os

import location as location

if __name__ == '__main__':

    # source_file_path = "./test.txt"
    # destination_file_path = "./temp/test.txt"
    # os.mkdir("./temp")
    # os.replace(source_file_path,destination_file_path)
    file_dest = "./temp/"
    if os.path.isfile('test.txt'):
        os.remove("temp/test.txt")

    for x in range(10):
        open(file_dest + "file" + str(x) + ".txt" "w").close()






# Open, change and close file
    # name = "Dimitar"
    # country = "Bulgaria"
    # var2 = "Hello my name is ${NAME} and I'm from ${COUNTRY}"
    # with open("./test.txt", "r+") as f:
    #     file_content = f.read()
    #     file_content = file_content.replace("${NAME}", name).replace("${COUNTRY}", country)
    #     f.seek(0)
    #     f.write(file_content)
    #     f.truncate()






