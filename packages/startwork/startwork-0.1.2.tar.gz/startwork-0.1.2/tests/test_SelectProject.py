import pytest
import unittest
from unittest.mock import patch

from pathlib import Path
import json

from startwork.models.CreateProject import CreateProject
from startwork.models.SelectProject import SelectProject

prompt_mock_values = [
  {"name": "sample_name", "project_path": "/home"},
]

prompt_mock_selected_project_values = [
  {"selected_project": prompt_mock_values[0]["name"]}
]

class TestCreateProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(SelectProject.run)

  @patch(
    "startwork.models.CreateProject.prompt",
    return_value=prompt_mock_values[0]
  )
  @patch(
    "startwork.models.SelectProject.prompt",
    return_value=prompt_mock_selected_project_values[0]
  )
  def test_happy_path(
    self,
    mock_inquirer_prompt_select,
    mock_inquirer_prompt_create
  ):
    # set json for the test
    CreateProject.run(self.project_list_path)
    with open(self.project_list_path, "r") as file:
      result = json.load(file)
      assert result == prompt_mock_values
    # clean output
    self.capsys.readouterr()

    # do the test it self
    expected_project = prompt_mock_values[0]
    selected_project = SelectProject.run(self.project_list_path)
    assert selected_project == expected_project

    # clean json for the next test 
    with open(self.project_list_path, "w") as outfile:
      outfile.write(json.dumps([], indent=4))

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == []
