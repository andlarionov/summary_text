import streamlit as st
from transformers import pipeline

# Загрузка модели для суммаризации
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

def main():
    st.title("Text Summarization App for Russian-Speaking Users")

    # Ввод текста от пользователя
    user_input = st.text_area("Enter the text for summarization:")

    # Проверка, что пользователь ввел текст
    if st.button("Summarize"):
        if user_input:
            # Получение суммаризации
            summary = generate_summary(user_input)
            st.subheader("Result:")
            st.write(summary)
        else:
            st.warning("Enter the text for summarization.")

def generate_summary(text):
    # Генерация суммаризации
    result = summarizer(text, max_length=230, min_length=30, do_sample=False)
    return result[0]['summary_text']

if __name__ == "__main__":
    main()
