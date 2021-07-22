import xml.etree.ElementTree as et
import os.path
import sys
import getopt
import shutil
def main(argv):
   config_file = ''
   source_path = ''
   destination_path = ''
   file = ''
   try:
      opts, args = getopt.getopt(argv, "f:", ["file"])
   except getopt.GetoptError:
      print('python_test_1.py -f <config_file.xml>')
      sys.exit(2)
   for opt, arg in opts:
      if opt in ("-f", "--file"):
         config_file = arg

   if (os.path.exists(os.fspath(config_file)) == 0):
      print('Configuration file does not exist, please check path to the configuration file')
      sys.exit()


   tree = et.parse(os.fspath(config_file))
   try:
      source_path = tree.find(".//source_path").text
      destination_path = tree.find(".//destination_path").text
      file = tree.find(".//file_name").text
   except AttributeError:
      print('Wrong format of configuration file')
      sys.exit()
   if os.path.exists(destination_path) == 0:
      os.mkdir(destination_path)
   else:
      if os.path.exists(source_path + '/' + file):
                try:
                    shutil.copy(os.fspath(os.path.join(source_path, file)), destination_path)
                    print('Done - file is copied')
                except Exception as e:
                    print(format(e))
                    print('Unable to copy file')
      else:
         print('Source file not found')
if __name__ == "__main__":
   main(sys.argv[1:])
