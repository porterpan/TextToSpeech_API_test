import base64
import json
import time
import hashlib
import requests



class yuyi_hec(object):
    def __init__(self):
        # API请求地址、API KEY、APP ID等参数，提前填好备用
        self.api_url = "http://api.xfyun.cn/v1/service/v1/tts"
        self.API_KEY = "38f30ffa5f297b12bb271e164736cd49"
        self.APP_ID = "5d82345d"
        self.OUTPUT_FILE = "./output.mp3"    # 输出音频的保存路径，请根据自己的情况替换
        # TEXT = "苟利国家生死以，岂因祸福避趋之"
        self.TEXT = "教育数据挖掘是一种这些数据，wake，orange是4种工具。周德清小姐姐, you are so cute, and you roommate is extremely  the excellent one!"
        self.Erro_Tips = ""
    # 发送HTTP POST请求
    def getBody(self, text):
        data = {'text': text}
        return data
    def yuyinhec(self,InText,str_voice_name):
        # 构造输出音频配置参数
        Param = {
            "auf": "audio/L16;rate=16000",  # 音频采样率
            "aue": "lame",  # 音频编码，raw(生成wav)或lame(生成mp3)
            "voice_name": str_voice_name,# "x_xiaowei",  # x_xiaowei
            "speed": "50",  # 语速[0,100]
            "volume": "77",  # 音量[0,100]
            "pitch": "50",  # 音高[0,100]
            "engine_type": "aisound"  # 引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
        }
        # 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
        Param_str = json.dumps(Param)  # 得到明文字符串
        Param_utf8 = Param_str.encode('utf8')  # 得到utf8编码(bytes类型)
        Param_b64 = base64.b64encode(Param_utf8)  # 得到base64编码(bytes类型)
        Param_b64str = Param_b64.decode('utf8')  # 得到base64字符串

        # 构造HTTP请求的头部
        time_now = str(int(time.time()))
        checksum = (self.API_KEY + time_now + Param_b64str).encode('utf8')
        checksum_md5 = hashlib.md5(checksum).hexdigest()
        header = {
            "X-Appid": self.APP_ID,
            "X-CurTime": time_now,
            "X-Param": Param_b64str,
            "X-CheckSum": checksum_md5
        }
        response = requests.post(self.api_url, data=self.getBody(InText), headers=header)
        # 读取结果
        response_head = response.headers['Content-Type']
        if (response_head == "audio/mpeg"):
            out_file = open(self.OUTPUT_FILE, 'wb')
            data = response.content  # a 'bytes' object
            out_file.write(data)
            out_file.close()
            print('输出文件: ' + self.OUTPUT_FILE)
            self.Erro_Tips = '输出文件: ' + self.OUTPUT_FILE
        else:
            self.Erro_Tips = response.text
            print(response.text)
