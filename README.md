# Telegram Task Manager Bot

A modular Telegram task manager bot built with Python.

## Features

- Add tasks
- List tasks
- Remove tasks
- User-specific task storage
- JSON database

## Commands

- `/start` - Start the bot
- `/add <task>` - Add a task
- `/list` - Show tasks
- `/remove <id>` - Remove a task by task ID

## Project Structure

```text
Task_Bot/
├── main.py
├── database.py
└── commands/
    ├── start.py
    ├── add.py
    ├── list.py
    └── remove.py
```

## Installation

Install requirements:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the bot, create a file named `config.py` in the project root.

Add your Telegram bot token:

```python
TOKEN = "your_bot_token_here"
```

## Run the bot

You can run the bot with this command:

```bash
python main.py
```
