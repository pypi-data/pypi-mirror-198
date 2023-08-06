import requests


def ask(question=None, session=None, user=None):
    if not user:
        return '请传入用户{user}'
    data = {
        'session': session,
        'user': user,
        'question': question,
    }
    response = requests.post('http://openai.yige.space/api/data/', data=data)
    if response.status_code == 200:
        return response.json()['data']['answer']
    else:
        return '用户无效，请续费'


if __name__ == '__main__':
    print(ask(user='test', question='你好'))
