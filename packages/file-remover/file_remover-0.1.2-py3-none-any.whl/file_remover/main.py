import argparse
from pathlib import Path

from rich.console import Console
from rich.progress import Progress
from rich.table import Table


def main():
    # Get filepath
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_path",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Path to folder, where files should be rmoved",
    )
    p = parser.parse_args()
    TARGET_PATH = p.file_path

    console = Console()
    table = Table()
    table.add_column("#")
    table.add_column("File", style="blue")

    with console.status("[bold green]Reading files..."):
        pathlist = TARGET_PATH.rglob("._*")

    pathlist = [file for file in pathlist]
    for i, file in enumerate(pathlist):
        table.add_row(str(i), file.name)

    console.print(table)
    input_res = input("Delete files? [y/N]: ")

    if input_res.lower() == "y":
        with Progress() as progress:
            task = progress.add_task(description="[red]Deleting files", total=100)
            step = 100 / len(pathlist)

            for file in pathlist:
                try:
                    file.unlink()
                    progress.update(task, advance=step)
                    progress.console.print(f"[bold]{file.name} [green]is deleted ✅")
                except:
                    progress.update(task, advance=step)
                    progress.console.print(f"{file.name} [red]not deleted ❌")


if __name__ == "__main__":
    main()
