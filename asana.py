import os

import asana
import requests

from dotenv import load_dotenv

load_dotenv()


class APIAsana:
    def __init__(self):
        self.token = os.environ.get('ASANA_TOKEN')
        self.project_gid = os.environ.get('ASANA_PROJECT_GID')
        self.workspace_gid = os.environ.get('ASANA_WORKSPACE_GID')
        self.user_gid = os.environ.get('ASANA_USER_GID')

    def _connect_asana(self):
        client = asana.Client.access_token(self.token)
        return client

    def _set_user_info(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }
        url = f'https://app.asana.com/api/1.0/users/me'
        response = requests.get(url=url, headers=headers)

        return response.json()

    def set_user_gid(self):
        user_gid = self._set_user_info()
        return user_gid['data']['gid']

    def set_user_tasks(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.token}'
        }

        url = f'https://app.asana.com/api/1.0/projects/{self.project_gid}/tasks?opt_fields="notes,name,assignee'
        response = requests.get(url=url, headers=headers)
        tasks = response.json()
        tasks_list = []
        for task in tasks['data']:
            if task['assignee']['gid'] == self.user_gid:
                tasks_list.append(task['name'])

        return tasks_list

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