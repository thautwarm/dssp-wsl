## dssp-wsl

Converting PDB (Protein Data Bank) file format to DSSP file format is required for generating datasets of peptides and their secondary structures.

Such a task should be permitted when using BioPython. However, on Windows, the lack of the program `dssp` stucks everything.

Fortunately, linux distros provide `dssp` or `mkdssp` installation, and Windows Subsystem for Linux is an easy-to-get thing. We hereby provide this simple script to wrap calling `dssp/mkdssp` from `wsl`, and you can install it via:

```
pip install dssp-wsl
```

Other than installing `dssp-wsl` On Windows, you should also install WSL ([see hints](https://docs.microsoft.com/en-us/windows/wsl/install)), and use `sudo apt install dssp` inside the subsystem. Then you rework BioPython.
