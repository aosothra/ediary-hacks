import random

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from datacenter.models import Chastisement, Schoolkid, Mark, Lesson, Commendation


def fix_marks(kid_name: str):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Too many entries for given name. Please specify.')
        return
    except ObjectDoesNotExist:
        print('No kid with the given name. Try other name')
        return
    
    bad_marks = Mark.objects.filter(schoolkid=kid, points__lt=4)
    for mark in bad_marks:
        mark.points=random.randint(4,5)
    Mark.objects.bulk_update(bad_marks, ['points'])


def remove_chastisements(kid_name: str):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Too many entries for given name. Please specify.')
        return
    except ObjectDoesNotExist:
        print('No kid with the given name. Try other name')
        return

    Chastisement.objects.filter(schoolkid=kid).delete()


def create_commendation(kid_name: str, subject_title:str):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Too many entries for given name. Please specify.')
        return
    except ObjectDoesNotExist:
        print('No kid with the given name. Try other name.')
        return

    
    lessons = Lesson.objects.filter(
        year_of_study=kid.year_of_study, 
        group_letter=kid.group_letter,
        subject__title=subject_title
        )
    if not lessons:
        print('No lessons of this type were found. Please verifvy your input.')
        return

    last_lesson = lessons.order_by('date').last()

    commendation_options = [
        'Респект!',
        'Уважаю!',
        'Хвалю!',
        'Восхищаюсь!',
        'Преклоняюсь!',
        'Преисполняюсь!'
    ]

    new_commendation = Commendation.objects.create(
        text=random.choice(commendation_options), 
        created=last_lesson.date, 
        schoolkid=kid, 
        subject=last_lesson.subject, 
        teacher=last_lesson.teacher
        )
