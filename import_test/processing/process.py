from import_test.db import connect


def do_it():
  print('MAGIC NUMBER IS', connect.MAGIC_NUMBER)
  connect.connect('tmoney', 'nbhack')
