# -*- coding: utf-8 -*-
# !/usr/bin/python3


import sys
import subprocess
import os
import paramiko


def local(file):
  os.environ['HOME']
  os.path.expandvars('$HOME')
  home = os.path.expanduser('~')
  print(home)
  os.getcwd()
  os.chdir(home + '/workspace/' + file + '-service')
  cmd('git pull origin dev')
  cmd('gradle clean build')
  cmd('docker build -t registry.xzlcorp.com/xzl-dev/' + file + '-service .')
  cmd('docker push registry.xzlcorp.com/xzl-dev/' + file + '-service')


def cmd(cmd):
  print("---------------")
  print(cmd)
  print("-----")
  process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, shell=True, bufsize=1)
  while process.poll() is None:
    line = process.stdout.readline()
    line = line.strip()
    if line:
      print(str(line, encoding='utf-8'))


def dev(ip, uname, file, port, srvname):
  passwd = 'dev'
  name2 = file.replace("-", "_") + "_svc"
  name = file.replace("-", "_") + "_srv"
  srv = file.replace("-", "_") + srvname
  print(name)
  pull = 'docker pull registry.xzlcorp.com/xzl-dev/' + file + '-service'
  stop = 'docker ps -a | grep -w ' + name + ' | cut -d \' \' -f 1 | xargs --no-run-if-empty docker stop | xargs --no-run-if-empty docker rm -f'
  stop2 = 'docker ps -a | grep -w ' + name2 + ' | cut -d \' \' -f 1 | xargs --no-run-if-empty docker stop | xargs --no-run-if-empty docker rm -f'
  start = 'docker run -d --log-opt max-size=10m -e HOST_IP=$(hostname -i) -p ' + port + ':' + port + ' --name ' + srv + ' registry.xzlcorp.com/xzl-dev/' + file + '-service --server.port=' + port + ' --spring.cloud.config.profile=dev'
  cmd = [pull, stop, stop2, start]
  print(cmd)
  ssh2(ip, uname, passwd, cmd)
  print()


def ssh2(ip, username, passwd, cmd):
  try:
    home = os.path.expanduser('~')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    pkey = home + '/.ssh/xinzhili-dev.pem'
    key = paramiko.RSAKey.from_private_key_file(pkey)
    print(pkey)
    ssh.connect(ip, username=username, timeout=5, pkey=key)
    for m in cmd:
      print("---------------")
      print(m)
      print("-----")
      stdin, stdout, stderr = ssh.exec_command(m, get_pty=True)
      out = stdout.readlines()
      # 屏幕输出
      for o in out:
        print(o),
    print('%s\tOK\n' % (ip))
    ssh.close()
  except:
    print('%s\tError\n' % (ip))


def main(argv):
  print(str(argv))
  doctor = ['doctor-api', '9007', 'ubuntu', '162', '_svc']
  patient = ['patient-api', '9001', 'ubuntu', '118', '_svc']
  user = ['user', '9005', 'ubuntu', '118', '_srv']
  business = ['business', '8089', 'dev', '175', '_srv']
  medical = ['medical', '9008', 'ubuntu', '162', '_svc']
  dpc = ['dpc', '9006', 'ubuntu', '118', '_svc']
  chat = ['chat', '9011', 'ubuntu', '52', '_srv']
  ip = "172.16.10."
  try:
    if argv[1] == 'doctor':
      arr = doctor
    if argv[1] == 'patient':
      arr = patient
    if argv[1] == 'user':
      arr = user
    if argv[1] == 'business':
      arr = business
    if argv[1] == 'medical':
      arr = medical
    if argv[1] == 'dpc':
      arr = dpc
    if argv[1] == 'chat':
      arr = chat
    else:
      print('参数应为 doctor patient user business medical dpc')
    name = arr[0]
    port = arr[1]
    uname = arr[2]
    ip = ip + arr[3]
    srvname = arr[4]
  except:
    print('参数应为 doctor patient user business medical dpc')
  local(name)
  dev(ip, uname, name, port, srvname)


if __name__ == '__main__':
  main(sys.argv)
