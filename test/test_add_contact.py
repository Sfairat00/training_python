# -*- coding: utf-8 -*-
from model.profile import Profile


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.profile.create_contact(Profile(firstname="Saimon", lastname="Ozhereliev", nickname="Sfai", address="Moscow", mobile="916 176-66-66", email="s.ojereliew@yandex.ru",
                                       bday="18", bmonth="April", byear="1986", address2="Moscow city"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.profile.create_contact(Profile(firstname="", lastname="", nickname="", address="", mobile="", email="",
                                       bday="", bmonth="", byear="", address2=""))
    app.session.logout()
