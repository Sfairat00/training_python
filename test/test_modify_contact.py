from model.profile import Profile


def test_modify_contact_firstname(app):
    if app.profile.count() == 0:
        app.profile.create(Profile(firstname="test"))
    old_profiles = app.profile.get_contact_list()
    app.profile.modify_first_contact(Profile(firstname="Sfairat"))
    new_profiles = app.profile.get_contact_list()
    assert len(old_profiles) == len(new_profiles)



def test_modify_contact_nickname(app):
    if app.profile.count() == 0:
        app.profile.create(Profile(firstname="test"))
    old_profiles = app.profile.get_contact_list()
    app.profile.modify_first_contact(Profile(nickname="Sfai"))
    new_profiles = app.profile.get_contact_list()
    assert len(old_profiles) == len(new_profiles)

