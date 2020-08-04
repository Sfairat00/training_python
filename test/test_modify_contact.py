from model.profile import Profile


def test_modify_contact_firstname(app):
    if app.profile.count() == 0:
        app.profile.create(Profile(firstname="test"))
    app.profile.modify_first_contact(Profile(firstname="Sfairat"))


def test_modify_contact_nickname(app):
    if app.profile.count() == 0:
        app.profile.create(Profile(firstname="test"))
    app.profile.modify_first_contact(Profile(nickname="Sfai"))
