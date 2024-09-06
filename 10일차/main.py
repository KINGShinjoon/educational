import base64

from openai import OpenAI
from string import Template
import requests

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")



query = "안녕하세요. 오늘 날짜로 뉴욕행 비행기를 예약할 수 있나요?"


prompt_template = Template("""
입력한 내용: "$query"
""")

def consult(query):
  prompt = prompt_template.substitute(query=query)
  chat_completion = client.chat.completions.create(
      messages=[
          {
            "role": "system",
            "content": "입력한 내용을 한국어로 번역해줘",
          },
          {
              "role": "user",
              "content": prompt,
          }
      ],
      model="ggml-model-q4_k_m",
  )
  return chat_completion.choices[0].message.content


def encode_image_to_base64(image_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(image_url, headers=headers, allow_redirects=True)
    print(f"Status code: {response.status_code}")  # For debugging

    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        raise Exception(f"Failed to fetch image from URL: {image_url}, Status code: {response.status_code}")


def imageAI(image_url):
    base64_image = encode_image_to_base64(image_url)
    payload = {
        "model": "llava-v1.5-7b-q4_0",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What is this image?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    # Sending request to your API
    chat_completion = client.chat.completions.create(
        **payload
    )

    return chat_completion.choices[0].message.content

## test

print(consult(imageAI("https://www.fitpetmall.com/wp-content/uploads/2023/10/230420-0668-1.png")))