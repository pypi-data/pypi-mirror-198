import sys
from pathlib import Path
from subprocess import check_call

from .models.SelectProject import SelectProject
from .models.CreateProject import CreateProject
from .models.DeleteProject import DeleteProject
from .constants.__version__ import __version__

project_list_path = Path(__file__).parent / "projects_list.json"
scripts_path = Path(__file__).parent / "scripts" / "work.sh"

def get_help():
  print("avaliable options:") 
  print("  default: run\n")  
  print("  create: create a new project\n") 
  print("  delete: delete a project\n") 

def main(argv=sys.argv) -> int:
  if len(argv) < 2:
    selected_project = SelectProject.run(project_list_path)
    start_work_script = [scripts_path, selected_project["project_path"]]
    requirementsPath = Path('requirements.txt')

    print("is file?")
    print(requirementsPath.is_file())
    if requirementsPath.is_file():
      for line in open('requirements.txt'):
        requirement_name = line.split("=")
        if requirement_name == "flask":
          start_work_script.append("flask")
          break

    check_call(start_work_script)
    return


  option = argv[1]

  if option == "create":
    return CreateProject.run(project_list_path)

  if option == "delete":
    return DeleteProject.run(project_list_path)

  if option == "--version":
    print(f'version: {__version__}\n')  
    return 0

  if option == "--help":
    get_help()
    return 0
  
  print(f'Unknown option: {option}')
  print('Try one of the following:')
  get_help()
  return 1


if __name__ == "__main__":
  main(sys.argv)
