from cat.mad_hatter.decorators import tool, hook
from typing import Dict
from cat.log import log
from bs4 import BeautifulSoup
import requests
import re


@hook(priority=20)
def before_cat_reads_message(user_message_json, cat):
    urls = extract_between_curly_brackets(user_message_json["text"])
    if urls:
        for url in urls:
            url_content = scrape_text(url, cat)
            if url_content:
                new_message = substitute_between_curly_brackets(
                    user_message_json["text"], url, url_content
                )
                user_message_json["text"] = new_message

    return user_message_json


def scrape_text(url, cat):
    settings = cat.mad_hatter.get_plugin().load_settings()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            tags_to_remove = soup.find_all(
                [
                    "script",
                    "noscript",
                    "link",
                    "style",
                    "head",
                    "footer",
                    "header",
                    "nav",
                ]
            )
            for element in tags_to_remove:
                element.decompose()
            cleaned_html = str(soup)
            if settings["remove_html_tags"]:
                soup = BeautifulSoup(cleaned_html, "lxml")
                # Extract all text contents
                extracted_text = " ".join(
                    [text.strip() for text in soup.find_all(text=True)]
                )
            else:
                extracted_text = cleaned_html
            return extracted_text
        else:
            return None
    except Exception as e:
        return None


def extract_between_curly_brackets(input_string):
    pattern = r"\{\{.*?\}\}"
    matches = re.finditer(pattern, input_string)
    results = []

    for match in matches:
        results.append(match.group(0)[2:-2].strip())

    return results


def substitute_between_curly_brackets(input_string, old_content, new_content):
    pattern = r"\{\{" + old_content + "\}\}"
    replaced_string = re.sub(pattern, new_content, input_string)
    return replaced_string
