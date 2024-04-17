def update_user_information(instance, user_data):
    user = instance.user
    user.email = user_data.get('email', user.email)
    user.first_name = user_data.get('first_name', user.first_name)
    user.last_name = user_data.get('last_name', user.last_name)
    user.is_staff = user_data.get('is_staff', user.is_staff)
    user.is_active = user_data.get('is_active', user.is_active)
    user.is_superuser = user_data.get('is_superuser', user.is_superuser)
    return user


def create_user_information(user_data):
    if not user_data.get('email'):
        raise ValueError('Not email provided')
    user = User.objects.create_user(user_json.pop('email'))
    user.username = user_json.pop('username')
    user.last_name = user_json.pop('last_name')
    user.first_name = user_json.pop('first_name')
    return user
