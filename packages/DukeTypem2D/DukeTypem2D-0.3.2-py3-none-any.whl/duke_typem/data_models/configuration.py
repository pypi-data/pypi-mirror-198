from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

import toml
import yaml
from pydantic import BaseModel
from pydantic import validator

from .logger import logger


class Configuration(BaseModel):
    language: str = "en"

    eol_linux: bool = True
    autofix: bool = False

    project_path: str = "."  # must be valid file or dir
    exclude_paths: List[str] = []  # list of valid files or dir
    types: List[str] = ["md", "rst", "html", "txt"]

    class Config:  # of the data-model itself
        allow_mutation = True  # const after creation?
        extra = "forbid"  # no unnamed attributes allowed
        validate_all = True  # also check defaults
        validate_assignment = True

    @validator(
        "project_path",
        "exclude_paths",
        always=True,
        pre=False,
    )
    def path_existing(cls, v: Union[List[str], str], field: str):  # noqa: N805
        if isinstance(v, str):
            values = [v]
        elif isinstance(v, list):
            values = v
        else:
            raise TypeError("Type not supported")
        for value in values:
            _dir = Path(value)
            if not _dir.exists():
                raise ValueError(f"{field} must exist (is set to '{value}')")
        return v

    @classmethod
    def parse_file(cls, file: Optional[Path]):
        file_orig = file
        if file is None:
            for substitute in [
                Path(".DukeTypem2D.yaml"),
                Path(".DukeTypem2D.toml"),
                Path("pyproject.toml"),
            ]:
                if substitute.exists():
                    file = substitute
                    break
        if file is None:
            return Configuration()
        file = Path(file)
        if not file.exists() or not file.is_file():
            raise ValueError(file)
        with open(file) as f:
            if file.suffix.lower() in [".yaml", ".yml"]:
                config = yaml.safe_load(f)
            elif file.suffix.lower() in [".toml"]:
                config = toml.load(f)
                if file.stem.lower() == "pyproject":
                    if "tool" in config and "DukeTypem2D" in config["tool"]:
                        config = config["tool"]["DukeTypem2D"]
                    elif "pyproject.toml" in str(file_orig).lower():
                        raise ValueError(
                            "pyproject.toml did not contain a valid config"
                        )
                    else:
                        return Configuration()
            else:
                raise TypeError("Config has to be TOML or YAML")
        logger.info("Duke-Config parsed from '%s'", file)
        logger.debug(
            "%s",
            yaml.safe_dump(config, default_flow_style=False, sort_keys=False),
        )
        return Configuration.parse_obj(config)

    def to_file(self, file: Path, style: str, version: str):
        if not isinstance(style, str):
            raise ValueError("Output-format must be provided as string")
        out_path = Path(file).with_suffix("." + style)
        if out_path.exists():
            raise FileExistsError("File '%s' already exists!", out_path)

        logger.debug("Will write config to '%s'", out_path)
        with open(out_path, "x", encoding="utf-8-sig") as f_out:
            f_out.write(
                f"# this is the default configuration (v{version}) - "
                "unchanged entries can be omitted",
            )

            if style.lower() == "yaml":
                yaml.safe_dump(
                    self.dict(), f_out, default_flow_style=False, sort_keys=False
                )
            elif style.lower() == "toml":
                toml.dump(self.dict(), f_out)
            else:
                raise TypeError("Output-format '%s' not implemented", style)
