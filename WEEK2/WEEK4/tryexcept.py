try:
    file = open("/home/brian/PythonEvening/WEEK2/WEEK4/randomfile.pdf", "w")
    data = file.read()
    print("The data is: ", data)
except FileNotFoundError:
    print("The file does not exist")
finally:
    print("This block of code will always run")
