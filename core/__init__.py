# -*- coding: utf-8 -*-
"""
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大愿地藏菩萨摩诃萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨
南无大方广佛华严经 华严海会佛菩萨

lazuli控件的核心模块

分为以下三个模块：
①. 读取
②. 整合
③. 写入

   - 此处是其核心Engine模块
      * 支持并发的任务(TaskManager)
      * 读取数据库时采用多线程读取(Reader)
      * 写入数据库时采用多线程写入(Writer)
      * 中间处理模块(Processer)
"""
