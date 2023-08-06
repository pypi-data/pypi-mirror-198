from commmons import get_host_url
from lxml import html

from hypersquirrel.util import html_from_url_with_headers


def scrape(url: str, body: str = None):
    if body:
        tree = html.fromstring(body)
    else:
        tree = html_from_url_with_headers(url)
    host_url = get_host_url(url)

    divs = tree.xpath("//div[contains(@class, 'video-item')]")
    for div in divs:
        if "data-id" not in div.attrib:
            continue

        dataid = div.attrib["data-id"]
        atags = div.xpath("./a")

        if not atags:
            continue

        imgs = div.xpath("./a/picture/img")
        if not imgs:
            continue

        atag = atags[0]
        img = imgs[0]

        yield {
            "fileid": "sb" + dataid,
            "sourceurl": host_url + atag.attrib["href"],
            "filename": img.attrib["alt"],
            "thumbnailurl": img.attrib["data-src"]
        }
