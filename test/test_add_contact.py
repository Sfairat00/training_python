# -*- coding: utf-8 -*-
from model.profile import Profile


def test_add_contact(app):
    old_profiles = app.profile.get_contact_list()
    app.profile.create_contact(Profile(firstname="Saimon", lastname="Ozhereliev", nickname="Sfai", address="Moscow", mobile="916 176-66-66", email="s.ojereliew@yandex.ru",
                                       bday="18", bmonth="April", byear="1986", address2="Moscow city"))
    new_profiles = app.profile.get_contact_list()
    assert len(old_profiles) + 1 == len(new_profiles)


def test_add_empty_contact(app):
    app.profile.create_contact(Profile(firstname="", lastname="", nickname="", address="", mobile="", email="",
                                       bday="", bmonth="", byear="", address2=""))
