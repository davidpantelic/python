# test

def change_file(old, new):
  with open("py_test/text.txt", 'r') as file:
    data = file.read()

  data = data.replace(old, new)

  with open("py_test/text.txt", 'w') as file:
    data = file.write(data)
    



change_file('TEST', '____')