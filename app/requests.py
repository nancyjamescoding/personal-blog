import json
import urllib.request


def get_quote():
    with urllib.request.urlopen("http://quotes.stormconsultancy.co.uk/random.json") as resp:
        res = resp.read().decode('utf-8')
        res = json.loads(res)
    return res
