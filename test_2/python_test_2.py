import xml.etree.ElementTree as et
import os.path
import sys
import getopt
import hashlib

def main(argv):
   input_file = ''
   dir = ''
   try:
      opts, args = getopt.getopt(argv, 'f:d:', ['file=, dir='])
   except getopt.GetoptError:
      print('python_test_2.py -f <input_file.txt> -d <checking dir> ')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-f", "--file"):
         input_file = os.fspath(arg)
      elif opt in ("-d", "--dir"):
         dir = os.fspath(arg)

   if (os.path.exists(input_file) == 0) or (os.path.exists(dir) == 0):
      print('File or directory does not exist')
      sys.exit()

   try:
      with open(input_file, 'r') as f:
         for line in f:
            if len(line.split()) == 3:
               filename = line.strip().split()[0]
               algorithm = line.strip().split()[1]
               hash = line.strip().split()[2]
            else:
               print('Wrong format of source file')
               sys.exit()
            BUF_SIZE = 65536
            md5 = hashlib.md5()
            sha1 = hashlib.sha1()
            sha256 = hashlib.sha256()
            hash_sum = ''
            try:
               with open(dir + '/' + filename, 'rb') as f2:
                  while True:
                     data = f2.read(BUF_SIZE)
                     if not data:
                        break
                     md5.update(data)
                     sha1.update(data)
                     sha256.update(data)
               if algorithm == 'md5':
                  hash_sum = md5.hexdigest()
               elif algorithm == 'sha1':
                  hash_sum = sha1.hexdigest()
               elif algorithm == 'sha256':
                  hash_sum = sha256.hexdigest()
               else:
                  print(filename, "Unknown hashing algorithm")

               if hash == hash_sum:
                  print(filename, "OK")
               else:
                  print(filename, "FAIL")
            except FileNotFoundError as e:
               print(filename, "NOT FOUND")


   except FileNotFoundError as e:
      print(e)
      print('Problem to open file')
      sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])