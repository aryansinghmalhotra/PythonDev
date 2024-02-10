import requests

def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/jokes/programming/random')
    if response.status_code == 200:
        joke = response.json()[0]
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Couldn't retrieve a joke"

print(get_joke())