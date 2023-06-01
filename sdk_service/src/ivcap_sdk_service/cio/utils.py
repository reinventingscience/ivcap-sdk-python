#
# Copyright (c) 2023 Commonwealth Scientific and Industrial Research Organisation (CSIRO). All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file. See the AUTHORS file for names of contributors.
#
from typing import BinaryIO
import requests

from ..logger import sys_logger as logger
from ..itypes import Url

def download(url: Url, fhdl: BinaryIO, chunk_size=None, close_fhdl=True):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        ct = r.headers.get('Content-Type')
        logger.debug(f"cio#download: request {r} - {ct} - {r.headers}")

        # if ct:
        #     cname = f"{cname}.{ct.replace('/', '.')}"
        # (fh, path) = self.cacheIO.get_fd(cname)
        # logger.info(f"Downloading {url} to cache {path}")

        for chunk in r.iter_content(chunk_size=chunk_size): # 8192): 
            #logger.info(f"chunk {chunk}")
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            #if chunk: 
            fhdl.write(chunk)
    fhdl.flush()
    if close_fhdl:         
        fhdl.close()
