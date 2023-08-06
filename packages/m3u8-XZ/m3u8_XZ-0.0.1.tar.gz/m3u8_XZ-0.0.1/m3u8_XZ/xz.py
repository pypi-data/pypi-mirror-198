# -- coding:utf-8 --
# Time:2023-03-23 10:48
# Author:XZ
# File:xz.py
# IED:PyCharm
import time
import aiohttp
import asyncio
import requests as req
import re
import os


class M3U8:
    """
        url: m3u8文件的url
        folder: 下载文件后存储的名字
        run(): 执行下载
    """

    def __init__(self, url, folder='test'):
        # 下载文件名
        self.file_name = folder + '.mp4'
        # 下载存储文件夹
        self.path = './down_load/' + folder + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        # 缓存文件夹
        self.temp_path = self.path + 'temp/'
        if not os.path.exists(self.temp_path):
            os.makedirs(self.temp_path)
        # m3u8
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
        # 记录进度
        self.list_length = 0
        self.num = 0
        # 有序存储ts列表文件
        self.ts_list = list()

    # 通过ts名称，转换ts网址
    @staticmethod
    def get_full_ts_url(url, ts_name):
        # 分割ts name
        tl = ts_name.split('/')
        #
        new_url = []
        # 循环url，去掉ts name中重复的部分
        for s in url.split('/')[:-1]:
            if s in tl:
                tl.remove(s)
            new_url.append(s)
        # 拼接ts name
        new_url.extend(tl)
        result = '/'.join(new_url)
        # 返回
        return result

    # 通过url，获取ts列表
    def get_ts_list(self) -> list:
        res = req.get(self.url, headers=self.headers, verify=False)
        if res.status_code != 200:
            raise Exception('亲求失败,m3u8地址不存在')
        text = res.text
        # 去掉注释
        ts_str = re.sub('#.*?\n', '', text)
        # 转为列表
        self.ts_list = ts_str.split('\n')
        self.list_length = len(self.ts_list)
        return self.ts_list

    # 通过ts列表，异步缓存所有ts文件
    async def get_data(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for index, ts in enumerate(self.get_ts_list()):
                if ts:
                    # 给ts重命名，为了排序
                    temp_ts = str(index).zfill(6) + '.mp4'
                    # 创建task任务
                    task = asyncio.create_task(self.down_file(session, self.get_full_ts_url(self.url, ts), temp_ts))
                    tasks.append(task)
            # 添加到事件循环
            await asyncio.wait(tasks)

    # 异步下载二进制文件
    async def down_file(self, session, url, ts_name):
        async with session.get(url) as res:
            data = await res.read()
            with open(self.temp_path + ts_name, 'wb') as f:
                f.write(data)
                # 打印进度
                self.num += 1
                print('\r下载中:{:3.0f}%| {}/{}'.format(self.num / self.list_length * 100, self.num, self.list_length),
                      end='', flush=True)

    # 通过名称按序读取ts文件，整合成一个ts文件
    def combine_ts(self):
        # 获取所有缓存文件
        file_list = os.listdir(self.temp_path)
        if not file_list:
            return
        # 排序
        file_list.sort(key=lambda s: s.split('.')[0])
        # 文件总数
        length = len(file_list)
        # 开始合并文件
        with open(self.path + self.file_name, 'ab') as f:
            # 循环文件列表
            for i, file in enumerate(file_list):
                # 读取每个文件
                with open(self.temp_path + file, 'rb') as rf:
                    # 把每个文件的内容 追加到同一个文件
                    data = rf.read()
                    f.write(data)
                # 清除缓存文件
                os.remove(self.temp_path + file)
                # 打印进度
                print('\r合并中:{:3.0f}%'.format(i / length * 100), end='', flush=True)

    # 异步启动器
    def run(self):
        if self.url:
            stime = time.time()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.get_data())
            print('下载完成，准备合并...')
            time.sleep(2)
            self.combine_ts()
            print('\nover time : ', time.time() - stime)

