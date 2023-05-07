"""Retrieve and print data from a URL.

Usage:
    python get_data.py <URL>
"""
from urllib.request import urlopen


def fetch_source_code(url):
    """Fetch the html code from a URL.

    Args:
        url: The URL of a website.

    Returns:
        A HTML document.
    """
    html = urlopen(url)
    return html


def hhd5(url):
    """Fetch the data from a URL.

    Args:
        url: The URL of a website.

    Returns:
        Bytes data of the document.
    """
    with urlopen(url) as text:
        data = text.read()
        print(type(data))
        return data


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words


def print_items(items):
    """Print items one per line

    Args:
        items: An iterable series of printable items.
    """
    for item in items:
        print(item)


def main(url):
    """Print data from a URL.

    Args:
        url: The URL of a website.
    """
    # html = fetch_source_code(url)
    data = fetch_data(url)
    # words = fetch_words(url)

    # print(html)
    print("URL data is: ", data)
    # print_items(words)


if __name__ == '__main__':
    url = input("URL is: ")
    main(url)   # The 0th arg is the module filename.
