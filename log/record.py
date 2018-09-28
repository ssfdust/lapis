# -*- coding: utf-8 -*-
"""
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨

日志监控模块(LapisLog):
    * 监控阅读条目数量
    * 监控写入条目数量
    * 监控CPU状态
    * 监控内存状态
    * 任务进程独占
"""

from bson.objectid import ObjectId
from lapis.log.models import (
    Task,
    Process,
    Log
)

import os
import platform
import psutil

class LapisLog(object):
    """
    log对象
    单例模式 单个进程中共用一个对象
    """
    # 单例变量
    _instance = {}

    def __new__(cls, *args, **kwargs):
        """根据pid参数识别的单例模式
           一次只允许一个实例存在
        """
        pid = kwargs.get('pid')
        if pid is not None and pid not in cls._instance:
            cls._instance[pid] = super(LapisLog,
                                       cls).__new__(cls)
        elif pid is None:
            raise TypeError('The pid argument is required.')
        return cls._instance[pid]

    def __init__(self, **kwargs):
        self.os = platform.platform()
        self.pid = os.getpid()
        self.pstat = psutil.Process(self.pid)
        self.log = kwargs.get('log')
        self.state = kwargs.get('state')

    @property
    def cpu_stat(self):
        """获取CPU信息
        """
        return self.pstat.cpu_percent()

    @property
    def mem_stat(self):
        """获取内存信息
        """
        return round(self.pstat.memory_percent, 1)

    @property
    def read_count(self):
        """
        读取的数量
        """
        if hasattr(self, '_read_count') is False:
            self._read_count = 0

        return self._read_count

    @read_count.setter
    def read_count(self, value):
        """设置读取数量
        """
        self._read_count = value

    @property
    def write_count(self):
        """写入的数量
        """
        if hasattr(self, '_write_count') is False:
            self._write_count = 0

        return self._write_count

    @write_count.setter
    def write_count(self, value):
        """设置写入数量
        """
        self._read_count = value

    def log(self, **kwargs):
        """写入日志
        """
        task_id = kwargs.get('task_id')
        if task_id is None:
            raise TypeError('No task id found')
        oid = ObjectId(task_id)
        task = Task.objects.raw({'_id': oid}).first()
        task.process = None

    def destory(self, pid):
        """摧毁一个实例, 防止冲突
        """
        if pid in self._instance:
            self._instance.pop(pid)
