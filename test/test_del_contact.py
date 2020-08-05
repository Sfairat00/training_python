

def test_delete_first_contact(app):
    old_profiles = app.profile.get_contact_list()
    app.profile.delete_first_contact()
    new_profiles = app.profile.get_contact_list()
    assert len(old_profiles) - 1 == len(new_profiles)

