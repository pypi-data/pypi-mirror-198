import os
from pathlib import Path

import click
from larzuk.migrate import MigrationManager, MigrationContext


@click.command('up')
@click.option('--data-dir', help='Data directory of Diablo II: Resurrected.', type=click.Path(file_okay=False, exists=True), required=True)
@click.option('--migration-dir', help='Directory of migration scripts.', type=click.Path(file_okay=False, exists=True), required=False, default=Path(os.getcwd(), 'migrations'))
@click.option('--output-dir', help='Output directory.', type=click.Path(file_okay=False, exists=False), required=True, default=Path(os.getcwd(), 'output'))
def up_command(data_dir: Path, migration_dir: Path, output_dir: Path):
    """Apply migrations"""

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    mm = MigrationManager(base_dir=migration_dir, ctx=MigrationContext(src_dir=data_dir, dest_dir=output_dir))

    for migration in mm.migrations:
        if migration.is_applied():
            click.echo(f'[SKIP] {migration.name} already applied.')
            continue

        migration.apply()

        click.echo(f'[DONE] {migration.name} applied.')
