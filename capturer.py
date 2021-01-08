from selenium import webdriver
import codecs

URL = "https://git-scm.com/book/de/v2/Git-Grundlagen-Taggen"
WEBPAGE_IDENTIFIER = '@misc'


def get_urls():
    with codecs.open('references.bib', 'r', encoding='utf8') as ref:
        line = ref.readline()
        cnt = 1
        urls = []
        while line:
            if not line.strip().startswith(WEBPAGE_IDENTIFIER):
                line = ref.readline()
                continue
            else:
                while line:
                    line = ref.readline()
                    if not line.strip().startswith('url'):
                        continue
                    else:
                        url = line.replace('url', '').replace('=', '').replace('{', '').replace('}', '') \
                            .replace(',', '').strip()
                        if url.endswith('/'):
                            url = url[:-1]
                        urls.append(url)
                        break
                line = ref.readline()
            cnt += 1
    return urls


def capture_webpage(url: str):
    print("capturing:", url)
    pic_name = url.replace('http://', '').replace('https://', '').replace('/', '-').replace('www.', '') \
                   .replace('.html', '') + ".png"
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
    driver.set_window_size(s('Width'), s(
        'Height'))  # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot(pic_name)
    driver.quit()
    print("saved:", pic_name)


if __name__ == '__main__':
    urls = get_urls()
    print(urls)
    for url in urls:
        capture_webpage(url)
