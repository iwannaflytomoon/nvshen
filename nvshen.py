import os
import sys
import threading
import urllib2
from urllib2 import HTTPError

baseUrl = "http://www.nvshen.so/wp-content/uploads/2015/"
storageBasePath = "./nvshen/data/"

def downloadPic(url, filename):
    print url, "->", filename
    try:
        req = urllib2.Request(url)
        req.add_header("User-Agent", "fake-client")
        res = urllib2.urlopen(req)
        fp = file(filename, "wb")
        fp.write(res.read())
        fp.close()
    except HTTPError:
        pass

def main():
    if not os.path.exists(storageBasePath):
        os.makedirs(storageBasePath)
    monthList = ['01/', '02/']
    threads = []
    for i in monthList:
        storageDirPath = storageBasePath + str(i)
        if not os.path.exists(storageDirPath):
            os.mkdir(storageDirPath)

        for j in range(0, 3):
            picUrl = baseUrl + str(i) + str(j) + ".jpg"
            storageFileName = storageDirPath + str(j) + ".jpg"
            thr = threading.Thread(target = downloadPic, args=(picUrl, storageFileName))
            threads.append(thr)
    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
