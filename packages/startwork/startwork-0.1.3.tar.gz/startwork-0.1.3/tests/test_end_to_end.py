from startwork.main import main
from startwork.constants.__version__ import __version__

class TestEndToEnd:
  expected_help_output = f'avaliable options:\n  default: run\n\n  create: create a new project\n\n  delete: delete a project\n\n'

  def test_unkown_option(self, capsys):
    main(["", "--randon_stuff"])
    out, err = capsys.readouterr()
    expeted_help_message = 'Unknown option: --randon_stuff\nTry one of the following:\n'
    assert out == expeted_help_message + self.expected_help_output
    assert err == ''

  def test_help(self, capsys):
    main(["", "--help"])
    out, err = capsys.readouterr()
    assert out == self.expected_help_output
    assert err == ''

  def test_version(self, capsys):
    main(["", "--version"])
    out, err = capsys.readouterr()
    assert out == f'version: {__version__}\n\n'
    assert err == ''
