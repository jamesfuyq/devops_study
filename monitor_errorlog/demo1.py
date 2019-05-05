# -*- coding: utf-8 -*-
import sys
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider

"""
短信业务调用接口示例，版本号：v20170525

Created on 2017-06-12

"""

reload(sys)
sys.setdefaultencoding('utf8')


def send_sms(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name);

    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    # TODO 业务处理

    return smsResponse


if __name__ == '__main__':
    #REGION = "cn-hangzhou"
    REGION = "cn-beijing"
    PRODUCT_NAME = "Dysmsapi"
    DOMAIN = "dysmsapi.aliyuncs.com"
    
    # ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
    ACCESS_KEY_ID = "this is api key"
    ACCESS_KEY_SECRET = "this is api key secret code"
    TEMPLATE_CODE = "SMS_123666155"
    SIGN_NAME = "阿里云短信测试专用"
    
    acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
    region_provider.add_endpoint(PRODUCT_NAME,REGION,DOMAIN)
    __business_id = uuid.uuid1()
    print __business_id
    params = "{\"filename\":\"某个业务的错误日志\",\"ip_address\":\"1.1\"}"
    print send_sms(__business_id, "18511111111", SIGN_NAME, TEMPLATE_CODE, params)
