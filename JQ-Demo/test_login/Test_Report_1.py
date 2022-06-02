# # -- coding: utf-8 --
# import telegram
# import os
# import time
#
#
#
# chat_id = -1001778121979
#
# bot = telegram.Bot(token='5279516168:AAGhVQwciSm6wpWr7Pea7_Fldh_bm1-I0tw')
#
# date = time.strftime('%Y_%m_%d')
#
# doc = open(f'D:/apache/apache-jmeter-5.4.3/demo/report/html/'+'金球接口测试报告'+date+'.html','rb')
#
# bot.send_document(chat_id, doc)
#
# doc.close()
#
# # time.sleep(3)
# # # 删除该文件
# # os.remove('D:/apache/apache-jmeter-5.4.3/demo/report/html/'+'IntTestReport'+date+'.html')
#
# # 发送消息
# # bot.send_message(chat_id='-1001708533248', text="新消息")
#
# # 发送文本
# # doc = open(f'D:/apache/apache-jmeter-5.4.3/demo/report/html/IntTestReport2022-03-27.html', 'rb')
# # bot.send_document(chat_id, doc)
#
#
# # 发送视频
# # bot.send_video(chat_id='-1001708533248', video=open(f'D:/apache/apache-jmeter-5.4.3/demo/report/html/test2022_03_26_11_41.html', 'rb'), supports_streaming=True)
#
#
#
