import json
from inquirer import List, prompt

from .GenericProjectActionsModel import GenericProjectActionsModel

class SelectProject(GenericProjectActionsModel):
  @staticmethod
  def run(project_list_path):
    projects_list = []

    with open(project_list_path, 'r') as openfile:
      projects_list = json.load(openfile)
    
    projects_keys=[project["name"] for project in projects_list]

    questions = [
      List(
        'selected_project',
        message="Selete a project to work on",
        choices=projects_keys,
      )
    ]

    selected_project_name = prompt(questions)["selected_project"]
    SelectProject._validate_selected_project_name(selected_project_name)

    print(f'Starting to work on "{selected_project_name}"')

    selected_project = list(
      filter(
        lambda project: project['name'] == selected_project_name,
        projects_list
      )
    )[0]
    return selected_project
