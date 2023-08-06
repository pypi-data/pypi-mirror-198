from transformers import pipeline
from newspaper import Article
from GoogleNews import GoogleNews
from io import StringIO
import re
import base64
import argparse
import json
import sys
import html


def sanitize_search_string(search_string):
    """
    Sanitizes a search string input for a news website in Python.
    """
    # escape HTML entities
    search_string = html.escape(search_string)

    # strip non-alphanumeric characters using regular expressions
    search_string = re.sub(r'[^\w\s]', '', search_string)

    # limit the length of the search string to 30 characters
    search_string = search_string[:30]

    # validate the search string to ensure that it only contains expected characters
    if not re.match(r'^[\w\s\-\.,!?"\']+$', search_string):
        raise ValueError("Invalid search string")

    return search_string


def segment_text(text):
    # Split the text into sentences using regular expressions
    sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!) ', text)

    # Initialize variables
    segments = []
    current_segment = ''
    words_in_current_segment = 0

    # Iterate over sentences
    for sentence in sentences:
        # Add sentence to current segment if it won't exceed the limit
        if words_in_current_segment + len(sentence.split()) <= 500:
            if len(current_segment) > 0:
                current_segment += ' '
            current_segment += sentence
            words_in_current_segment += len(sentence.split())
        else:
            # Add current segment to list and start a new one
            segments.append(current_segment)
            current_segment = sentence
            words_in_current_segment = len(sentence.split())

    # Add the last segment to the list
    if len(current_segment) > 0:
        segments.append(current_segment)

    return segments


def main():
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Create the argument parser
    parser = argparse.ArgumentParser()

    # Add the named arguments
    parser.add_argument("-m", "--max-articles",
                        help="Maximum number of articles to summarize", type=int, required=False)
    parser.add_argument("-t", "--news-topic",
                        help="Topic of the news articles to summarize", type=str, required=True)

    # Parse the arguments
    args = parser.parse_args()

    max_articles = args.max_articles if args.max_articles else 5
    news_topic = sanitize_search_string(args.news_topic)

    summarizer = pipeline(
        "summarization", model="philschmid/bart-large-cnn-samsum")

    gn = GoogleNews(lang='en', encode='utf-8')
    gn.enableException(True)
    gn.get_news(news_topic + ' news')

    return_dict = {}

    for r in gn.results()[:max_articles]:
        l = r['link']
        l = bytes(l.split('articles/')[1].split('?')
                  [0].strip(), 'utf-8') + b'=='
        try:
            l = base64.b64decode(l)[4:-3].decode('utf-8')
        except:
            print('Base64 decode failed on: ', l)
            continue
        a = Article(l)
        try:
            a.download()
            a.parse()
        except:
            print('Article failed on: ', l)
            continue

        segments = segment_text(a.text)
        total_summary = ''
        if len(segments) > 1:
            for segment in segments:
                tokens = summarizer.tokenizer(segment)
                segment_summary = summarizer(
                    segment, do_sample=False)[0]['summary_text']
                total_summary += segment_summary + ' '
        else:
            total_summary = segments[0]
        tokens = summarizer.tokenizer(total_summary)
        final_summary = summarizer(
            total_summary, do_sample=False)[0]['summary_text']

        return_dict[l] = final_summary

    sys.stdout = old_stdout
    print(json.dumps(return_dict))
    sys.exit(0)
