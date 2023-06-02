import openai
import os
from flask import Flask,request
from waitress import serve

app = Flask(__name__)
openai.api_type = "azure"
openai.api_base = os.getenv('ENDPOINT')
openai.api_version = "2023-03-15-preview"
# openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/chatres", methods=["POST"])
def hello_world():
    if(request.method == 'POST'):
        print(request.json)
        return 'very good'
    # response = openai.ChatCompletion.create(
    #     engine="ChatSpeaks",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are an AI assistant that helps people find information."
    #         }
    #     ],
    #     temperature=0.7,
    #     max_tokens=800,
    #     top_p=0.95,
    #     frequency_penalty=0,
    #     presence_penalty=0,
    #     stop=None)
    # print(response)
    return 'good'


if (__name__ == '__main__'):
    # app.run(debug=True, port=8000, host="0.0.0.0")
    print("Waitress Running")
    serve(app, host='0.0.0.0',port=15000)
