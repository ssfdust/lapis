# -*- coding: utf-8 -*-
"""
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨

ORM模块(mongodb orm):
"""
from mongoengine import (DynamicDocument,
                         BooleanField,
                         DictField,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         ListField,
                         DateTimeField,
                         StringField,
                         IntField,
                         FloatField
                         )

class Log(EmbeddedDocument):
    create_time = DateTimeField()
    level = IntField()
    log = StringField()
    cpu_load = FloatField()
    mem_load = FloatField()
    io_load = FloatField()
    chunk_count = IntField()

class Process(EmbeddedDocument):
    logs = ListField(EmbeddedDocumentField(Log))
    request_ip = StringField()
    create_time = DateTimeField()
    end_time = DateTimeField()
    all_count = IntField()
    processed_cnt = IntField()
    celery_id = StringField()

class Task(DynamicDocument):
    task_name = StringField()
    create_time = DateTimeField()
    ended_time = ListField()
    active = BooleanField()
    rule = StringField()
    configuration = DictField()
    processes = ListField(EmbeddedDocumentField(Process))
