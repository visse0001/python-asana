import argparse
from pprint import pprint

from asana import APIAsana

parser = argparse.ArgumentParser(description='Create your tasks in Asana using API Asana.')
parser.add_argument('-p', '--projects', action='store_true', help='show all projects')
parser.add_argument('-o', '--oneproject', action='store_true', help='show project info')
parser.add_argument('-u', '--usergid', action='store_true', help='show user gid')
parser.add_argument('-t', '--task', action='store_true', help='create task')
parser.add_argument('-l', '--list', action='store_true', help="show user's tasks list")

args = parser.parse_args()

if args.projects:
    asana_obj = APIAsana()
    all_projects = asana_obj.set_projects()
    pprint(all_projects)

if args.oneproject:
    asana_obj = APIAsana()
    project_info = asana_obj.set_project()
    pprint(project_info)

if args.usergid:
    asana_obj = APIAsana()
    user_gid = asana_obj.set_user_gid()
    print(user_gid)

if args.task:
    asana_obj = APIAsana()
    name = input('Task name: ')
    notes = input('Task notes: ')
    send_task = asana_obj.create_task(name=name, notes=notes)

if args.list:
    asana_obj = APIAsana()
    tasks = asana_obj.set_user_tasks()
    if tasks:
        for index, task in enumerate(tasks):
            index += 1
            print(index, task)
    else:
        print('There is no assignment task to you.')