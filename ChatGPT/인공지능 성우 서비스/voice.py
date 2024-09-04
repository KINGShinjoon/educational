import os
import streamlit as st
from openai import OpenAI
import openai

client = OpenAI(
    api_key="sk-"
)

st.title("OpenAI's Text-to-Audio Response")

# 달리가 생성한 이미지를 사용. prompt: 귀여운 인공지능 성우 로봇 그려줘
st.image("https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EC%84%B1%EC%9A%B0.jpg", width=200)

# 인공지능 성우 선택 박스를 생성.
# 공식 문서 참고: https://platform.openai.com/docs/guides/text-to-speech
options = ['alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer']
selected_option = st.selectbox("성우를 선택하세요:", options)

# 인공지능 성우에게 프롬프트 전달
default_text = '오늘은 생활의 꿀팁을 알아보겠습니다.'
user_prompt = st.text_area("인공지능 성우가 읽을 스크립트를 입력해주세요.", value=default_text, height=200)

# Generate Audio 버튼을 클릭하면 True가 되면서 if문 실행.
if st.button("Generate Audio"):

    # 텍스트로부터 음성을 생성.
    audio_response = client.audio.speech.create(
        model="tts-1",
        voice=selected_option,
        input=user_prompt,
    )

    # 음성을 mp3 파일로 저장. 코드가 있는 경로에 파일이 생성된다.
    audio_content = audio_response.content

    with open("temp_audio.mp3", "wb") as audio_file:
        audio_file.write(audio_content)

    # mp3 파일을 재생.
    st.audio("temp_audio.mp3", format="audio/mp3")