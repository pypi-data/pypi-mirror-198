from pprint import pprint

from startwork.models.GenericProjectActionsModel import GenericProjectActionsModel
from inquirer.errors import ValidationError as InquirerValidationError

class TestGenericProjectActionsModel():
  # CLASS SETUP
  prompt_mock_values = [
    {"name": "sample_name1", "project_path": "/home"},
    {"name": "sample_name2", "project_path": "/home"},
    {"name": "sample_name3", "project_path": "/home"},
  ]

  def _get_error(self, error, current=""):
    if error == "empty":
      return InquirerValidationError("", reason="Project name can't be empty")
    if error == "alredy_used" and len(current) > 1:
      return InquirerValidationError("", reason=f'Name "{current}" alredy in use')
    return InquirerValidationError("", reason=error)

  # TESTS
  def test_raiseError(self):
    error_string = "sample_error"
    try:
      GenericProjectActionsModel._raiseError(error_string)
      assert False
    except Exception as exception:
      expected_exception = self._get_error(error_string)
      assert exception.__module__ == expected_exception.__module__
      assert exception.reason == expected_exception.reason
      assert exception.value == expected_exception.value

  def test_validate_name_happy_path(self, capsys):
    try:
      is_valid_name = GenericProjectActionsModel._validate_name(
        "aa",
        self.prompt_mock_values
      )
      out, err = capsys.readouterr()
      assert out == ""
      assert err == ""
      assert is_valid_name
    except Exception:
      assert False  

  def test_validate_name_string_length(self):
    try:
      GenericProjectActionsModel._validate_name(
        "",
        self.prompt_mock_values
      )
      assert False
    except Exception as exception:
      expected_exception = self._get_error("empty")
      assert exception.__module__ == expected_exception.__module__
      assert exception.reason == expected_exception.reason
      assert exception.value == expected_exception.value

  def test_validate_name_alredy_used(self):
    for prompt_value in self.prompt_mock_values:
      try:
        GenericProjectActionsModel._validate_name(
          prompt_value["name"],
          self.prompt_mock_values
        )
        assert False
      except Exception as exception:
        expected_exception = self._get_error("alredy_used", prompt_value["name"])
        assert exception.__module__ == expected_exception.__module__
        assert exception.reason == expected_exception.reason
        assert exception.value == expected_exception.value
