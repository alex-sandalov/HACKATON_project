from django.core.mail import send_mail
from .models import Order
from celery import shared_task
from HACKATON_project.celery import app


@shared_task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    print("HELLO")
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                Your order id is {}.'.format(order.first_name,
                                             order.id)
    send_mail(subject, message, 'admin@mail.ru', [order.email])

    #return mail_sent
