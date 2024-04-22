#!/usr/bin/env python
#Script usage:
##python google_auth.py

import subprocess
import os
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

#Writes goo.sh
f = open("goo.sh", "a")
f.write('#!/bin/bash\n\n')
f.write('yum install -y expect\n')
f.write('echo "STARTED to Set-up GOOGLE-AUTHENTICATOR"\n')
f.write('GOOGLE_AUTH=$(expect -c "\n')
f.write('spawn google-authenticator\n')
f.write('expect \\"Do you want authentication tokens to be time-based (y/n) \\"\n')
f.write('send \\"y\\r\\"\n')
f.write('expect \\"Do you want me to update your "/root/.google_authenticator" file? (y/n)\\"\n')
f.write('send \\"y\\r\\"\n')
f.write('expect \\"Do you want to disallow multiple uses of the same authentication\n')
f.write('token? This restricts you to one login about every 30s, but it increases\n')
f.write('your chances to notice or even prevent man-in-the-middle attacks (y/n) \\"\n')
f.write('send \\"y\\r\\"\n')
f.write('expect \\"Do you want to do so? (y/n) \\"\n')
f.write('send \\"y\\r\\"\n')
f.write('expect \\"Do you want to enable rate-limiting? (y/n) \\"\n')
f.write('send \\"y\\r\\"\n')
f.write('expect eof\n')
f.write('")\n')
f.write('yum remove -y expect\n')
f.close()
os.chmod("goo.sh", 755)

#Install Google Authenticator
subprocess.run('yum -y install epel-release', shell=True)
subprocess.run('yum -y install google-authenticator', shell=True)
subprocess.run('./goo.sh', shell=True)

#Configuring File
file1 = open("/etc/pam.d/sshd", "a")
file1.write("auth    required      pam_unix.so     try_first_pass\n")
file1.write("auth    required      pam_google_authenticator.so")
file1.close()
file2 = open("/etc/ssh/sshd_config", "a")
file2.write("Match User administrator\n")
file2.write("    AuthenticationMethods keyboard-interactive")
file2.close()
replace_line('/etc/ssh/sshd_config', 67, 'ChallengeResponseAuthentication yes\n')
replace_line('/etc/ssh/sshd_config', 68, '#ChallengeResponseAuthentication no\n')
subprocess.run('systemctl restart sshd', shell=True)
os.remove("goo.sh")

#Displays Google_Authenticator_Key
f=open('/root/.google_authenticator')
lines=f.readlines()
print ("Your new secret key is: " + lines[0])
print ("Your emergency scratch codes are:")
print (lines[5])
print (lines[6])
print (lines[7])
print (lines[8])
print (lines[9])
