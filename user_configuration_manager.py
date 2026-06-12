test_settings = {"theme": "space", "language" : "english", "notifications" : "enabled"}

def add_setting(settings, kv):
    key, value = kv[0].lower(), kv[1].lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, kv):
    key, value = kv[0].lower(), kv[1].lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += key[0].upper() + key[1:] + ": " + value + "\n"
    return result

print(add_setting({'theme': 'light'}, ('THEME', 'dark')))

print(add_setting({'theme': 'light'}, ('volume', 'high')))

print(update_setting({'theme': 'light'}, ('theme', 'dark')))

print(update_setting({'theme': 'light'}, ('volume', 'high')))

print(delete_setting({'theme': 'light'}, 'theme'))

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))

