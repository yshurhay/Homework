import aiohttp
import asyncio
import pandas as pd


async def get_info():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://belarusbank.by/api/news_info?lang=ru') as response:
            text = await response.json()
            return [{
                'заголовок': text[i]['name_ru'],
                'текст': text[i]['html_ru'],
                'дата': text[i]['start_date']
            }
                for i in range(20)]


async def main():
    all_news_info = await get_info()
    even_month_info = list(filter(lambda x: int(x['дата'][5:7]) % 2 == 0, all_news_info))
    max_letter_count = find_max_count(all_news_info)
    task_3_info = {
        'text_max_length': max(all_news_info, key=lambda x: len(x['текст'])),
        'article_max_length': max(all_news_info, key=lambda x: len(x['заголовок'].split()))['заголовок'],
        max_letter_count[0]: max_letter_count[1]
    }

    task_3 = pd.DataFrame(task_3_info)
    all_news = pd.DataFrame(all_news_info)
    even_month_news = pd.DataFrame(even_month_info)
    even_month_news.to_excel('even_month_news.xlsx')
    all_news.to_excel('all_news.xlsx')
    task_3.to_excel('task_3.xlsx')


def find_max_count(all_info):
    ALPHABET = 'йцукенгшщзхъфывапролджэячсмитьбюё'
    text = ''.join(info['текст'] for info in all_info)
    maximum = {}
    for letter in ALPHABET:
        maximum[letter] = text.lower().count(letter)
    return max(maximum.items(), key=lambda x: x[1])


if __name__ == '__main__':
    asyncio.run(main())
