import shutil
import sys
import ast
from pathlib import Path

SRC_DIR = Path("src/algorithms")
BACKUP_DIR = Path(".practice_backup")


def create_stub_from_file(filepath):
    """Extract function signatures and create pass stubs (excluding private helpers)"""
    with open(filepath, "r") as f:
        content = f.read()

    tree = ast.parse(content)
    functions = []

    # Walk the tree and collect functions in order
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Skip private helper functions (they give hints away)
            if node.name.startswith("_"):
                continue

            args = [arg.arg for arg in node.args.args]
            sig = f"def {node.name}({', '.join(args)}):"

            # Extract docstring if present
            docstring = ast.get_docstring(node)

            functions.append((node.lineno, sig, docstring))

    # Sort by line number to preserve order
    functions.sort(key=lambda x: x[0])

    stubs = []
    for _, sig, docstring in functions:
        stub = f"{sig}\n"
        if docstring:
            # Format docstring with proper indentation (ast.get_docstring already dedents)
            lines = docstring.split("\n")
            if len(lines) == 1:
                # Single line docstring
                stub += f'    """{lines[0]}"""\n'
            else:
                # Multi-line docstring - add 4 spaces indentation to each line
                stub += '    """\n'
                for line in lines:
                    if line:  # Non-empty line
                        stub += f"    {line}\n"
                    else:  # Empty line - no trailing spaces
                        stub += "\n"
                stub += '    """\n'
        stub += "    pass\n"
        stubs.append(stub)

    return "\n".join(stubs) if stubs else "# TODO: Implement\n    pass\n"


def enable_practice_mode():
    """Backup current solutions and replace with stubs"""
    if BACKUP_DIR.exists():
        print("⚠️  Practice mode already enabled! Run 'practice-mode off' first.")
        return

    BACKUP_DIR.mkdir(exist_ok=True)
    backed_up = 0

    # Find all Python files (except __init__.py)
    for py_file in SRC_DIR.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue

        # Backup original
        rel_path = py_file.relative_to(SRC_DIR)
        backup_path = BACKUP_DIR / rel_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(py_file, backup_path)

        # Create stub
        stub_content = create_stub_from_file(py_file)
        with open(py_file, "w") as f:
            f.write(stub_content)

        backed_up += 1

    print(f"✅ Practice mode enabled! {backed_up} solution(s) backed up and stubbed.")
    print("   Implement your solutions and run: pytest")


def disable_practice_mode():
    """Restore solutions from backup"""
    if not BACKUP_DIR.exists():
        print("⚠️  Practice mode not enabled!")
        return

    restored = 0

    # Restore all files
    for backup_file in BACKUP_DIR.rglob("*.py"):
        rel_path = backup_file.relative_to(BACKUP_DIR)
        target = SRC_DIR / rel_path
        shutil.copy2(backup_file, target)
        restored += 1

    # Clean up
    shutil.rmtree(BACKUP_DIR)
    print(f"✅ Practice mode disabled! {restored} solution(s) restored.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/practice_mode.py [on|off]")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "on":
        enable_practice_mode()
    elif cmd == "off":
        disable_practice_mode()
    else:
        print("Usage: python scripts/practice_mode.py [on|off]")
