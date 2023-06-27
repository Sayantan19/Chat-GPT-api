import openai
import os
from flask import Flask,request
from waitress import serve

app = Flask(__name__)
openai.api_type = "azure"
openai.api_base = os.getenv("ENDPOINT")
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")
# openai.api_version = "2022-12-01"


@app.route("/chatres", methods=["POST"])
def hello_world():
    if(request.method == 'POST'):
        print(request.json['message'])
        response = openai.ChatCompletion.create(
            engine="ChatSpeaks",
            messages=[
                {
                    "role": "system",
                    "content": request.json['message']
                }
            ],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
        print(response)
        return response["choices"]
    return "good"


if (__name__ == '__main__'):
    # app.run(debug=True, port=15000, host="0.0.0.0")
    print("Waitress Running")
    # serve(app, host='0.0.0.0',port=15000)
