import pytest
import unittest
from unittest.mock import patch

from copy import deepcopy, copy
from pathlib import Path
import json

from startwork.models.CreateProject import CreateProject

prompt_mock_values = [
  {"name": "sample_name1", "project_path": "/home"},
  {"name": "sample_name2", "project_path": "/home"},
  {"name": "sample_name3", "project_path": "/home"},
]

class TestCreateProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"
  prompt_mock_values = deepcopy(prompt_mock_values)

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(CreateProject.run)

  @patch(
    "startwork.models.CreateProject.prompt",
    return_value=prompt_mock_values[0]
  )
  def test_happy_path(self, mock_inquirer_prompt):
    for prompt_value in prompt_mock_values:
      mock_inquirer_prompt.return_value["name"] = copy(prompt_value["name"])
      mock_inquirer_prompt.return_value["project_path"] = copy(prompt_value["project_path"])

      CreateProject.run(self.project_list_path)
      out, err = self.capsys.readouterr()
      assert out == "New project created!\n"
      assert err == ""

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == prompt_mock_values

    # clean json for the next test 
    with open(self.project_list_path, "w") as outfile:
      outfile.write(json.dumps([], indent=4))

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == []
