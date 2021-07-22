import os.path
import sys
import getopt
import time
import shutil
class Logger(object):
    def __init__(self, filename="python_test_3_result.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
class BaseTestCase(object):
    def __init__(self):
        self.tc_id = '';
        self.name = ''
    def prep(self):
        return
    def run(self):
        return
    def clean_up(self):
        return
    def execute(self):
        print('EXECUTE: ', self.name)
        try:
            if self.prep():
                self.run()
                self.clean_up()
            else:
                print('  Unable to perform preparation steps ', self.name)
        except Exception as exp:
            print(format(exp))
            print('  Unable to execute test ', self.name)

class TestCase1(BaseTestCase):
    def __init__(self, id='1', test_name='Test1'):
        self.tc_id = id;
        self.name = test_name
    def prep(self):
        print('PREPARATION: ', self.name)
        print('  system time in seconds: ', round(time.time()))
        return (bool(round(time.time()) % 2 == 0))
    def run(self):
       print('RUN: ', self.name)
       try:
            os.system('ls -A1')
       except OSError as e:
            print(format.e)
            print('  Unable to run ', self.name)
    def clean_up(self):
        print('CLEAN_UP: ', self.name)
        return

class TestCase2(BaseTestCase):
    def __init__(self, id='2', test_name='Test2', filename = '/root/test_python_3_file', ram_size = 1024, size_file=1048576):
        self.tc_id = id;
        self.name = test_name
        self.filename = filename
        self.ram_size = ram_size
        self.size_of_file = size_file
    def prep(self):
        print('PREPARATION: ', self.name)
        total_memory, used_memory, free_memory = map(
            int, os.popen('free -t -m').readlines()[-1].split()[1:])
        print('  total memory: ', total_memory)
        return (bool(total_memory > self.ram_size))
    def run(self):
        print('RUN: ', self.name)
        file = open(self.filename, 'w+')
        with open(self.filename, 'wb') as f:
            f.seek(self.size_of_file)  # One Mb
            f.write(os.urandom(self.size_of_file))
    def clean_up(self):
        print('CLEAN_UP: ', self.name)
        os.remove(self.filename)
        print('  file has been removed')


def main(argv):
   input_file = ''
   dir = ''
   try:
      opts, args = getopt.getopt(argv, 'f:d', ['file=, dir='])
   except getopt.GetoptError:
      print('python_test_3.py -f <input_file> -d <checking dir> ')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-f", "--file"):
         input_file = arg
      elif opt in ("-d", "--dir"):
         dir = arg


if __name__ == "__main__":
   main(sys.argv[1:])
   #if you want to redirect console stdout into file - uncomment this line
   #sys.stdout = Logger("python_test_3_result.log")
   tc1 = TestCase1()
   tc1.execute()
   tc2 = TestCase2()
   tc2.execute()