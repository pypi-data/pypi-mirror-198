# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=consider-alternative-union-syntax
import sys
from pathlib import Path

import pytest
from pydantic.dataclasses import dataclass

from application_settings import SettingsBase, SettingsSectionBase

if sys.version_info < (3, 10):
    from typing import Union


@dataclass(frozen=True)
class AnExample1SettingsSection(SettingsSectionBase):
    """Example 1 of a Settings section"""

    setting1: str = "setting1"
    setting2: int = 2


@dataclass(frozen=True)
class AnExample1Settings(SettingsBase):
    """Example Settings"""

    section1: AnExample1SettingsSection = AnExample1SettingsSection()


def test_paths() -> None:
    # default_filepath:
    if the_path := AnExample1Settings.default_filepath():
        assert the_path.parts[-1] == "settings.toml"
        assert the_path.parts[-2] == ".an_example1"
    else:
        assert False


def test_update(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    if sys.version_info >= (3, 10):

        def mock_default_filepath() -> Path | None:
            return None

    else:

        def mock_default_filepath() -> Union[Path, None]:
            return None

    monkeypatch.setattr(AnExample1Settings, "default_filepath", mock_default_filepath)
    AnExample1Settings.set_filepath("")
    assert AnExample1Settings.get(reload=True).section1.setting1 == "setting1"
    assert AnExample1Settings.get().section1.setting2 == 2
    with pytest.raises(RuntimeError):
        new_settings = AnExample1Settings.get().update(
            {"section1": {"setting1": "new s1", "setting2": 222}}
        )
    tmp_filepath = (
        tmp_path
        / AnExample1Settings.default_foldername()
        / AnExample1Settings.default_filename()
    )
    AnExample1Settings.set_filepath(tmp_filepath)
    new_settings = AnExample1Settings.get().update(
        {"section1": {"setting1": "new s1", "setting2": 222}}
    )

    assert new_settings.section1.setting1 == "new s1"
    assert AnExample1Settings.get().section1.setting2 == 222


def test_update_json(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    if sys.version_info >= (3, 10):

        def mock_default_filepath() -> Path | None:
            return None

    else:

        def mock_default_filepath() -> Union[Path, None]:
            return None

    monkeypatch.setattr(AnExample1Settings, "default_filepath", mock_default_filepath)
    AnExample1Settings.set_filepath("")
    assert AnExample1Settings.get(reload=True).section1.setting1 == "setting1"
    assert AnExample1Settings.get().section1.setting2 == 2
    tmp_filepath = (
        tmp_path
        / AnExample1Settings.default_foldername()
        / AnExample1Settings.default_filename().replace("toml", "json")
    )
    AnExample1Settings.set_filepath(tmp_filepath)
    new_settings = AnExample1Settings.get().update(
        {"section1": {"setting1": "new s1a", "setting2": 333}}
    )

    assert new_settings.section1.setting1 == "new s1a"
    assert AnExample1Settings.get().section1.setting2 == 333


def test_update_ini(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capfd: pytest.CaptureFixture[str]
) -> None:
    if sys.version_info >= (3, 10):

        def mock_default_filepath() -> Path | None:
            return None

    else:

        def mock_default_filepath() -> Union[Path, None]:
            return None

    monkeypatch.setattr(AnExample1Settings, "default_filepath", mock_default_filepath)
    AnExample1Settings.set_filepath("")
    assert AnExample1Settings.get(reload=True).section1.setting1 == "setting1"
    assert AnExample1Settings.get().section1.setting2 == 2
    tmp_filepath = (
        tmp_path
        / AnExample1Settings.default_foldername()
        / AnExample1Settings.default_filename().replace("toml", "ini")
    )
    AnExample1Settings.set_filepath(tmp_filepath)
    new_settings = AnExample1Settings.get().update(
        {"section1": {"setting1": "new s1a", "setting2": 333}}
    )

    # new settings have been applied but not stored to file
    assert new_settings.section1.setting1 == "new s1a"
    assert AnExample1Settings.get().section1.setting2 == 333
    captured = capfd.readouterr()
    assert "Unknown file format ini given in" in captured.out
    assert AnExample1Settings.get(reload=True).section1.setting1 == "setting1"
    assert AnExample1Settings.get().section1.setting2 == 2
