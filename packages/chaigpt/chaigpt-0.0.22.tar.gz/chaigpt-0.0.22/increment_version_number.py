from sys import exit

def increment_version_number():
    lines = None
    with open("pyproject.toml") as f:
        lines = f.readlines()
    
    if lines is None:
        return False
        
    n = -1
    for i, line in enumerate(lines):
        if line.startswith("version"):
            n = i
            break

    if n == -1:
        return False
    
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

    with open("pyproject.toml", "w") as f:
        f.write("".join(lines))
        return True


def main():
    if not increment_version_number():
        print("Error incrementing version number")


if __name__ == "__main__":
    exit(main())

