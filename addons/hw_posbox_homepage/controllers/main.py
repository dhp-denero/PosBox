# -*- coding: utf-8 -*-
import logging
import os
import time
from os import listdir

import openerp
from openerp import http
from openerp.http import request
from openerp.tools.translate import _

_logger = logging.getLogger(__name__)

index_template = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>BizzCloud's PosBox</title>
        <style>
        body {
            width: 480px;
            margin: 60px auto;
            font-family: sans-serif;
            text-align: justify;
            color: #6B6B6B;
        }
        </style>
    </head>
    <body>
        <h1>Your PosBox is up and running</h1>
        <p>
        The PosBox is an hardware adapter that allows you to use 
        receipt printers and barcode scanners with BizzCloud's Point of
        Sale. You can start an <a href='http://www.bizzcloud.nl'>online free trial</a>.
        </p>
        <p>
        To see the status of the connected hardware, please refer 
        to the <a href='/hw_proxy/status'>hardware status page</a>
        </p>
        <p>
        The PosBox software installed on this posbox is <b>version 11</b>, 
        You can upgrade the software on the <a href='/hw_proxy/upgrade/'>upgrade page</a>
        </p>
        <p>For any other question, please contact the BizzCloud support at <a href='mailto:support@bizzcloud.nl'>support@bizzcloud.nl</a>
        </p>
    </body>
</html>

"""


class PosboxHomepage(openerp.addons.web.controllers.main.Home):
    @http.route('/', type='http', auth='none', website=True)
    def index(self):
        #return request.render('hw_posbox_homepage.index',mimetype='text/html')
        return index_template
        
