
import configparser


def sendMessage(message):
    import requests
    inifile = configparser.SafeConfigParser()
    inifile.read('./config.ini')

    line_notify_token = inifile['settings']['notify_token']
    line_notify_api = 'https://notify-api.line.me/api/notify'

    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    line_notify = requests.post(line_notify_api, data=payload, headers=headers)



#sendMessage('test')
