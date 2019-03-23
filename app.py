# encoding: utf-8
from flask import Flask, request, abort
import apple_crawd
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

handler = WebhookHandler('f8777392a7e733048768d7bdf7f132e9') 
line_bot_api = LineBotApi('isN4uAsP6qwM+aOiiBfyZCE2HfJZ2OGAKsvAjiDGtNGXwqwO/QrW0hoBPE+D9uh4j0e5H/6Oqk8hY1T+7BaZ7l71QyPquv7kSBDVaSWh9XBjgnI8RVRwnmyvHOPFYKH9t6mvmZG/C3Er3Tj+2/sTkQdB04t89/1O/w1cDnyilFU=') 


@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# ================= 機器人區塊 Start =================
@handler.add(MessageEvent, message=TextMessage)  # default
def handle_text_message(event):                  # default
    msg = event.message.text #message from user
    
    profile = line_bot_api.get_profile(event.source.user_id)
    #跑社會類別
    apple_crawd.app_social_fun()
    

    #跑政治類別
    apple_crawd.app_political_fun()
    

    
    if msg == "社會":
        social_title = apple_crawd.local_title_list
        social_href = apple_crawd.local_href_list
        for i in range(2):
            single_push(profile.user_id,social_title[i])
            single_push(profile.user_id,social_href[i])
    elif msg == "政治":
        social_title = apple_crawd.local_political_title_list
        social_href = apple_crawd.local_political_href_list
        for i in range(2):
            single_push(profile.user_id,social_title[i])
            single_push(profile.user_id,social_href[i])
    else:
        single_push(profile.user_id,"暫時無這類別資訊")
    

        
    
    # single_push(profile.user_id, "test")

   

    # 針對使用者各種訊息的回覆 End =========

# ================= 機器人區塊 End =================

def single_push(id, msg):
    line_bot_api.push_message(id, TextSendMessage(text=msg))

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
