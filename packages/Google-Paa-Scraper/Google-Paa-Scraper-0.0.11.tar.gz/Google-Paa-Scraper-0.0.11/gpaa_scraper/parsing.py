import re
from typing import Optional, List

from bs4 import Tag, BeautifulSoup

from gpaa_scraper.exception import PAADoesNotExist
from gpaa_scraper.browser import get_page_source
from gpaa_scraper.container import Answer
from gpaa_scraper.utils import _youtube_check, _table_check, _list_check, _get_paragraph_answer

def extract_answer(answer_block: Tag):
    """
    Takes a html blob of single question and returns its relevant answer.

    :param answer_block: Bs4 Tag element containing the relevant data
    """
    div_under_related_question_pair = answer_block.find('div', class_=re.compile(
        r'related-question-pair')).find('div', recursive=False)

    question_answer_tags = div_under_related_question_pair.find_all('div', recursive=False)

    if len(question_answer_tags) == 3:

        question_tag, answer_tag = question_answer_tags[1], question_answer_tags[2]
        under_answer_tag = answer_tag.find_all('div', recursive=False)
        question_str = question_tag.find('span').text if question_tag.find('span') else None

        if question_str:
            answer_class = Answer(question=question_str)
            answer_tag = under_answer_tag[0].find('div')
            divs_with_only_id = answer_tag.find_all('div', recursive=False)[:-1]

            if ans := _youtube_check(divs_with_only_id, answer_class):
                return ans

            elif ans := _table_check(divs_with_only_id, answer_class):
                return ans

            elif ans := _list_check(divs_with_only_id, answer_class):
                return ans

            else:
                ans = _get_paragraph_answer(divs_with_only_id, answer_class)
                return ans

    return


def _get_questions(html: str,
                   ) -> Optional[List]:
    """returns all questions"""

    bs = BeautifulSoup(html, 'lxml')
    try:
        main_block = bs.find(
            'div', {
                "id": "rso", "data-async-context": re.compile(r'query:')})

        questions = main_block.select(
            'div[data-sgrd="true"] > div')

        return questions

    except AttributeError:
        return None


def get_answers_from_source(html: str) -> list[Answer]:
    """
    parse question and their answers from a page.

    :param html: html content with questions_html
    """

    questions_and_answers = []
    questions_html = _get_questions(html)
    if questions_html:
        for question in questions_html:
            qna = extract_answer(question)
            if qna:
                questions_and_answers.append(qna)

    return questions_and_answers


def scrape_paa(keyword: str, question_range=10, headless=True) -> Optional[list[Answer]]:
    """
    @param keyword: keyword to get answers for.
    @param question_range: the larger the question range, the more questions it yields, but with more time. default range is 10, which is ~15-20 seconds and 25-30 questions
    @param headless: if false, open a browser.
    """
    if not isinstance(question_range, int):
        raise ValueError(f"{question_range} is not an int")
    try:
        html = get_page_source(keyword, question_range, headless)
        answers = get_answers_from_source(html)
        return answers if answers else None

    except PAADoesNotExist:
        raise PAADoesNotExist
