# Python-asana

Create tasks using API Asana.

# Virtual Enviroment

Create a virtual environment:  
`python3.8 -m venv venv`

To activate a venv:  
`source venv/bin/activate`



## Set up

Copy `.env.example` and rename to `.env` (linux command: `mv .env.example .env`)  
and set enviroment variables.

To get the token follow this [steps](https://asana.com/guide/help/api/api).  

Now you may use command `python main.py --help`. It will return:

```python
usage: main.py [-h] [-p] [-o] [-t]

Create your tasks in Asana using API Asana.

optional arguments:
  -h, --help        show this help message and exit
  -p, --projects    Show all projects
  -o, --oneproject  Show project info
  -t, --task        Create task
```

Steps:  
`python main.py -p` and copy the gid of the project you want. Then paste it to `.env` ASANA_PROJECT_GID. 
  
`python main.py -o` and copy the gid of workspace, after that paste it to `.env` ASANA_WORKSPACE_GID.  

`python main.py -t` input name and notes to create a task.
 


