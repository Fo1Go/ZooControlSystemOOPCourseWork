def update_user_information(instance, user_data):
    user = instance.user
    user.email = user_data.get('email', user.email)
    user.first_name = user_data.get('first_name', user.first_name)
    user.last_name = user_data.get('last_name', user.last_name)
    user.is_staff = user_data.get('is_staff', user.is_staff)
    user.is_active = user_data.get('is_active', user.is_active)
    user.is_superuser = user_data.get('is_superuser', user.is_superuser)
    return user
