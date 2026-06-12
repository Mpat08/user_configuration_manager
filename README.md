# User Configuration Manager

A Python utility that lets users manage personal application settings — such as theme, language, and notifications — through a set of clean, modular functions. Built to practice core dictionary operations, input normalization, and defensive programming in Python.

---

## Installation

No external dependencies required — just Python 3.x.

```bash
# Clone the repository
git clone https://github.com/your-username/user-config-manager.git

# Navigate into the project folder
cd user-config-manager
```

---

## Usage

Run the script directly with Python:

```bash
python config_manager.py
```

Each function takes a settings dictionary and the necessary arguments, performs the operation, and returns a status message.

| Function | Parameters | Description |
|---|---|---|
| `add_setting(settings, kv)` | dict, (key, value) tuple | Adds a new setting if it doesn't already exist |
| `update_setting(settings, kv)` | dict, (key, value) tuple | Updates a setting if it exists |
| `delete_setting(settings, key)` | dict, key string | Deletes a setting by key |
| `view_settings(settings)` | dict | Returns all current settings as a formatted string |

---

## Examples

**Adding a setting**

<img width="400" height="300" alt="Picture1" src="https://github.com/user-attachments/assets/e6cbaa6e-c5ab-483b-84af-9fb03577b0e6" />


**Updating a setting**

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/197204e9-e9a5-45a0-934c-ff4be228f932" />


**Deleting a setting**

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/9af492e1-78e6-409f-91df-e041a8958d0a" />


**Viewing all settings**

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/04647e98-85e5-44e4-9ce3-9951abd235d8" />


---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, copy, modify, and distribute this project as long as the original license and copyright notice are included.


---

## Contributors

Mayur Patel — Computer Engineering Major at the University of Central Florida
