# Datgat

A Python script that recursively scans the Windows `C:\` drive and copies target file types (pictures and documents) into a local `Stolendata` folder.

## Features

- Scans the entire `C:\` drive for matching files.
- **Pictures copied:** `.jpg`, `.jpeg`, `.png`
- **Documents copied:** `.pdf`, `.docx`, `.doc`
- **Skips common system and application directories by default:**
  - `C:\Windows\`
  - `\All Users\`
  - `\Public\`
  - `C:\ProgramData\`
  - `C:\Program Files`
  - `\AppData\`
- **Custom Exclusions:** Supports reading additional excluded directories from a file named `excdir`. If `excdir` is not present, it will be automatically created with the standard excludes only.

## Usage

### Windows Command Line
You can launch the script using the provided batch file:
```cmd
launch.cmd
```
This will run the Python script and wait for you to hit ENTER upon completion.

### Direct Execution
Alternatively, you can run the script directly using Python:
```bash
python3 datgat.py
```

## How It Works
When you run the script, it first identifies all available folders on the `C:\` drive and then finds all the files within those directories. It checks each file against a set of exclusion directories (defined in the script and the `excdir` file).

If a file matches the target picture or document extensions and is not in an excluded directory, it will be copied to a local `Stolendata{id}` folder that the script creates in its own directory, separating the copied files into `Pics` and `Docs` subdirectories.

## Disclaimer
This script copies personal files from your computer and saves them to a folder locally. Ensure you use this software responsibly.
