from import_test.processing import process


def do_something(test_mode=False):
  print(f'Doing something!')
  process.do_it()


# Run with: python -m import_test.main
if __name__ == '__main__':
  do_something(test_mode=True)
