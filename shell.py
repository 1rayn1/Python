import basic

while True:
    command = input("line > ")
    result, error = basic.run("<stdin>", command)

    if error:
        print(error.as_string())
    else:
        print(result)