from argparse import Namespace
from pathlib import Path
import shutil
import os

from tinytracer.main import main


def test_output_directory_is_created_and_file_written():
    out_dir = Path("output")
    out_file = out_dir / "image.ppm"

    # Ensure a clean start
    if out_dir.exists():
        shutil.rmtree(out_dir)

    assert not out_dir.exists()

    args = Namespace(format="ppm", width=20, height=10, samples=1, output="DEFAULT", depth=1, aspectratio=None)

    try:
        main(args)
        assert out_file.exists()
        # file should be non-empty
        assert out_file.stat().st_size > 0
    finally:
        # cleanup
        if out_dir.exists():
            shutil.rmtree(out_dir)
