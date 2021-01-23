import os

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

        return response.json()

    def set_project(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        response = requests.get(f'https://app.asana.com/api/1.0/projects/{self.project_gid}', headers=headers)

        return response.json()

    def create_task(self, name: str, notes: str):
        client = self._connect_asana()
        result = client.tasks.create_task({
            'name': name,
            'notes': notes,
            'projects': self.project_gid,
            'parent': None,
            'workspace': self.workspace_gid},
            opt_pretty=True)
