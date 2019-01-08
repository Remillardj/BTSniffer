import os

# get log file size so we maintain checksum
def file_size(fileName):
  statinfo = os.stat(fileName)
  return statinfo.st_size

# truncate log to stay hidden, assuming we have write permissions
def truncate(fileName, size):
  file = open(fileName, "rw+")
  file.truncate(size)
  file.close()
