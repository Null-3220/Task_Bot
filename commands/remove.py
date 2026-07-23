from database import load_tasks, save_tasks

def register(bot):
    @bot.message_handler(commands=['remove'])
    def remove_command(message): # Remove a task for the user
        try:
            task_id = int(message.text.removeprefix('/remove ').strip())

        except ValueError: # Ceck if the task_id is not a valid integer
                bot.send_message(message.chat.id, "Please provide a valid task ID. Usage: /remove <task_id>")
                return
        
        loaded_tasks = load_tasks()
        task_to_remove = [task for task in loaded_tasks if task["task_id"] == task_id and task["user_id"] == message.from_user.id]

        if not task_to_remove: # CHeck if the task exists and belongs to the user
                bot.send_message(message.chat.id, "Task not found or you don't have permission to remove it.")
                return
        
        loaded_tasks.remove(task_to_remove[0])

        for item in loaded_tasks: # Renumber the task IDs after deletion
              if item["user_id"] == message.from_user.id and item["task_id"] > task_id:
                    item["task_id"] -= 1

        save_tasks(loaded_tasks)
        bot.send_message(message.chat.id, f"Task removed successfully!")
        