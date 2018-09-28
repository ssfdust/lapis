from lapis.core.manager.celery_app import app
from lapis.log.record import LapisLog

@app.task
def test(pid):
    lalog = LapisLog(pid=pid)
    lalog.read_count += 1000
    print(lalog.read_count)
    print(111111111)

@app.task
def test2(pid):
    print(2222222222)
