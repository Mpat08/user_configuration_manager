# 🛠️ User Configuration Manager

A Python-based lab project that implements a simple but functional configuration management system. Users can manage personal settings — such as theme, language, and notifications — through a menu-driven interface backed by core CRUD operations.

---

## 📋 Overview

This project was built as part of a Python lab focused on dictionary manipulation, modular function design, and input validation. The program stores user settings in a Python dictionary and provides a clean interface to interact with them.

---

## ✨ Features

- ➕ **Add** new user settings
- ✏️ **Update** existing settings
- 🗑️ **Delete** unwanted settings
- 👁️ **View** all current settings
- 🔒 Input validation to prevent invalid or duplicate entries

---

## 🗂️ Project Structure

```
user-config-manager/
│
├── config_manager.py   # All CRUD functions + test calls
└── README.md           # Project documentation
```

---

## ⚙️ How It Works

Settings are stored as key-value pairs in a Python dictionary. A default test dictionary is included to demonstrate each function:

```python
test_settings = {
    "theme": "space",
    "language": "english",
    "notifications": "enabled"
}
```

Each function accepts the settings dictionary along with the necessary arguments, performs the operation, and returns a descriptive message. All keys and values are automatically normalized to lowercase for consistency.

---

## 🔧 Functions

### `add_setting(settings, kv)`
Adds a new setting. Rejects duplicates.
```python
add_setting({'theme': 'light'}, ('volume', 'high'))
# → "Setting 'volume' added with value 'high' successfully!"

add_setting({'theme': 'light'}, ('THEME', 'dark'))
# → "Setting 'theme' already exists! Cannot add a new setting with this name."
```

### `update_setting(settings, kv)`
Updates an existing setting. Rejects keys that don't exist.
```python
update_setting({'theme': 'light'}, ('theme', 'dark'))
# → "Setting 'theme' updated to 'dark' successfully!"

update_setting({'theme': 'light'}, ('volume', 'high'))
# → "Setting 'volume' does not exist! Cannot update a non-existing setting."
```

### `delete_setting(settings, key)`
Deletes a setting by key.
```python
delete_setting({'theme': 'light'}, 'theme')
# → "Setting 'theme' deleted successfully!"
```

### `view_settings(settings)`
Displays all current settings in a readable format.
```python
view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
# → Current User Settings:
#    Theme: dark
#    Notifications: enabled
#    Volume: high
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Run the Program

```bash
# Clone the repository
git clone https://github.com/your-username/user-config-manager.git

# Navigate into the project folder
cd user-config-manager

# Run the program
python config_manager.py
```

---

## 🧠 Concepts Practiced

| Concept | Description |
|---|---|
| Dictionaries | Storing and manipulating key-value settings |
| Functions | Modular CRUD operations with return messages |
| Input Normalization | `.lower()` ensures case-insensitive keys/values |
| Duplicate Handling | Guards against adding already-existing keys |
| String Formatting | Capitalizing keys for clean display output |

---

## 👤 Author

**Mayur** — Computer Engineering Student at UCF
Feel free to connect or explore more of my projects on [GitHub](https://github.com/Mpat08)

---

## 📄 License

This project was for a Python certification course by FreeCodeCamp.
