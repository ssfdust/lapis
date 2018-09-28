# -*- coding: utf-8 -*-
"""
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨

lazuli控件的celery模块
    * celery的声明
"""
from celery import Celery
import os
import subprocess
import json

# 获取配置项目
config_file = '/etc/lazuli/config.json'
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
        backend_url = config.get('backend', 'redis://localhost')
        broker_url = config.get('broker', 'amqp://ssfdust:a136901@localhost:5672/ssfdust')
        schedule_db = config.get('schedule_db', 'lazuli')
        mongo_uri = config.get('mongo_uri', "mongodb://localhost")
else:
    backend_url = os.getenv('LAZULI_REDIS', 'redis://localhost')
    broker_url = os.getenv('LAZULI_RMQ', 'amqp://ssfdust:a136901@localhost:5672/ssfdust')
    schedule_db = os.getenv('LAZULI_DB', 'lazuli')
    mongo_uri = os.getenv('LAZULI_MONGO', "mongodb://localhost")

app = Celery('tasks', backend=backend_url, broker=broker_url,
             CELERY_MONGODB_SCHEDULER_DB = schedule_db,
             CELERY_MONGODB_SCHEDULER_COLLECTION = "schedules",
             CELERY_MONGODB_SCHEDULER_URL = mongo_uri)

def start_celery(app=None):
    """开启celery进程
       代码来源:
       https://stackoverflow.com/questions/23389104
       /how-to-start-a-celery-worker-from-a-script-module-main
    """
    argv = [
        'worker',
        '-A'
        'lapis.core.tasks',
        '--loglevel=INFO'
    ]
    if app is not None:
        app.worker_main(argv)

def start_celerybeat(app=None):
    """开启celerybeat mongodb进程
    """
    argv = [
        '/usr/bin/celery', 
        'beat',
        '-S',
        'celerybeatmongo.schedulers.MongoScheduler',
        '-A',
        'lapis.core.tasks',
        '--loglevel=INFO'
    ]
    if app is not None:
        process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return process
