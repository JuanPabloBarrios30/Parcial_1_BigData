from datetime import datetime
from apps import request_site, get_file_name, get_headers, get_url


def test_request_site(mocker):
    url = "https://www.fincaraiz.com.co/finca-raiz/venta/chapinero/bogota"
    mocker.patch("requests.post", return_value=True)
    html = request_site(url, json="Json", headers="Headers")
    assert html


def test_get_url():
    url = 'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
    assert get_url() == url


def test_get_headers():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/109.0.0.0 Safari/537.36",
        "referer": "https://fincaraiz.com.co/"
    }
    assert get_headers() == headers


def test_get_file_name():
    dt = datetime.now()
    file_name = "landing-casas-" + str(dt.date()) + '.html'
    assert get_file_name() == file_name
