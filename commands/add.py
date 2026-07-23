from database import load_tasks, save_tasks


def register(bot):
    @bot.message_handler(commands=['add'])
    def add_command(message):
        message_text = message.text
        task = message_text.removeprefix("/add").strip()  # Extract the task after the command

        if task: # Save the task to the database
            loaded_tasks = load_tasks()
            task_id_list = []
#----------------------------------------------------------------------------#
            for item in loaded_tasks:                                        
                if item["user_id"] == message.chat.id: 
                    task_id_list.append(item["task_id"])
            task_id_gen = max(task_id_list, default=0) + 1
            new_task_list = [
                {
                    "task_name": task,
                    "user_id": message.chat.id,
                    "task_id": task_id_gen
                }
            ]
# Task id generation logic: It find the maximum task_id for the user and increments it by 1 to generate a new unique task_id for the new task. If the user has no existing tasks, it defaults to 0 and starts with task_id 1.
#----------------------------------------------------------------------------#
            save_tasks(loaded_tasks + new_task_list)
            bot.send_message(message.chat.id, f"Task added: {task}")

        else: # Send message if no task is provided
            bot.send_message(message.chat.id, "Please enter a task. Usage: /add <task>")
            return
        