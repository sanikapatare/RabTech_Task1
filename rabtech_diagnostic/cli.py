import json
import os
import platform
import shutil
import sys
from pathlib import Path


def inspect_environment():
    """Collect system and development environment information."""

    disk = shutil.disk_usage(Path.cwd())

    developer_tools = {}

    tools = ["git", "python", "pip", "code"]

    for tool in tools:
        developer_tools[tool] = shutil.which(tool) is not None

    return {
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "disk_space_gb": round(disk.free / (1024 ** 3), 2),

        # Store only environment variable names,
        # not their private values.
        "environment_variables": sorted(os.environ.keys()),

        "developer_tools": developer_tools,
    }


def load_config(config_path):
    """Load a JSON configuration file."""

    path = Path(config_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {config_path}"
        )

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def create_report(config_path=None):
    """Create the diagnostic report."""

    report = inspect_environment()

    if config_path:
        report["configuration"] = load_config(config_path)

    return report


def print_human_report(report):
    """Display a human-readable report."""

    print("\n===================================")
    print("     RABTECH DIAGNOSTIC REPORT")
    print("===================================")

    print("\nPython Version:", report["python_version"])
    print("Platform:", report["platform"])
    print("Free Disk Space:", report["disk_space_gb"], "GB")

    print("\nDeveloper Tools:")

    for tool, available in report["developer_tools"].items():
        status = "Available" if available else "Missing"
        print(f"- {tool}: {status}")

    print("\nEnvironment Variables:")

    for name in report["environment_variables"]:
        print(f"- {name}")

    if "configuration" in report:
        print("\nConfiguration:")
        print(json.dumps(report["configuration"], indent=2))

    print("\n===================================")
    print("        ANALYSIS COMPLETE")
    print("===================================")


def main():
    """Console entry point."""

    config_path = None
    json_output = False

    args = sys.argv[1:]

    if "--config" in args:
        index = args.index("--config")

        if index + 1 >= len(args):
            print("Error: --config requires a file path.")
            return 2

        config_path = args[index + 1]

    if "--json" in args:
        json_output = True

    try:
        report = create_report(config_path)

    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 2

    except json.JSONDecodeError:
        print("Error: Configuration file contains invalid JSON.")
        return 3

    except Exception as error:
        print(f"Error: {error}")
        return 1

    if json_output:
        print(json.dumps(report, indent=2))
    else:
        print_human_report(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())