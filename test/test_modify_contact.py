from model.profile import Profile


def test_modify_contact_firstname(app):
    app.profile.modify_first_contact(Profile(firstname="Sfairat"))


#def test_modify_contact_nickname(app):
#    app.profile.modify_first_contact(Profile(nickname="Sfai"))
