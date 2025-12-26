import shutil
import sys
import ast
import os
from pathlib import Path

SRC_DIR = Path("src/algorithms")
BACKUP_DIR = Path(".practice_backup")
GIT_HOOKS_DIR = Path(".git/hooks")
PRE_COMMIT_HOOK = GIT_HOOKS_DIR / "pre-commit"


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


def install_git_hook():
    """Install a pre-commit hook to prevent commits during practice mode"""
    if not GIT_HOOKS_DIR.exists():
        return  # Not a git repo or .git doesn't exist

    hook_start_marker = "# BEGIN Practice mode protection"
    hook_end_marker = "# END Practice mode protection"
    hook_content = f"""{hook_start_marker}
if [ -d ".practice_backup" ]; then
    echo "❌ Cannot commit while practice mode is enabled!"
    echo "   Run 'python scripts/practice_mode.py off' to disable practice mode first."
    exit 1
fi
{hook_end_marker}
"""
    GIT_HOOKS_DIR.mkdir(parents=True, exist_ok=True)

    # Check if hook already exists
    if PRE_COMMIT_HOOK.exists():
        existing_content = PRE_COMMIT_HOOK.read_text()
        # If our marker is already there, remove old section first
        if hook_start_marker in existing_content:
            lines = existing_content.split("\n")
            new_lines = []
            skip_section = False
            for line in lines:
                if hook_start_marker in line:
                    skip_section = True
                    continue
                if hook_end_marker in line:
                    skip_section = False
                    continue
                if not skip_section:
                    new_lines.append(line)
            content = "\n".join(new_lines).rstrip() + "\n\n" + hook_content
        else:
            # Append our check to existing hook
            content = existing_content.rstrip() + "\n\n" + hook_content
    else:
        # Create new hook with shebang
        content = "#!/bin/sh\n\n" + hook_content

    with open(PRE_COMMIT_HOOK, "w") as f:
        f.write(content)
    os.chmod(PRE_COMMIT_HOOK, 0o755)


def remove_git_hook():
    """Remove the practice mode pre-commit hook section"""
    if not PRE_COMMIT_HOOK.exists():
        return

    hook_start_marker = "# BEGIN Practice mode protection"
    hook_end_marker = "# END Practice mode protection"

    content = PRE_COMMIT_HOOK.read_text()
    if hook_start_marker not in content:
        return  # Our hook section not present

    lines = content.split("\n")
    new_lines = []
    skip_section = False
    for line in lines:
        if hook_start_marker in line:
            skip_section = True
            continue
        if hook_end_marker in line:
            skip_section = False
            continue
        if not skip_section:
            new_lines.append(line)

    # Remove trailing empty lines
    while new_lines and not new_lines[-1].strip():
        new_lines.pop()

    if new_lines:
        # Write back the hook without our section
        PRE_COMMIT_HOOK.write_text("\n".join(new_lines) + "\n")
    else:
        # Hook is empty, remove it
        PRE_COMMIT_HOOK.unlink()


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

    install_git_hook()

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
    remove_git_hook()
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
