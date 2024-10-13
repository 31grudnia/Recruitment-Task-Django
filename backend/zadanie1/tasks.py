from celery import shared_task

from .utils import shuffle_word


@shared_task
def shuffle_text(contents):
    words = contents.split()
    shuffled_words = [shuffle_word(word) for word in words]
    return ' '.join(shuffled_words)