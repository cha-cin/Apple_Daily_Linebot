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
    ImageCarouselTemplate, ImageCarouselColumn,PostbackTemplateAction,
    MessageTemplateAction,URITemplateAction,MessageImagemapAction,ImagemapSendMessage,
    BaseSize,ImagemapArea
)

handler = WebhookHandler('f8777392a7e733048768d7bdf7f132e9') 
line_bot_api = LineBotApi('isN4uAsP6qwM+aOiiBfyZCE2HfJZ2OGAKsvAjiDGtNGXwqwO/QrW0hoBPE+D9uh4j0e5H/6Oqk8hY1T+7BaZ7l71QyPquv7kSBDVaSWh9XBjgnI8RVRwnmyvHOPFYKH9t6mvmZG/C3Er3Tj+2/sTkQdB04t89/1O/w1cDnyilFU=') 

# def getTaipeiCarouselTemplate(Taipei_list,id):
#     print(Taipei_list[6])
#     Carousel_template = TemplateSendMessage(
#         alt_text='Carousel template',
#         template=CarouselTemplate(
#         columns=[
#             CarouselColumn(
#                 thumbnail_image_url=Taipei_list[6],
#                 title=Taipei_list[0],
#                 text=Taipei_list[1]+"溫度 : "+Taipei_list[2]+"\n"+"天氣狀況 : "+Taipei_list[3]+"\n"+"舒適度 : "+Taipei_list[4]+"\n"+"降雨機率 (%)   : "+Taipei_list[5],
#                 actions=[
#                     PostbackTemplateAction(
#                         label='postback1',
#                         text='postback text1',
#                         data='action=buy&itemid=1'
#                     ),
#                     MessageTemplateAction(
#                         label='溫度',
#                         text="溫度 : "+Taipei_list[2]+"\n"+"天氣狀況 : "+Taipei_list[3]+"\n"+"舒適度 : "+Taipei_list[4]+"\n"+"降雨機率 (%)   : "+Taipei_list[5]
#                     )
#                 ]
#             )
#         ]
#     )
#     )
#     line_bot_api.push_message(id,Carousel_template)


def getTaipeiCarouselTemplate(Taipei_list,id):
    imagemap_message = ImagemapSendMessage(
                        base_url=Taipei_list[6]+"#",
                        alt_text=Taipei_list[0],
                        base_size=BaseSize(height=100, width=100),
                        actions=[
                            MessageImagemapAction(
                                text="溫度 : "+Taipei_list[2]+"\n"+"天氣狀況 : "+Taipei_list[3]+"\n"+"舒適度 : "+Taipei_list[4]+"\n"+"降雨機率 (%)   : "+Taipei_list[5],
                                area=ImagemapArea(
                                    x=520, y=0, width=520, height=520
                                )
                            )
                        ]
                    )
    line_bot_api.push_message(id,imagemap_message)