from subprocess import Popen
p = Popen("create.bat", cwd=r"D:\Python\Projects\automation")
stdout, stderr = p.communicate()