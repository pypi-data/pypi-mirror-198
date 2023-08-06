#!/usr/bin/env python3

import nbformat
import subprocess
import argparse

# Create an argument parser object
parser = argparse.ArgumentParser(
    description="Convert markdown cells in a jupyter notebook with pandoc"
)
# Add an input file argument
parser.add_argument("input_file", help="The name of the input notebook file")
# Add an output file argument with no default value
parser.add_argument(
    "-o", "--output_file", help="The name of the output notebook file", default=None
)
# Add a clean flag argument with a default value of False
parser.add_argument(
    "--clean",
    help="Clean the markdown cells with pandoc conversions",
    action="store_true",
)
# Add a latex flag argument with a default value of False
parser.add_argument(
    "--latex", help="Convert the output to latex format", action="store_true"
)
# Parse the arguments
args = parser.parse_args()


def clean_markdown(nb: nbformat):
    """Read the input notebook and convert all markdown cells
    into a clean markdown without html tags"""
    # Loop through the cells and transform markdown cells with pandoc if clean is True

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            # Run a pandoc command to convert markdown to html
            html = subprocess.run(
                ["pandoc", "-f", "markdown", "-t", "html", "-o", "-"],
                input=cell.source.encode(),
                capture_output=True,
            )
            result = subprocess.run(
                ["pandoc", "-f", "html", "-t", "gfm-raw_html", "-o", "-"],
                input=html.stdout,
                capture_output=True,
            )
            # Replace the cell source with the transformed text
            cell.source = result.stdout.decode()

    return nb


def main():
    print("Hello from jupytercor !")
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")

    # Read the input notebook file from the input_file argument
    nb = nbformat.read(args.input_file, as_version=4)
    if args.clean:
        print("Démarrage du nettoyage...")
        nb = clean_markdown(nb)
        # Write the output notebook file in the same file as the input file if output_file is None or in a different file otherwise
        if args.output_file is None:
            nbformat.write(nb, args.input_file)
        else:
            nbformat.write(nb, args.output_file)
        print("Nettoyage effectué avec succès !")



if __name__ == "__main__":
    main()
