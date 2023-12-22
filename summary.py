import streamlit as st
from transformers import pipeline

# Загрузка модели для суммаризации
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

def main():
    st.title("Приложение для суммаризации текста")

    # Ввод текста от пользователя
    user_input = st.text_area("Введите текст для суммаризации:")

    # Проверка, что пользователь ввел текст
    if st.button("Суммаризировать"):
        if user_input:
            # Получение суммаризации
            summary = generate_summary(user_input)
            st.subheader("Результат:")
            st.write(summary)
        else:
            st.warning("Введите текст для суммаризации.")

def generate_summary(text):
    # Генерация суммаризации
    result = summarizer(text, max_length=230, min_length=30, do_sample=False)
    return result[0]['summary_text']

if __name__ == "__main__":
    main()
