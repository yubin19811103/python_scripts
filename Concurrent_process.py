# !/usr/bin/python
# -*- coding: UTF-8 -*-

import multiprocessing
from multiprocessing import Pool
import time
import os


lock = multiprocessing.Condition(multiprocessing.Lock())
def s(x):
    run_l = []
    lock.acquire()
    with open("databgi.txt","r+") as f:
        for i in f.readlines():
            run_l.append(i.strip())
        #print run_l

        if x in run_l:
            lock.release()
            return
        f.write(x + "\n")
    lock.release()
    time.sleep(10)
    print x
    os.system("cat /root/databgi/%s |xargs -i /root/genedock_client_cmd_linux_x64/bin/genedock upload /www1{} /chinacdc/MetaGenome{} --internal" % (x))

if __name__ == '__main__':
    l = []
    o = os.popen('ls /root/databgi/')
    # print o.read()
    for i in o:
        l.append(i.strip())
    p = Pool(processes = 4)
    if not os._exists("databgi.txt"):
        w = open("databgi.txt","w+")
        w.close()
    p.map(s,l)
    p.close()
    p.join()
