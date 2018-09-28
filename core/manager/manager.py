# -*- coding: utf-8 -*-
"""
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨

任务管理模块(Manager):
    * 通过celery来管理任务
    * 自定义任务运行时间
    * 启动以及关闭任务
    * 任务存储通过mongodb
"""

from __future__ import absolute_import, unicode_literals
from celery_app import app, start_celery
from lapis.log.models import Task, Process, Log
from lapis.core.tasks import test
from multiprocessing import Process as SubProcess
from datetime import datetime, timedelta
from celerybeatmongo.models import PeriodicTask

import os

class TaskManager(object):
    # 单例变量
    _instance = None

    def __new__(cls, *args, **kwargs):
        """单例模式
           一次只允许一个TaskManager实例存在
        """
        if not cls._instance:
            cls._instance = super(TaskManager,
                                  cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, redis_url):
        """初始化内容
        """
        self.redis_url = redis_url

        # 启动celery
        self.fork_celery()

    def fork_celery(self):
        """启动celery
        """
        self.process = SubProcess(target=start_celery, args=(app,))
        self.process.start()

    def add_task(self, task_name, configuration, rule=None, **kwargs):
        """新增任务
        """
        task = Task(task_name=task_name,
                    create_time=datetime.now(),
                    configuration=configuration,
                    rule=rule,
                    active=False)
        task.save()

    def list_tasks(self, page=None, perpage=None,
                   oid=None):
        """查询全部任务
        """
        if oid is not None:
            task = Task.objects(id=oid).first()
            return task
        elif page is not None and perpage is not None:
            task = Task.objects    

    def start_task(self, oid):
        """启动任务
        """
        task = Task.objects(_id=oid).first()
        log = Log(create_time=datetime.now(),
                  all_count=0,)
        run_task = test.delay()
        process = Process(all_count=0,
                          processed_cnt=0,
                          celery_id=run_task.id)
        task.processes.append(process)

    def stop_celery(self):
        """关闭celery
        """
        if self.process is None:
            return False
        else:
            self.process.terminate()
            self.process = None
            return True
