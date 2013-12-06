# Copyright 2013 Mirantis Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.config import cfg


common_opts = [
    cfg.StrOpt('api_paste_config',
               default="api-paste.ini",
               help='File name for the paste.deploy config for magnetodb-api'),

    cfg.IntOpt('magnetodb_api_workers', default=None),

    cfg.StrOpt('bind_host', default="0.0.0.0"),

    cfg.IntOpt('bind_port', default=80),

    cfg.StrOpt('storage_impl', default="magnetodb.storage.impl.fake_impl"),

<<<<<<< HEAD
    cfg.StrOpt('storage_param', default="{}")
=======
    cfg.StrOpt('storage_param', default={})
>>>>>>> fa89c27ba3fda51c959ecf12dc121c74c50fe42e
]

CONF = cfg.CONF
CONF.register_opts(common_opts)


def parse_args(argv, default_config_files=None):
    cfg.CONF(args=argv[1:],
             project='magnetodb',
             default_config_files=default_config_files)
