import re

def split_text(text):
    # Регулярное выражение для разделения по точке, восклицательному и вопросительному знакам
    pattern = re.compile(r'(?<=[\n.!?])')

    # Разделение текста на предложения
    sentences = pattern.split(text)

    # Переменная для хранения текущего чанка
    current_chunk = ''

    # Список для хранения чанков
    chunks = []

    for sentence in sentences:
        # Проверяем, не превышает ли текущий чанк 2000 символов
        if len(current_chunk) + len(sentence) < 2000:
            current_chunk += sentence
        else:
            # Добавляем текущий чанк в список
            chunks.append(current_chunk.strip())
            # Начинаем новый чанк с текущим предложением
            current_chunk = sentence

    # Добавляем последний чанк, если он не пустой
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
