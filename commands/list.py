from database import load_tasks

def register(bot):
    @bot.message_handler(commands=['list'])
    def list_command(message): # Send the list of tasks for the user
        loaded_tasks = load_tasks()
        user_tasks = [task for task in loaded_tasks if task["user_id"] == message.chat.id]

        if user_tasks:
            task_list = "\n".join([f"{task['task_id']}. {task['task_name']}" for task in user_tasks])
            bot.send_message(message.chat.id, f"Your tasks:\n{task_list}")

        else: # Send a message if the user has no tasks
            bot.send_message(message.chat.id, "You have no tasks. Use /add <task> to add a new task.")