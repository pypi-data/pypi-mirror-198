import pypdl
import time

if __name__ == '__main__':
    d = pypdl.Downloader()
    url = "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe"
    d.start(url, "r.exe")
    print("hello")
    # th = threading.Thread(target=d.start, args=(url,"dfd.exe",2))
    # th.start()
    # while True:
    #     print(d.progress,d.speed,d.eta,d.doneMB,d.totalMB,d.remaining,d.time_spent,d.download_mode)
    #     time.sleep(1)
    # time.sleep(2)
    # d._Error.set()
    # print(id(d._Error),id(d._signal))
    # time.sleep(4)
    # d._Error.set()
    # print(id(d._Error),id(d._signal))
    # print("stoped 2")
    # time.sleep(3)
    # d._Error.set()
    # print(id(d._Error),id(d._signal))
    # print("stoped 3")
    # time.sleep(2)
    # print("stoping")
    # d.stop()
    # print(id(d._Error),id(d._signal))
    # time.sleep(2)
    # print("restarting")
    # d.start(url, "r.exe", 2,True,block=False,retries=4)
    # print(id(d._Error),id(d._signal))

# pypi-AgEIcHlwaS5vcmcCJDI1YjdhNDMxLTgwODktNDgxNy1iYThmLWIwZTMxNjQ3OTVlYQACDVsxLFsicHlwZGwiXV0AAixbMixbImZiNjM2YzdlLWQzYmEtNGRkYi04YmI4LWMwYzZkZjllOTk4NCJdXQAABiAf1lRMH7TMDf8GQERzIQRcMokgpCGGeZHCbyTKodtfww