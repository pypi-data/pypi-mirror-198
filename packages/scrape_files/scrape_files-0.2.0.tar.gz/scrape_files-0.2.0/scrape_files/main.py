"""
`scrape_files` is a tool to help scrape things online to your local machine.
Currently, it supports scraping images in a web page as well as scraping and converting htmls to well-formatted markdowns for easy reading.
"""

import os
import sys
import re
import time
import requests
import concurrent.futures
from threading import Lock
from lxml import etree
import urllib
from urllib.parse import urlparse, urljoin
# from functools import wraps
from fake_user_agent import user_agent


ua = user_agent()
headers = {"User-Agent": ua}

count = 0
total = 0 
ops = ["FETCHING", "RETRY FETCHING", "PARSING", "SAVING"]
base_page_text ="" 
base_page_url = ""


def fetch(url, session, stream=False):
    "Fetch a web page with retry mechanism."

    attempt = 0 
    proxies = requests.utils.getproxies()
    # requests.utils.get_environ_proxies("https://www.google.com")
    
    session.headers.update(headers)
    session.proxies = proxies

    while True:
        try:
            r = session.get(url, timeout=9.05, stream=stream)
        except requests.exceptions.HTTPError as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except requests.exceptions.ConnectTimeout as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except requests.exceptions.ConnectionError as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except requests.exceptions.ReadTimeout as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except requests.exceptions.ProxyError as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except Exception as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        else:
            if r.status_code != 200:  # only a 200 response has a response body
                attempt = call_on_error(r.status_code, url, attempt, ops[1])
            return r


def call_on_error(error, url, attempt, op):
    attempt += 1

    logger.debug(f"{op} file from {url} {attempt} times")

    if attempt == 3:
        print(f"Maximum {op} reached: {error}")
        sys.exit()
    return attempt


"""
def fetch_js(url):
    "Fetch the web page with retry mechanism using selenium. 
    Needs to download chromedriver first.
    Only for special use."

    from selenium import webdriver

    attempt = 0 
    while True:
        try:
            driver = webdriver.Chrome()
            driver.get(url)
            page_source = driver.page_source
            driver.quit()
        except http.client.RemoteDisconnected as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        except Exception as e:
            attempt = call_on_error(e, url, attempt, ops[1])
            continue
        else:
            return page_source 
"""

# Parse links with in <p> tag
def parse_links():
    tree = etree.HTML(base_page_text.encode("utf-8"))

    # for friends transcripts at https://fangj.github.io/friends/
    # link_nodes = tree.xpath("//ul/li/a")

    link_nodes = tree.xpath("//p/a")
    links = []
    for l in link_nodes:
        loc = l.attrib["href"] 
        name = l.text
        if not loc.startswith("http"):
            loc = base_page_url + loc
        pair = (name, loc)
        links.append(pair) 
    return links


def parse_imgs(formats):
    img_list = []
    tree = etree.HTML(base_page_text.encode("utf-8"))
    img_links = tree.xpath("//img/@src")
    if img_links:
        for link in img_links:
            if urlparse(link).path.split(".")[-1] in formats:
                img_list.append(link)
    a_links = tree.xpath("//a/@href | //a/@data-original")
    if a_links:
        for link in a_links:
            if urlparse(link).path.split(".")[-1] in formats:
                img_list.append(link)
    if img_list:
        for index, img in enumerate(img_list):
            img = img.strip()
            if re.match(r"^//.+", img):
                img_list[index] = "https:" + img
            if re.match(r"^/[^/].+", img):
                img_list[index] = urljoin(base_page_url, img)
        img_list = set(img_list) 
        return img_list
    else:
        print("No images found.")
        sys.exit()


def process_dir(dir):
    try:
        os.mkdir(dir)
    except FileExistsError:
        return
    except OSError as e:
        logger.error(str(e))
        sys.exit()


def process_img_path(dir, formats, link):
    process_dir(dir)

    img_name = "_".join(link.split("/")[-2:])
    if "?" in img_name:
        img_name = img_name.split("?")[0]
    if img_name.split(".")[-1] not in formats:
        img_name = img_name + ".jpg"
    img_path = os.path.join(dir, img_name)
    return img_path


def save_img(session, link, dir, formats):
    r = fetch(link, session, stream=True)
    path = process_img_path(dir, formats, link)

    try: 
        with open(path, "wb") as f:  # for stream=True, you have to use with open, otherwise it will generate "write to closed file" error
            for chunk in r:
                f.write(chunk)
        logger.debug("Saved file to %s", path)
    except Exception as e:
        logger.debug(str(e))


def save_to_markdown(session, link, dir=None, level=1, title=None):
    if level == 1:
        text = base_page_text
    else:
        r = fetch(link, session)
        text = r.text

    # This line is only for texts that have html characters as below: 
    # text = text.replace("\n", " ").replace("  ", " ").replace("&nbsp;", "").replace("&#146;", "'").replace("&#151;", "-").replace("&#133;", "...").replace("&#145;", "'")
    
    # Create file path
    if not title:
        match = re.search(r'<title[^>]*>(.*?)(?=</title>)', text, re.S)
        if match:
            title = match.group().split(">")[1]
        else:
            title = "untitled"
  
    # Transform Chiness punctuation marks to english ones, for better file naming and terminal displaying
    # The syntax only allows the key in the dictionary to be one character long
    trans_pattern = str.maketrans({"’": "'", "—": "-", "…": "...", "‘": "'", "：": ":", "，": ",", "？": "?"})
    title = title.translate(trans_pattern)

    # Get rid of symbols from title
    title = title.replace(",", "").replace(" ", "_").replace("__", "_").replace(".", "").split("?")[0].split(":")[0].strip('"').strip("'").title()
    
    path = title + ".md"

    if dir:
        process_dir(dir)
        path = os.path.join(dir, path)

    # Narrow down to article node if any
    article = re.search(r'<article(.*?)</article>', text, re.S)
    if article:
        tree = etree.HTML(article.group().encode("utf-8"))
    else:
        tree = etree.HTML(text.encode("utf-8"))

    # Write to file
    try:
        with open(path, "w") as f:

            #if title != "untitled":
            #    f.write(title)
            #    f.write("\n---\n\n")

            # Xpath will sort the returned list according the order in the source
            # You shouldn't only depend on what you see on browser inspect screen, you can only depend on the source file content by `view page source`
            # For emogis, there is no <img> tag in source file, but there is on inspect.
            # There is no `tabindex` attribute in source file, but there is on inspect.
            # New Discovery: if if ntag block has logics that can be performed by lxml, you can't get the right result from `tree.xpath()`
            # E.g. nodes = tree.xpath("//pre") should have 17 nodes, but things under `if ntag == "pre"` go wrong, nodes is None or sometimes its number is 1.  
            nodes = tree.xpath("//p[not(img) and not(parent::blockquote) and not(ancestor::aside)] | //h1 | //h2 | //h3 | //h4 | //blockquote[not(parent::aside)] | //img[not(parent::noscript) and not(ancestor::aside) and not(ancestor::span)] | //hr | //code[not(parent::p) and (ancestor::article) and not(parent::pre)] | //pre | //ul[(ancestor::article)] | //ol | //p/img")
            for n in nodes:
                ntag = n.tag
                if ntag == "p":
                    # Scenario: <p></p>, which blocks other elements from printing
                    # i.e. check there is no text and no children
                    if n.text is None and len(list(n)) == 1 and list(n)[0].text is None:
                        continue
                    else:
                        codes = []
                        links = {}
                        br = ""
                        strongs = []
                        italics = []
                        for c in n.iterchildren():
                            if c.tag == "code":
                                codes.append(c.text)
                            if c.tag == "a":
                                links[c.text] = c.attrib["href"]
                            if c.tag == "br":
                                br = c.tail
                            if c.tag == "strong":
                                strongs.append(c.text)
                            if c.tag == "i":
                                italics.append(c.text)
                        text = list(n.itertext())
                        if not text:
                            continue
                        else:
                            for i in text:
                                if i in codes:
                                    f.write("`" + i + "`")
                                elif i in links.keys():
                                    f.write("[" + i + "]" + "(" + links[i] + ")")
                                elif i == br:
                                    i = i.replace("\xa0", " ")
                                    f.write("\n\n" + i)
                                elif i in strongs:
                                    f.write("**" + i + "**")
                                elif i in italics:
                                    f.write("*" + i + "*")
                                else:
                                    i = i.replace("\xa0", " ")
                                    f.write(i)
                            if n.getnext() is not None and n.getnext().tag == "p":
                                f.write("\n\n")
                            elif n.getnext() is not None and n.getnext().tag.startswith("h"):
                                f.write("\n\n")
                            else:
                                f.write("\n")
                if ntag == "h1": 
                    f.write("# ")
                    for i in n.itertext():
                        f.write(i)
                    f.write("\n\n")
                if ntag == "h2":
                    if "tabtitle" in n.values():
                        continue
                    else:
                        f.write("## ")
                        for i in n.itertext():
                            f.write(i)
                        f.write("\n")
                if ntag == "h3":
                    f.write("### ")
                    for i in n.itertext():
                        f.write(i)
                    f.write("\n")
                if ntag == "h4":
                    f.write("#### ")
                    codes = []
                    for c in n.iterchildren():
                        if c is not None and c.tag == "code":
                            codes.append(c.text)
                    for i in n.itertext():
                        if i in codes:
                            f.write("`" + i + "`")
                        else:
                            f.write(i)
                    f.write("\n")
                if ntag == "blockquote":
                    f.write("> ")
                    for i in n.itertext():
                        if i != " ":
                            f.write(i)
                    f.write("\n\n")
                if ntag == "img":
                    if "data-original" in n.keys():
                        f.write("![image]" + "(" + n.attrib["data-original"] + ")" + "\n\n")
                    elif "src" in n.keys():
                        if "data-actualsrc" in n.keys():
                            loc = n.attrib["data-actualsrc"]
                        else:
                            loc = n.attrib["src"]
                
                        if loc.startswith("http"):
                            f.write("![image]" + "(" + loc + ")" + "\n\n")
                        else:
                            f.write("![image]" + "(" + link + loc + ")" + "\n\n")
                if ntag == "hr":
                    f.write("---\n\n")
                if ntag == "pre":
                    # check if the element is a tag element with no text.
                    # `if not n.text` does not work.
                    # `if n.text == "" does not work.
                    if n.text is None and len(list(n)) == 0:
                        continue
                    else:
                        f.write("```")
                        text = list(n.itertext())
                        for i in text:
                            if not i.startswith("\n"):
                                f.write("\n")
                            f.write(i)
                        if text[-1].endswith("\n"):
                            f.write("```\n\n")
                        else:
                            f.write("\n```\n\n")
                if ntag == "code":
                    text = n.text.replace("\xa0", " ")
                    attrs = n.keys()
                    if not attrs:
                        f.write("`" + text + "`")
                    else:
                        values = n.values()
                        parent = n.getparent()
                        if parent.getprevious() is None and n.getprevious() is None:
                            f.write("```\n")
                                
                        if "comments" in values or text[-1] == ";" or text.strip() == "}": 
                            f.write(text + "\n")
                        elif "preprocessor" in values:
                            f.write(text + "\n\n")
                        elif text.strip() == "{":
                            f.write("\n" + text + "\n")
                        else:
                            #if text[-1] == "(" or (n.getnext() is not None and n.getnext().text == ")") or (n.getnext() is not None and n.getnext().text == "("):
                            #    f.write(text)
                            if n.getnext() is not None and n.getnext().text[0].isalnum() and text[-1] != "(":
                                f.write(text + " ")
                            else:
                                f.write(text)
                                
                        if parent.getnext() is None and n.getnext() is None:
                            f.write("```\n\n")
                if ntag == "ul" or ntag == "ol":
                    for c in n.iterchildren():
                        if c is not None and c.tag == "li":
                            strongs = []
                            italics = []
                            for cc in c.iterchildren():
                                if cc is not None and cc.tag == "strong":
                                    strongs.append(cc.text)
                                if cc is not None and cc.tag == "i":
                                    italics.append(cc.text)
                            f.write("- ")
                            for i in c.itertext():
                                if i == "\n":
                                    continue
                                elif i in strongs:
                                    f.write("**" + i + "**")
                                elif i in italics:
                                    f.write("*" + i + "*")
                                else:
                                    i = i.replace("\xa0", " ")
                                    f.write(i)
                            f.write("\n")
                    f.write("\n")
                    
            f.write("\n---\nSource: " + link)
        logger.debug("Saved file to %s", path)
    except Exception as e:
        logger.debug(str(e))


def download():
    args = parse_args()
    url = get_url(args.url)

    lock = Lock()
    global base_page_text
    global base_page_url
    global total
    global count

    with requests.Session() as session:

        print(f"{ops[0]} {url} ...")
        response = fetch(url, session)
        base_page_text = response.text
        base_page_url = url

        if args.subparser_name == "image":
            formats = args.format
            _, dir = get_download_dir(url, args.dir)

            print(f"{ops[2]} {url} ...")
            
            img_list = parse_imgs(formats)
            if not img_list:
                print("No files found")
                sys.exit()

            total = len(img_list)
            print(f"FOUND {total} files")
            print(f"{ops[3]} files ...")
            update(count, total)
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                for link in img_list:
                    executor.submit(save_img, session, link, dir, formats)
                    lock.acquire()
                    count += 1
                    lock.release()
                    update(count, total)

        if args.subparser_name == "html":
            level = args.level
            check, dir = get_download_dir(url, args.dir)

            if level == 1:
                print(f"{ops[2]} {url} ...")
                total += 1 
                print(f"FOUND {total} files")
                print(f"{ops[3]} files ...")
                update(count, total)
                if check:
                    save_to_markdown(session, base_page_url, dir)
                else:
                    save_to_markdown(session, base_page_url)
                count += 1
                update(count, total)

            if level == 2:
                print(f"{ops[2]} {url} ...")
                link_list = parse_links()
                if not link_list:
                    print("No files found")
                    sys.exit()

                total = len(link_list)
                print(f"FOUND {total} files")
                print(f"{ops[3]} files ...")
                update(count, total)
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    for i in link_list:
                        title = i[0]
                        link = i[1]
                        executor.submit(save_to_markdown, session, link, dir, level, title)
                        lock.acquire()
                        count += 1
                        lock.release()
                        update(count, total)

    print("DONE!")
    print(f"DOWNLOADED {count} files")
    print(f"FAILED: {total - count}")


def timer(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        start_at = time.time()
        f = func(*args, **kwargs)
        time_taken = time.time() - start_at
        print(f"Time taken: {round(time_taken, 2)} seconds")
        return f

    return wrapper


@timer
def main():
    try:
        download()
    except KeyboardInterrupt:
        print("\nCancelled out by user.")


if __name__ == "__main__":
    import os
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from scrape_files.args import parse_args, get_url, get_download_dir
    from scrape_files.progressbar import update
    from scrape_files.log import logger

    main()

else:
    from .args import parse_args, get_url, get_download_dir
    from .progressbar import update
    from .log import logger

