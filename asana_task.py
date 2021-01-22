import os
from pprint import pprint

import asana
import requests

from dotenv import load_dotenv

load_dotenv()

class CreateTaskAsana:
    def __init__(self):
        self.token = os.environ.get('ASANA_TOKEN')
        self.project_gid = str(os.environ.get('ASANA_PROJECT_GID'))
        self.workspace_gid = str(os.environ.get('ASANA_WORKSPACE_GID'))

    def _connect_asana(self):
        client = asana.Client.access_token(self.token)
        return client

    def set_projects(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.get('https://app.asana.com/api/1.0/projects', headers=headers)
        response = response.json()

        return response

    def set_project(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.get(f'https://app.asana.com/api/1.0/projects/{self.project_gid}', headers=headers)
        response = response.json()

        return response

    def create_task(self):
        client = self._connect_asana()
        result = client.tasks.create_task({
            'name': 'Testuje cos po raz drugi',
            'notes': 'Tworze taska przez api',
            'projects': self.project_gid,
            'parent': None,
            'workspace': self.workspace_gid},
            opt_pretty=True)

task_asana = CreateTaskAsana()

asana_obj = CreateTaskAsana()
projects_info = asana_obj.set_projects()
print('Projects info:')
pprint(projects_info)


project_info = asana_obj.set_project()
print('Project info:')
pprint(project_info)
