def register(bot):
    @bot.message_handler(commands=['start'])
    def start_command(message):
        bot.send_message(message.chat.id, "Welcome to the task manager bot!")
    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(message.chat.id, "Available commands:\n/start - Start the bot\n/help - Show this help message\n/add - Add a new task\n/remove - Remove a task\n/list - List all tasks") 