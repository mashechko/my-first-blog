from celery import Celery

CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@127.0.0.1:5672/'
CELERY_RESULT_BACKEND = 'rpc://'

app = Celery(
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='Europe/Minsk',
    enable_utc=True,
)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    sender.add_periodic_task(30.0, test.s('world'), expires=10)


@app.task
def test(arg):
    print(arg)


#celery -A tasks worker -l info
#celery -A tasks beat --loglevel=info
#docker-compose up --build