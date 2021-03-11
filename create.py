from subprocess import Popen
import sys

p = Popen("create.bat", cwd=r"D:\Python\Projects\automation")
stdout, stderr = p.communicate()
