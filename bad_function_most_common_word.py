import requests

def most_common_word_in_web_page(words, url):
    response = requests.get(url)
    text = response.text
    word_frequency = {w: text.count(w) for w in words}
    return sorted(words, key=word_frequency.get)[-1]

if __name__ == '__main__':
    mc = most_common_word_in_web_page(
        ['CPA', 'оффер', 'сеть'], 'https://leadrock.com'
    )
    print(mc)
