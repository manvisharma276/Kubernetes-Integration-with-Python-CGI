#!/usr/bin/python3
import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue('n')
ip="65.2.80.246"
op = subprocess.getoutput("sudo ssh ec2-user@{} -i keyhadoop.pem -o stricthostkeychecking=no  \"sudo {}\"".format(ip,cmd))
print(op)

