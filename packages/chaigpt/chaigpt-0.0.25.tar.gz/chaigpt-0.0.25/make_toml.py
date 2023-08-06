from sys import exit, argv
from os.path import join, split

def main():
    lines = None
    with open("pyproject.toml") as f:
        lines = f.readlines()
    
    # First increment version number
    
    if lines is None:
        return -1
        
    n = -1
    for i, line in enumerate(lines):
        if line.startswith("version"):
            n = i
            break

    if n == -1:
        return -1
    
    line = lines[n]
    l = len(line)
    r = list(line)
    r.reverse()
    i0 = l - r.index(".")
    i1 = l - r.index("\"") - 1
    version = int(line[i0:i1])
    version += 1
    line = line[:i0] + str(version) + line[i1:]
    lines = lines[:n] + [line] + lines[n + 1:]

    # Now parse requirements.txt into make_toml.py

    dependencies = []
    with open(join(split(argv[0])[0], "requirements.txt")) as reqs_file:
        dependencies = reqs_file.readlines()

    a = None
    for i, line in enumerate(lines):
        if line.startswith("dependencies"):
            a = i
        if line.startswith("]") and a is not None:
            b = i
            break

    if a is None:
        return False
    
    result = lines[:a + 1]
    for dependency in dependencies:
        tokens = dependency.split("==")
        # if tokens[0] == "unicode_slugify":
        #     tokens[0] = "python_slugify"
        #     tokens[1] = "7.0.0"
        result += [f"    \"{tokens[0]}>={tokens[1].strip()}\",\n"]
    
    result += lines[b:]

    with open(join(split(argv[0])[0], "pyproject.toml"), "w") as f:
        f.write("".join(result))
        return True


if __name__ == "__main__":
    exit(main())

