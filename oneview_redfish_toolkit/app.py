# -*- coding: utf-8 -*-

# Copyright (2017) Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
import os

from flask import Flask

from oneview_redfish_toolkit.blueprints.computer_system import computer_system
from oneview_redfish_toolkit.blueprints.computer_system_collection \
    import computer_system_collection
from oneview_redfish_toolkit.blueprints.redfish_base import redfish_base
from oneview_redfish_toolkit.blueprints.service_root import service_root
from oneview_redfish_toolkit import util

import logging


util.configure_logging(os.getenv("LOGGING_FILE",
                                 "oneview_redfish_toolkit/logging.ini"))

# Load config file, schemas and creates a OV connection
try:
    util.load_config('oneview_redfish_toolkit/redfish.ini')
except Exception as e:
    logging.error('Failed to load app configuration')
    logging.error(e)
    exit(1)

# Flask application
app = Flask(__name__)

# Register blueprints
app.register_blueprint(redfish_base, url_prefix="/redfish")
app.register_blueprint(service_root, url_prefix='/redfish/v1/')
app.register_blueprint(computer_system_collection)
app.register_blueprint(computer_system)