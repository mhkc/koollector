import click

@click.command()
@click.option("-c", "--config", "config_file", type=click.Path(exists=True), help="Path to the configuration file.")
@click.option("-o", "--output-dir", "output_dir", type=click.Path(exists=True), help="Path to the output directory.")
def main(config_file, output_dir):
    print(f"Using configuration file: {config_file}")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()
