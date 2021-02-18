import requests

def most_common_word_on_web_page(words, url):
    response = requests.get(url)
    text = response.text
    return most_common_word(words, text)

def most_common_word(words, text):
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]


if __name__ == '__main__':
    mc = most_common_word_on_web_page(
        ['сеть', 'оффер', 'CPA'], 'https://leadrock.com'
    )
    print(mc)
