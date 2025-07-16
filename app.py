# OpenAI API Chat Uygulaması

#Bu proje, OpenAI'nin GPT modellerini kullanarak basit bir soru-cevap sistemi oluşturur.
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

my_key = os.getenv("openai_apikey")
#print(my_key)

client = OpenAI(api_key=my_key)


#ai response ile gelecek yaniti yakalamaya calisiyorum
AI_Response = client.chat.completions.create(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=256,
    messages=[
        {"role": "system", "content":"Sen yardımsever bir asistansın."},
        {"role": "user", "content": "Mevsimler neden oluşur? Dünya kendi etrafında döndüğü için mi?"}
    ]
)

print(AI_Response.choices[0].message.content)