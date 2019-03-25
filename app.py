# encoding: utf-8
from flask import Flask, request, abort
import apple_crawd as ac
import immidiate_weather as im
import time
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    TemplateSendMessage,ButtonsTemplate,
    PostbackAction, MessageAction,
    URIAction, DatetimePickerAction,
    ConfirmTemplate, CarouselTemplate, CarouselColumn,
    ImageCarouselTemplate, ImageCarouselColumn
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
    ac.app_social_fun()
    if msg == "新聞類別":
        buttletemplate(profile.user_id)
        buttletemplate2(profile.user_id)
    elif msg == "氣象":
        buttletemplate_weather_north(profile.user_id)
        buttletemplate_weather_middle(profile.user_id)
        buttletemplate_weather_south(profile.user_id)
        buttletemplate_weather_south2(profile.user_id)
        buttletemplate_weather_east(profile.user_id)
    elif msg == "社會":
        social_title = ac.local_title_list
        social_href = ac.local_href_list
        for i in range(len(social_title)):
            single_push(profile.user_id,social_title[i])
            single_push(profile.user_id,social_href[i])
        social_title = []
        social_href = []
    elif msg == "政治":
        political_title = ac.local_political_title_list
        political_href = ac.local_political_href_list
        for i in range(len(political_title)):
            single_push(profile.user_id,political_title[i])
            single_push(profile.user_id,political_href[i])
        political_title = []
        political_href = []
    elif msg == "國際":
        national_title = ac.local_national_title_list
        national_href = ac.local_national_href_list
        for i in range(len(national_title)):
            single_push(profile.user_id,national_title[i])
            single_push(profile.user_id,national_href[i])
        national_title = []
        national_href = []
    elif msg == "娛樂":
        entertainment_title = ac.local_entertainment_title_list
        entertainment_href = ac.local_entertainment_href_list
        for i in range(len(entertainment_title)):
            single_push(profile.user_id,entertainment_title[i])
            single_push(profile.user_id,entertainment_href[i])
        entertainment_title = []
        entertainment_href = []
    elif msg == "生活":
        life_title = ac.local_life_title_list
        life_href = ac.local_life_href_list
        for i in range(len(life_title)):
            single_push(profile.user_id,life_title[i])
            single_push(profile.user_id,life_href[i])
        life_title = []
        life_href = []
    elif msg == "體育":
        sports_title = ac.local_sports_title_list
        sports_href = ac.local_sports_href_list
        for i in range(len(sports_title)):
            single_push(profile.user_id,sports_title[i])
            single_push(profile.user_id,sports_href[i])
        sports_title = []
        sports_href = []
    elif (msg == "基隆市" or msg == "新北市" or msg == "臺北市" or msg == "桃園市" or msg == "臺中市" or msg == "新竹市" or msg == "新竹縣" or msg == "苗栗縣" or msg == "嘉義市" or msg == "嘉義縣" or msg == "雲林縣" or msg == "南投縣"
    or msg == "臺南市" or msg == "高雄縣" or msg == "屏東縣" or msg == "彰化縣" or msg == "宜蘭縣" or msg == "花蓮縣" or msg == "臺東縣"):
        im.city(msg)
        time.sleep(2)
        single_push(profile.user_id,im.title)
        single_push(profile.user_id,"時間 : "+im.weather_time+"\n"+"溫度 : "+im.weather_temperature+"\n"+"天氣狀況 : "+im.weather_situation+"\n"+"舒適度 : "+im.weather_feel+"\n"+"降雨機率 (%)   : "+im.weather_rain)
        single_push(profile.user_id,"時間 : "+im.weather_tonight_time+"\n"+"溫度 : "+im.weather_tonight_temperature+"\n"+"天氣狀況 : "+im.weather_tonight_situation+"\n"+"舒適度 : "+im.weather_tonight_feel+"\n"+"降雨機率 (%)   : "+im.weather_tonight_rain)
        single_push(profile.user_id,"時間 : "+im.weather_tomorrow_time+"\n"+"溫度 : "+im.weather_tomorrow_temperature+"\n"+"天氣狀況 : "+im.weather_tomorrow_situation+"\n"+"舒適度 : "+im.weather_tomorrow_feel+"\n"+"降雨機率 (%)   : "+im.weather_tomorrow_rain)
    else:
        single_push(profile.user_id,"暫時無這類別資訊")
    

        
    
    # single_push(profile.user_id, "test")

   

    # 針對使用者各種訊息的回覆 End =========

# ================= 機器人區塊 End =================

def single_push(id, msg):

    line_bot_api.push_message(id, TextSendMessage(text=msg))
def buttletemplate(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            MessageAction(
                label='社會',
                text='社會'
            ),
            MessageAction(
                label='政治',
                text='政治'
            ),
            MessageAction(
                label='國際',
                text='國際'
            ),
            MessageAction(
                label='娛樂',
                text='娛樂'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)
def buttletemplate2(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='Menu',
        text='Please select',
        actions=[
            MessageAction(
                label='生活',
                text='生活'
            ),
            MessageAction(
                label='體育',
                text='體育'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)

def buttletemplate_weather_north(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='北部縣市',
        text='Please select',
        actions=[
            MessageAction(
                label='臺北市',
                text='臺北市'
            ),
            MessageAction(
                label='新北市',
                text='新北市'
            ),
            MessageAction(
                label='桃園市',
                text='桃園市'
            ),
            MessageAction(
                label='基隆市',
                text='基隆市'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)
def buttletemplate_weather_middle(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='中北部縣市',
        text='Please select',
        actions=[
            MessageAction(
                label='臺中市',
                text='臺中市'
            ),
            MessageAction(
                label='新竹市',
                text='新竹市'
            ),
            MessageAction(
                label='新竹縣',
                text='新竹縣'
            ),
            MessageAction(
                label='苗栗縣',
                text='苗栗縣'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)
def buttletemplate_weather_south(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='中部縣市',
        text='Please select',
        actions=[
            MessageAction(
                label='雲林縣',
                text='雲林縣'
            ),
            MessageAction(
                label='嘉義市',
                text='嘉義市'
            ),
            MessageAction(
                label='南投縣',
                text='南投縣'
            ),
            MessageAction(
                label='彰化縣',
                text='彰化縣'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)
def buttletemplate_weather_south2(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='南部縣市',
        text='Please select',
        actions=[
            MessageAction(
                label='臺南市',
                text='臺南市'
            ),
            MessageAction(
                label='高雄市',
                text='高雄市'
            ),
            MessageAction(
                label='屏東縣',
                text='屏東縣'
            ),
            MessageAction(
                label='嘉義縣',
                text='嘉義縣'
            ),
        ]
    )
    )
    line_bot_api.push_message(id,message)
def buttletemplate_weather_east(id):
    message = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        # thumbnail_image_url='https://example.com/image.jpg',
        title='東部縣市',
        text='Please select',
        actions=[
            MessageAction(
                label='宜蘭縣',
                text='宜蘭縣'
            ),
            MessageAction(
                label='花蓮縣',
                text='花蓮縣'
            ),
            MessageAction(
                label='臺東縣',
                text='臺東縣'
            )
        ]
    )
    )
    line_bot_api.push_message(id,message)

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
