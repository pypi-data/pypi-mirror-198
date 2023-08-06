import json
from os import getcwd
from inquirer import Text, Path, prompt
from .GenericProjectActionsModel import GenericProjectActionsModel

class CreateProject(GenericProjectActionsModel):
  @staticmethod
  def run(project_list_path):
    projects_list = []

    with open(project_list_path, 'r') as openfile:
      projects_list = json.load(openfile)

    questions = [
      Text(
        'name',
        message="What's the project name?",
        validate=lambda answers, current: CreateProject._validate_name(
          current,
          projects_list
        )
      ),
      Path(
        'project_path',
        message="Where is the project located?",
        path_type=Path.DIRECTORY,
        exists=True,
        normalize_to_absolute_path=True,
        default=getcwd()
      ),
    ]

    new_project = prompt(questions)
    if new_project:
      projects_list.append(new_project)

    with open(project_list_path, "w") as outfile:
      outfile.write(json.dumps(projects_list, indent=4))

    if new_project:
      print("New project created!")
