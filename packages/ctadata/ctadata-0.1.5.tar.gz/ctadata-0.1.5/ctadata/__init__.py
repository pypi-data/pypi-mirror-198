import os
import logging
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)

# https://daskhub.dev.ctaodc.ch/services/downloadservice/fetch/pnfs/cta.cscs.ch/lst/DL1/20230226/v0.9_calib12100/tailcut84


def list_dir(url):
    return requests.get(
            urljoin("http://hub:5000/services/downloadservice/fetch/pnfs/cta.cscs.ch/", url),
            params = {'token': os.getenv("JUPYTERHUB_API_TOKEN")},
            stream=True
        ).json()


def fetch_and_save_file(url, fn=None):
    total_wrote = 0

    if fn is None:
        fn = url.split("/")[-1]

    with open(fn, "wb") as outf:
        with requests.get(
            urljoin("http://hub:5000/services/downloadservice/fetch/pnfs/cta.cscs.ch/", url),
            params = {'token': os.getenv("JUPYTERHUB_API_TOKEN")},
            stream=True
        ) as f:          
            f.raise_for_status()
            for r in f.iter_content(chunk_size=1024*1024):
                outf.write(r)                
                total_wrote += len(r)

    return total_wrote
        
    