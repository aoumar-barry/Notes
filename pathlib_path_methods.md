
# 🛠️ pathlib.Path — 30 Most Useful Methods

## 🔟 Basic Methods

1. `path.exists()` — Check if the file or directory exists.
2. `path.is_file()` — Check if it’s a file.
3. `path.is_dir()` — Check if it’s a directory.
4. `path.mkdir(parents=True, exist_ok=True)` — Create directory.
5. `path.unlink()` — Remove a file.
6. `path.rmdir()` — Remove an empty directory.
7. `list(path.iterdir())` — List contents of a directory.
8. `path.read_text()` — Read text from a file.
9. `path.write_text("Hello")` — Write text to a file.
10. `path.read_bytes()` — Read binary content from a file.

## 🔟 Intermediate Usage

11. `path.write_bytes(b"data")` — Write binary content.
12. `path / "file.txt"` — Join paths using `/`.
13. `path.name` — Get file name.
14. `path.suffix` — Get file extension.
15. `path.parent` — Get the parent directory.
16. `path.is_absolute()` — Check if path is absolute.
17. `path.absolute()` — Get absolute path.
18. `path.resolve()` — Resolve symlinks to real path.
19. `path.parts` — Get path components as a tuple.
20. `path.stem` — Get filename without extension.

## 🔟 Advanced Techniques

21. `path.with_suffix(".md")` — Change the file extension.
22. `path.with_name("new.txt")` — Change file name.
23. `path.joinpath("folder", "file.txt")` — Join path segments.
24. `path.is_relative_to(Path("base"))` — Check if path is relative to another.
25. `path.relative_to(Path("base"))` — Get relative path.
26. `path.rename("new.txt")` — Rename the file.
27. `path.replace("backup.txt")` — Replace file with another.
28. `path.match("*.txt")` — Match filename pattern.
29. `path.glob("*.py")` — Glob pattern in a directory.
30. `path.rglob("*.py")` — Recursive glob in all subdirectories.

file_path = Path("/mnt/data/python_syllabus_zero_to_hero.md")
file_path.write_text(python_syllabus_md)

file_path.name