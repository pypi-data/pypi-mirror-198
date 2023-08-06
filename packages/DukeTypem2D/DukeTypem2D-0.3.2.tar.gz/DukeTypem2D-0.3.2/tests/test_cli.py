from pathlib import Path

from click.testing import CliRunner

from duke_typem.cli import cli

# BASICS


def test_cli_invoke_help(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-h"])
    assert res.exit_code == 0


# CHECK


def test_cli_verbosity(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-v", "check"])
    assert res.exit_code == 0
    res = CliRunner().invoke(cli, ["-vv", "check"])
    assert res.exit_code == 0
    res = CliRunner().invoke(cli, ["-vvv", "check"])
    assert res.exit_code == 0
    res = CliRunner().invoke(cli, ["-vvvv", "check"])
    # 4*V should not further raise the verbosity, but does not fail
    assert res.exit_code == 0


def test_cli_check_nonex_file(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "check", "lubula"])
    assert res.exit_code != 0


def test_cli_check_path(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "check", "."])
    assert res.exit_code == 0


def test_cli_check_invalid_cfg(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "check", "-c", "lubula"])
    assert res.exit_code != 0


def test_cli_check_with_passive_pyproject(tmp_cwd: Path):
    out_path = tmp_cwd / "pyproject.toml"
    with open(out_path, "x", encoding="utf-8-sig") as f_out:
        f_out.write("something = 'Lorem'")
    assert out_path.exists()
    # should not irritate the program
    res = CliRunner().invoke(cli, ["-vvv", "check"])
    assert res.exit_code == 0


def test_cli_check_pyproject_config(tmp_cwd: Path):
    out_path = tmp_cwd / "pyproject.toml"
    with open(out_path, "x", encoding="utf-8-sig") as f_out:
        f_out.write("something = 'Lorem'")
    assert out_path.exists()
    # should not irritate the program
    res = CliRunner().invoke(cli, ["-vvv", "check", "-c", "pyproject.toml"])
    assert res.exit_code != 0


# INIT


def test_cli_init_default(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "init"])
    assert (tmp_cwd / ".DukeTypem2D.yaml").exists()
    assert res.exit_code == 0


def test_cli_init_invalid(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "init", "-s", "pommel"])
    assert res.exit_code != 0


def test_cli_init_default_yaml(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "init", "-s", "yaml"])
    assert (tmp_cwd / ".DukeTypem2D.yaml").exists()
    assert res.exit_code == 0


def test_cli_init_default_toml(tmp_cwd: Path):
    res = CliRunner().invoke(cli, ["-vvv", "init", "-s", "toml"])
    assert (tmp_cwd / ".DukeTypem2D.toml").exists()
    assert res.exit_code == 0
