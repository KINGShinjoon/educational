from openai import OpenAI
import streamlit as st
import requests
# OpenAI Key 값 셋팅
client = OpenAI(
    api_key = ''
)

# 주어진 이미지 주소로부터 GPT4V의 설명을 얻는 함수.
def describe(image_url):
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": "이 이미지에 대해서 알려줘"},
            {
            "type": "image_url",
            "image_url": {
                "url": image_url,
            },
            },
        ],
        }
    ],
    max_tokens=1024,
    )
    return response.choices[0].message.content

# 웹 사이트 상단에 노출될 웹 사이트 제목.
st.title("AI 도슨트: 이미지를 설명해드려요!")

# st.text_area()는 사용자의 입력을 받는 커다란 텍스트 칸을 만든다. height는 이 텍스트 칸의 높이.
input_url = st.text_area("여기에 이미지 주소를 입력하세요", height=30)

# st.button()을 클릭하는 순간 st.button()의 값은 True가 되면서 if문이 실행된다.
if st.button("해설"):

    # st.text_area()의 값이 존재하면 input_url의 값이 True가 되면서 if문이 실행된다.
    if input_url:
        try:
            # st.image()는 기본적으로 이미지 주소로부터 이미지를 웹 사이트 화면에 생성한다.
            st.image(input_url, width=300)
            
            # describe() 함수는 GPT4V의 출력 결과를 반환한다.
            result = describe(input_url)

            # st.success()는 텍스트를 웹 사이트 화면에 출력하되, 초록색 배경에 출력한다.
            st.success(result)
        except:
            st.error("요청 오류가 발생했습니다!")
    else:
        st.warning("텍스트를 입력하세요!") # 화면 상으로 노란색 배경으로 출력한다.