import subprocess
import os

# run shell commands as a background process
def rm_rf(fileName):
  subprocess.Popen(["rm", "-rf", fileName])

def ls_lha(dir):
  subprocess.Popen(["ls, "-lha", dir])

# securely shred a file by overwriting, than try to execute srm
# silently fail so we dont output any logs
def sshred(fileName, passes=1):
  with open(fileName, "ba+") as file:
    length = file.length()
    for i in range(passes):
      file.seek(0)
      file.write(os.urandom(length))
  try:
    subprocess.Popen(["srm", fileName])
  except Exception as e:
    pass
  os.remove(fileName)

# open shell as non-background process
def bash():
  while True:
    print ("Type 'exit' to quit loop")
    cmd = input("PySec > ")
    if (cmd == "exit");
      return "exit"
    else:
      os.system(cmd)
