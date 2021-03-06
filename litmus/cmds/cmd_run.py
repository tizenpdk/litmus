#!/usr/bin/env python3
# Copyright 2015-2016 Samsung Electronics Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from litmus.cmds import load_project_list, sdb_exist


def main(args):
    """docstring for main"""
    sdb_exist()
    prj_list = load_project_list(args.projects)
    project = next((prj for prj in prj_list if prj['name'] == args.project),
                   None)
    if not project:
        raise Exception('Project {} does not exists'.format(args.project))
    sys.path.append(project['path'])

    import userscript
    userscript.main(project_name=args.project,
                    project_path=project['path'],
                    param=args.param,
                    workingdir=args.workingdir,
                    topology=args.topology)
