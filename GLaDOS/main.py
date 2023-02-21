from os import environ
from Check import CheckIn
from push import send_msg_serverJ , send_msg_pushplus


def main():
    # 获取actions secrets配置的cookie SendKey
    ck = environ["cookie"]
    SendKey = environ.get('SendKey')
    token = environ.get('token')
    try:
        title, Text = CheckIn(ck)
        print('签到成功！')
    except Exception as e:
        print('程序出错！')
        title = '程序出错！'
        Text = e
    finally:
        # print(title)
        print(Text)
        # Text = Text.replace('\n', '%0D%0A%0D%0A')
        
        rsp = send_msg_serverJ(SendKey, title, Text)  # 推送消息，无SendKey不推送
        print(rsp)
        
        rsp = send_msg_pushplus(token, title, Text)  # 推送消息，无token不推送
        print(rsp)


if __name__ == '__main__':
    main()