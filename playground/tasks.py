from time import sleep
from celery import shared_task


# task/function to receive a message from a view and run in the background
@shared_task
def notify_customers(message):
    print('sending 10k emails')
    print(message)
    sleep(10)
    print('Emails were sent')