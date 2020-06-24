# -*- coding: utf-8 -*-
import pytest
from model.profile import Profile
from fixture.application_contact import Application_contact


@pytest.fixture()
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session_contact.login(username="admin", password="secret")
    app.profile.create(Profile(firstname="Saimon", lastname="Ozhereliev", nickname="Sfai", address="Moscow", mobile="916 176-66-66", email="s.ojereliew@yandex.ru",
                               bday="18", bmonth="April", byear="1986", address2="Moscow city"))
    app.session_contact.logout()

