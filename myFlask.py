from twilio.rest import Client
import time
import json
from flask import Flask, request, jsonify
app = Flask(__name__)


#记录日志
def myLog(datas):
    log_file = open('sms.log', 'a+')
    log_str = ''
    log_str = log_str + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' '
    log_str = log_str + json.dumps( datas) + ' ';
    log_file.write(log_str + '\n')
    log_file.close()


#首页
@app.route('/')
def index():
    return 'Welcome,send sms api is /send[post],please send sms content to send api!'


#发送短信API
@app.route('/send', methods=['GET', 'POST'])
def send():
    #返回结果
    data = {}
    data['code'] = 'E001'
    if request.method == 'GET':
        #获取请求参数
        #key = request.args.get('key', '')
        data['msg'] = 'Not allowed to request method !'
        myLog(data)
        return jsonify(data)
    else:
        content = request.form.get('content', None)

        if content is None:
            data['msg'] = 'Please fill sms content'
            myLog(data)
            return jsonify(data)

        # Your Account SID from twilio.com/console
        account_sid = "ACdfe22133a6e3ddfe5c4ae2c0bb2e9dda"
        # Your Auth Token from twilio.com/console
        auth_token = "*******"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+8613248409848",
            from_="+16017650897",
            body = content)

        if message is None:
            data['msg'] = 'Fail send sms'
            myLog(data)
            return jsonify(data)

        print(message.sid)
        data['code'] = 'S001'
        data['sid'] = message.sid
        data['msg'] = 'Success'
        #response = make_response(jsonify({'test': 'good'}, 403)
        myLog(data)
        return jsonify(data)


#启动服务
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8090)
