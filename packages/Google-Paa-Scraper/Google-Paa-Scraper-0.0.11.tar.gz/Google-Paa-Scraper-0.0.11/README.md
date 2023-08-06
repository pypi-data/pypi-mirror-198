<h1>Google-Paa-Scraper</h1>

### _Get data from googles people also ask section._

***

Google Paa Scraper provides a single function that enables you to scrape google people also ask questions and answers in bulk, ranging from 23-30 to max, under google runs out. but getting more answers require more time.

Auto download for chromedriver thanks to [webdriver-manager](https://pypi.org/project/webdriver-manager/).

## Example Usage:

```python
>>> from gpaa_scraper import scrape_paa
>>> answers = scrape_paa("csgo")
>>> print(type(answers))
class 'list'>
>>> print(answers[0])
Answer(question='Is CSGO free?', answer_heading=None, answer='The free download of CS:GO includes the full game. Free CS:GO players receive access to all game modes and matchmaking types with the exception of Ranked Matchmaking, which requires Prime Status to participate in.', answer_type=<AnswerType.Paragraph: 'paragraph'>, truncated_info_link=None)
```

### Return Values:
 Returns a list of Answer objects which can be imported from 
```python
from gpaa_scraper.container import Answer, AnswerType
```


| answer_type              | return type  | return value                 |
|--------------------------|--------------|------------------------------|
| *<AnswerType.List>*      | list         | ordered or unordered values  |
| *<AnswerType.Table>*     | list of list | first item is the header     |
| *<AnswerType.Youtube>*   | str          | youtube link                 |
| *<AnswerType.Paragraph>* | str          | string of answer             |


## Installation:
OS X & Linux:
```shell
pip3 install Google-Paa-Scraper
```

Windows:

```shell
pip install Google-Paa-Scraper
```


### PyPI: [https://pypi.org/project/Google-Paa-Scraper/](https://pypi.org/project/Google-Paa-Scraper/)
### Github: [https://github.com/huzai786/Google-Paa-Scraper](https://github.com/huzai786/Google-Paa-Scraper)



## Dependencies:
 * [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 * [Selenium](https://www.selenium.dev/documentation/)
 * [webdriver-manager](https://pypi.org/project/webdriver-manager/)
 * [lxml](https://lxml.de/)


## Release History
* 0.1.0
    * The first proper release
