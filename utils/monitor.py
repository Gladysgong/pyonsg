# -*- coding:utf-8 -*-
from datetime import datetime
import pexpect
import threading
import pymysql
import sys
import time
import signal
import os

database_host="10.134.110.163"
database_data="sogotest"
database_table="fanyi_fymonitor"
database_user="root"
database_pass="Zhangjj@sogou123"
monitor_id = int(sys.argv[1])
host_id = sys.argv[2]

# 主方法
def ssh_command(user, host, password, command):
    ssh_new_key = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_new_key, 'password: '])
    if i == 0:
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        return None
    if i == 1:
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0:
            print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
    child.sendline(password)
    return child

#gpu mem
def gpu_info():
    leave_num = 0
    while True:
        child = ssh_command("root", "10.153.51.60", "sogourank@2016", "nvidia-smi | grep 250W")
        child.expect(pexpect.EOF)
        gpuinfo = (child.before).decode('utf-8')
        gpu_lst = gpuinfo.strip().split('\r\n')
        g_mem=gpu_lst[0].split()[8].split('MiB')[0]
        g_used=gpu_lst[0].split()[12].split('%')[0]
        timedata = datetime.now().strftime('[Date.UTC(%Y,%m,%d,%H,%M,%S)')
        gpumeminfo = timedata+","+g_mem+'],\n'
        gpumemused = timedata+","+g_used+'],\n'
        db = pymysql.connect(database_host, database_user, database_pass, database_data)
        cursor = db.cursor()
        sql = "UPDATE %s set gpumem=CONCAT(gpumem, '%s'),gpumemused=CONCAT(gpumemused, '%s') where id=%d;" % (database_table, gpumeminfo, gpumemused,monitor_id)
        cursor.execute(sql)
        try:
            db.commit()
        except:
            db.rollback()
        leave_num += 1
        time.sleep(5)


def sig_handler(sig, frame):
    sys.exit()

signal.signal(signal.SIGTERM, sig_handler)

if __name__ == '__main__':
    try:
        # t1 = threading.Thread(target=gpu_info)
        # t1.start()
        subpid = os.getpid()
        print(subpid)
        db = pymysql.connect(database_host, database_user, database_pass, database_data)
        cursor = db.cursor()
        sql = "UPDATE fanyi_host set runningPID='%s',status=1 where id=%d;" % ( subpid, host_id)
        cursor.execute(sql)
        try:
            db.commit()
        except:
            db.rollback()
        gpu_info()

    except Exception as e:
        print(str(e))
