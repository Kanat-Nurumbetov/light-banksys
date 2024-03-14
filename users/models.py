from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    id = models.UUIDField
    password = models.CharField(max_length = 100)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    deposit = models.ForeignKey() #добавить связь с моделью депозиты
    create_date = models.DateField

    def registration(self):                                 #Проверить праввильность
        new_first_name = input("Введите логин: ")           #\\\\\\\\\\\\\\\\\\\\\\\
        new_password = input("Введите пароль: ")            #\\\\\\\\\\\\\\\\\\\\\\\
        if len(new_password) < 3:                           #\\\\\\\\\\\\\\\\\\\\\\\
            logging.error("пароль меньше 3 символов")       #\\\\\\\\\\\\\\\\\\\\\\\
            print("пароль должен быть мин 3 символа")       #\\\\\\\\\\\\\\\\\\\\\\\
        else:                                               #\\\\\\\\\\\\\\\\\\\\\\\
            print("Вы успешно зарегистрировались!")         #\\\\\\\\\\\\\\\\\\\\\\\
            # # new_user = {                                    #\\\\\\\\\\\\\\\\\\\\\\\
            # # first_name = new_first_name.strip(),            #\\\\\\\\\\\\\\\\\\\\\\\
            # password = new_password,                        #\\\\\\\\\\\\\\\\\\\\\\\
            # deposit = 0}                                    #\\\\\\\\\\\\\\\\\\\\\\\
