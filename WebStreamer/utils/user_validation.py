def user_validation(allowed_users, user_id, user_username):
    return allowed_users and not ((str(user_id) in allowed_users) or (user_username in allowed_users))

def error_message_user_without_permission():
    return "You are not in the allowed list of users who can use me. Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info."