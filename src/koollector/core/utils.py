"""Various utility functions for Koolector."""

import datetime
from pathlib import Path


def get_timestamp() -> datetime.datetime:
    """Get datetime timestamp in utc timezone."""
    return datetime.datetime.now(tz=datetime.UTC)


def make_output_path(profile, *, dir_override: Path | None = None, **kwargs) -> Path:
    """Generate output path based on profile and optional directory override."""

    output_dir = dir_override or profile.output.directory or Path.cwd()
    return output_dir / profile.output.filename_template.format(
        source_name=Path(kwargs.get("source", "")).stem,
        format=profile.output.output_format,
        created_at=get_timestamp(),
    )


def write_output(path: Path, content: str) -> None:
    """Write content to the specified path, creating parent directories if needed."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
