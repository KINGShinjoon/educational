import streamlit as st
import io
import base64
from openai import OpenAI
from PIL import Image

client = OpenAI(
    api_key = '' # 여러분들의 OpenAI API Key 값
)

def get_image(prompt):
    response = get_image_info(prompt) # DALLE로부터 Base64 형태의 이미지를 얻음.
    image_data = base64.b64decode(response) # Base64로 쓰여진 데이터를 이미지 형태로 변환
    image = Image.open(io.BytesIO(image_data)) # '파일처럼' 만들어진 이미지 데이터를 컴퓨터에서 볼 수 있도록 Open
    return image

# DALLE가 이미지를 반환하는 함수.
def get_image_info(prompt): 
    response = client.images.generate(
    model="dall-e-3", # 모델은 DALLE 버전3 (현 최신 버전)
    prompt=prompt, # 사용자의 프롬프트
    size="1024x1024", # 이미지의 크기
    quality="standard", # 이미지 퀄리티는 '표준'
    response_format='b64_json', # 이때 Base64 형태의 이미지를 전달한다.
    n=1,
    )
    return response.data[0].b64_json

st.title("그림 그리는 AI 화가 서비스 👨‍🎨")

st.image('https://wikidocs.net/images/page/215361/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%ED%99%94%EA%B0%80.png', width=200)

st.text("🎨 Tell me the picture you want. I'll draw it for you!")

input_text = st.text_area("원하는 이미지의 설명을 영어로 적어보세요.", height=200)

# Painting이라는 버튼을 클릭하면 True
if st.button("Painting"):

    # 이미지 프롬프트가 작성된 경우 True
    if input_text:
        try:
            # 사용자의 입력으로부터 이미지를 전달받는다.
            dalle_image = get_image(input_text)

            # st.image()를 통해 이미지를 시각화.
            st.image(dalle_image)
        except:
            st.error("요청 오류가 발생했습니다")
    # 만약 이미지 프롬프트가 작성되지 않았다면
    else:
        st.warning("텍스트를 입력하세요")