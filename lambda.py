from urllib2 import urlopen
import xml.etree.ElementTree as ET


def handler(event, context):
    r = urlopen('http://thecatapi.com/api/images/get?format=xml&results_per_page=1')
    root = ET.fromstring(r.read())
    url = root.find('.//url').text
    return {'text': url}
