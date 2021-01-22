import argparse
from pprint import pprint

from asana_task import CreateTaskAsana

parser = argparse.ArgumentParser(description='Create your tasks in Asana using API Asana.')
parser.add_argument('-p', '--projects', action='store_true', help='Show all projects')
parser.add_argument('-o', '--oneproject', action='store_true', help='Show project info')
parser.add_argument('-t', '--task', action='store_true', help='Create task')

args = parser.parse_args()

if args.projects:
    asana_obj = CreateTaskAsana()
    all_projects = asana_obj.set_projects()
    pprint(all_projects)

if args.oneproject:
    asana_obj = CreateTaskAsana()
    project_info = asana_obj.set_project()
    pprint(project_info)

if args.task:
    asana_obj = CreateTaskAsana()
    send_task = asana_obj.create_task(name='nazwa', notes='notatka')
