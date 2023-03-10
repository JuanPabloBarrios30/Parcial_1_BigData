import requests
import boto3
from datetime import datetime


def get_json_data():
    json_data = {
        "filter": {
            "offer": {"slug": ["sell"]},
            "property_type": {"slug": ["house"]},
            "locations": {
                "zones": {
                    "slug": [
                        "zone-colombia-bogota-zona-chapinero",
                        "colombia-cundinamarca-bogotá-3630103-zona-chapinero"
                    ]
                }
            }
        },
        "fields": {
            "exclude": [],
            "facets": [],
            "include": [
                "area", "baths.id", "baths.name", "baths.slug",
                "client.client_type", "client.company_name",
                "client.first_name", "client.fr_client_id",
                "client.last_name", "client.logo.full_size",
                "garages.name", "is_new", "locations.cities.fr_place_id",
                "locations.cities.name", "locations.cities.slug",
                "locations.countries.fr_place_id", "locations.countries.name",
                "locations.countries.slug", "locations.groups.name",
                "locations.groups.slug", "locations.groups.subgroups.name",
                "locations.groups.subgroups.slug",
                "locations.neighbourhoods.fr_place_id",
                "locations.neighbourhoods.name",
                "locations.neighbourhoods.slug",
                "locations.states.fr_place_id",
                "locations.states.name", "locations.states.slug",
                "locations.location_point", "max_area", "max_price",
                "media.photos.list.image.full_size",
                "media.photos.list.is_main",
                "media.videos.list.is_main", "media.videos.list.video",
                "media.logo.full_size", "min_area", "min_price",
                "offer.name", "price", "products.configuration.tag_id",
                "products.configuration.tag_name", "products.label",
                "products.name", "products.slug", "property_id",
                "property_type.name", "fr_property_id",
                "fr_parent_property_id",
                "rooms.id", "rooms.name", "rooms.slug", "stratum.name", "title"
            ],
            "limit": 25,
            "offset": 0,
            "ordering": [],
            "platform": 41,
            "with_algorithm": True
        }
    }
    return json_data


def get_headers():
    return {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/109.0.0.0 Safari/537.36",
        "referer": "https://fincaraiz.com.co/"
    }


def get_url():
    url = 'https://api.fincaraiz.com.co/document/api/1.0/listing/search'
    return url


def get_file_name():
    dt = datetime.now()
    return "landing-casas-"+str(dt.date())+'.html'


def request_site(url, headers, json):
    response = requests.post(url, headers=headers, json=json)
    return response


def f(event, context):
    url = get_url()
    headers = get_headers()
    json_data = get_json_data()
    response = request_site(url, headers, json_data)
    data = response.text.encode('utf-8')
    s3 = boto3.resource('s3')
    s3.Object('bucketfincaraiz', get_file_name()).put(Body=data)
