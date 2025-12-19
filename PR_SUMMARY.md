# PR Summary: Fix Crash When output/ Directory is Missing

## Issue

Fixes #3 - Program crashed with `FileNotFoundError` when `output/` directory didn't exist.

## Problem

- Code tried to write to `tinytracer/output/` without creating directory first
- Relative imports prevented tests from importing `main.py`
- Optional dependencies (numpy/PIL) blocked basic PPM rendering

## Solution

1. Changed default output paths from `tinytracer/output/` to `output/`
2. Fixed imports to use absolute package paths (`tinytracer.core.*`)
3. Moved numpy/PIL imports to PNG-only branch with error handling
4. Added test to verify directory auto-creation

## Changes Made

- **tinytracer/main.py**: Updated paths, fixed imports, lazy-load dependencies (~15 lines)
- **tinytracer/shapes/material.py**: Fixed imports to use `tinytracer.core.*` (~3 lines)
- **tests/test_output_dir.py**: New test validating the fix (47 lines)

## Testing

```bash
$ pytest -q
.....
5 passed in 0.22s
```

✅ All tests pass (4 existing + 1 new)

## Verification

```bash
# Before: Crashed with FileNotFoundError
# After: Creates output/ and renders successfully
rm -rf output/
python -m tinytracer.main --samples 5
ls -la output/image.ppm  # ✅ File exists
```

## Backward Compatibility

✅ **Fully compatible** - Custom output paths via `--output` flag still work

## Checklist

- [x] Code follows PEP 8
- [x] Commented where needed
- [x] All tests pass (5/5)
- [x] No new warnings
- [x] Tests added for the fix
- [x] No breaking changes
