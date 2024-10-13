from celery import shared_task

from .utils import extract_pesel_data, check_control_number


@shared_task
def check_pesel_data(pesel):
    return extract_pesel_data(pesel)

@shared_task
def check_pesel_control_number(pesel):
    return check_control_number(pesel)