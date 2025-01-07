import streamlit as st
from langchain_community.chat_models import ChatOpenAI

# Streamlit 애플리케이션 설정
st.title('텍스트 요약기 - LangChain & GPT-4o-mini')

# OpenAI API Key 입력 (사이드바 사용)
st.sidebar.header("설정")
api_key = st.sidebar.text_input("OpenAI API Key를 입력하세요:", type="password")

# 사용자 입력 텍스트
user_text = st.text_area("요약할 텍스트를 입력하세요:")

# 요약 버튼
if st.button('요약 생성'):
    if not api_key:
        st.error("API Key를 입력해주세요!")
    elif not user_text:
        st.error("요약할 텍스트를 입력해주세요!")
    else:
        # LangChain 및 OpenAI 초기화
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=api_key)
        summary = llm.invoke(f"요약을 생성해줘: {user_text}")

        # 결과 출력
        st.subheader("요약 결과")
        st.write(summary.content)

st.sidebar.markdown("이 앱은 LangChain과 OpenAI GPT-4o-mini를 사용하여 텍스트를 요약합니다.")
