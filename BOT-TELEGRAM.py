from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Темы и их описания с примерами кода и изображениями
topics = {
    'Переменные типы данных': {
        'text': '''Переменные в Python используются для хранения данных. Python поддерживает несколько типов данных: строки (str), числа (int, float), списки (list), словарь (dict) и другие.''',
        'image': 'variables_image.png',  # Укажите путь к изображению
        'subtopics': ['Типы данных', 'Создание переменных']
    },
    'Условные операторы': {
        'text': '''С помощью условных операторов выполняются действия на основе условий. Это позволяет управлять потоком программы.''',
        'image': 'conditional_image.png',  # Укажите путь к изображению
        'subtopics': ['if', 'if-else', 'if-elif-else']
    },
    'Циклы': {
        'text': '''Циклы используются для повторения блоков кода. Есть два основных типа циклов: for и while. Циклы позволяют выполнять одно и то же действие несколько раз, что упрощает написание кода.''',
        'image': 'loops_image.png',  # Укажите путь к изображению
        'subtopics': ['Цикл for', 'Цикл while']
    },
    'Функции': {
        'text': '''Встроенные функции Python используются для решения различных задач. Примеры некоторых из них: str.lower() – преобразует все символы в строке в верхний или нижний регистр соответственно.''',
        'image': 'functions_image.png',  # Укажите путь к изображению
        'subtopics': ['Определение функции', 'Вызов функции']
    }
}

# Главное меню с категориями
main_menu = [['Переменные типы данных', 'Условные операторы'],
             ['Циклы', 'Функции']]


# Функция для отображения главного меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    await update.message.reply_text("Выберите категорию:", reply_markup=reply_markup)


# Функция для обработки выбора категорий
async def handle_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    category = update.message.text
    if category in topics:
        subtopics = topics[category]['subtopics']
        reply_markup = ReplyKeyboardMarkup([[subtopic] for subtopic in subtopics], resize_keyboard=True)
        await update.message.reply_text("Выберите подкатегорию:", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Пожалуйста, выберите категорию из меню.")


# Функция для обработки выбора подкатегорий
async def handle_subtopic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    subtopic = update.message.text
    for category, details in topics.items():
        if subtopic in details['subtopics']:
            await update.message.reply_text(details['text'], parse_mode='Markdown')
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(details['image'], 'rb'))
            return
    await update.message.reply_text("Пожалуйста, выберите подкатегорию из меню.")


if __name__ == '__main__':
    app = ApplicationBuilder().token('7772637398:AAEEEAOSvZzq1uAGqEolfC8CVc8CHQynAKI').build()  # Вставьте ваш токен
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_category))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_subtopic))

    app.run_polling()