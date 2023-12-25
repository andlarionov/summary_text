import os
from transformers import pipeline
import summary_t as sum_t

def test_generate_summary():
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")

    # Путь к файлу с тестовым текстом
    t_test_path = os.path.join(os.path.dirname(__file__), 't_test.txt')

    try:
        # Открываем файл и читаем его содержимое
        with open(t_test_path, 'r', encoding='utf-8') as file:
            t_test = file.read()

        # Ввод тестового текста
        test_text = t_test

        # Получение суммаризации с использованием вашей функции
        summary = sum_t.generate_summary(test_text)

        # Проверка, что результат не является пустой строкой
        assert summary.strip() != ""

    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        print(f"Файл '{t_test_path}' не найден.")
