import pytest
import unittest
from unittest.mock import patch

from copy import deepcopy, copy
from pathlib import Path
import json

from startwork.models.CreateProject import CreateProject
from startwork.models.DeleteProject import DeleteProject


mock_values_create = [
  {"name": "sample_name1", "project_path": "/home"},
  {"name": "sample_name2", "project_path": "/home"},
  {"name": "sample_name3", "project_path": "/home"},
]

mock_values_delete = [{
  "selected_project": value_create["name"],
  "delete_confirmed": True,
  "delete_confirmed2": True,
} for value_create in mock_values_create ]

mock_values_delete_unconfirmed = [
  {
    "selected_project": mock_values_create[0]["name"],
    "delete_confirmed": False,
    "delete_confirmed2": False,
  },
  {
    "selected_project": mock_values_create[0]["name"],
    "delete_confirmed": False,
    "delete_confirmed2": True,
  },
  {
    "selected_project": mock_values_create[0]["name"],
    "delete_confirmed": True,
    "delete_confirmed2": False,
  }
]

class TestDeleteProject(unittest.TestCase):
  # CLASS SETUP
  project_list_path = Path(__file__).parent / "projects_list.json"
  mock_values_create = deepcopy(mock_values_create)
  generic_error_exception = Exception("Deletion Aborted!")

  @pytest.fixture(autouse=True)
  def _capsys(self, capsys):
    self.capsys = capsys

  # TESTS
  def test_if_is_function(self):
    assert callable(DeleteProject.run)

  @patch(
    "startwork.models.CreateProject.prompt",
    return_value=mock_values_create[0]
  )
  @patch(
    "startwork.models.DeleteProject.prompt",
    return_value=mock_values_delete[0]
  )
  def test_happy_path(
    self,
    mock_inquirer_prompt_delete,
    mock_inquirer_prompt_create
  ):
    # set json for the test
    for prompt_value in mock_values_create:
      mock_inquirer_prompt_create.return_value["name"] = copy(prompt_value["name"])
      mock_inquirer_prompt_create.return_value["project_path"] = copy(prompt_value["project_path"])

      CreateProject.run(self.project_list_path)

    with open(self.project_list_path, "r") as file:
      result = json.load(file)
      assert result == mock_values_create
    # clean output
    self.capsys.readouterr()

    # do the test it self
    expected_result = mock_values_create
    for prompt_value in mock_values_delete:
      project_name = prompt_value["selected_project"]
      mock_inquirer_prompt_delete.return_value["selected_project"] = copy(project_name)

      DeleteProject.run(self.project_list_path)

      out, err = self.capsys.readouterr()
      assert out == f'Project named as "{project_name}" has been deleted!\n'
      assert err == ""
      # asset comparing array removing each item at time
      with open(self.project_list_path, "r") as file:
        expected_result = list(
          filter(
            lambda mock_value: mock_value["name"] != project_name,
            expected_result
          )
        )
        result = json.load(file)
        assert result == expected_result


  @patch(
    "startwork.models.CreateProject.prompt",
    return_value=mock_values_create[0]
  )
  @patch(
    "startwork.models.DeleteProject.prompt",
    return_value=mock_values_delete_unconfirmed[0]
  )
  def test_delete_unconfirmed(
    self,
    mock_inquirer_prompt_delete,
    mock_inquirer_prompt_create
  ):
    CreateProject.run(self.project_list_path)
    with open(self.project_list_path, "r") as file:
      result = json.load(file)
      assert result == [mock_values_create[0]]
    # clean output
    self.capsys.readouterr()

    for mock_value in mock_values_delete_unconfirmed:
      mock_inquirer_prompt_delete.return_value["delete_confirmed"] = mock_value["delete_confirmed"]
      mock_inquirer_prompt_delete.return_value["delete_confirmed2"] = mock_value["delete_confirmed2"]
      try:
        DeleteProject.run(self.project_list_path)
        assert False
      except Exception as exception:
        assert exception.args == self.generic_error_exception.args

    with open(self.project_list_path, "w") as outfile:
      outfile.write(json.dumps([], indent=4))

    with open(self.project_list_path, "r") as file:
      assert json.load(file) == []
