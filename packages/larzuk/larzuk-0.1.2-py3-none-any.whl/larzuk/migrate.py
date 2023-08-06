import os
import json
import importlib.util
from pathlib import Path
from dataclasses import dataclass
from types import ModuleType, FunctionType

from d2txt import D2TXT


@dataclass
class MigrationContext:
    src_dir: Path
    dest_dir: Path


class MigrationSpec(ModuleType):
    filename: str
    migrate: FunctionType


class Migration:
    name: str
    spec: MigrationSpec
    ctx: MigrationContext

    def __init__(self, name: str, spec: MigrationSpec, ctx: MigrationContext):
        self.name = name
        self.spec = spec
        self.ctx = ctx

    def apply(self):
        dest_path = Path(self.ctx.dest_dir, self.spec.filename)

        if dest_path.exists():
            txt_file = D2TXT.load_txt(dest_path)
        else:
            txt_file = D2TXT.load_txt(Path(self.ctx.src_dir, self.spec.filename))
            dest_path.parent.mkdir(parents=True, exist_ok=True)

        self.spec.migrate(txt_file)

        txt_file.to_txt(dest_path)

        logs = self.read_logs()
        logs.append(self.name)

        self.write_logs(logs)

    def read_logs(self):
        log_file = Path(self.ctx.dest_dir, '.migrate_logs')
        if not log_file.exists():
            log_file.write_text('[]', encoding='utf-8')
            return []

        with log_file.open('r', encoding='utf-8') as fp:
            return json.load(fp)

    def write_logs(self, logs: list[str]):
        log_file = Path(self.ctx.dest_dir, '.migrate_logs')
        with log_file.open('w', encoding='utf-8') as fp:
            json.dump(logs, fp)

    def is_applied(self) -> bool:
        return self.name in self.read_logs()


class MigrationManager:
    base_dir: Path
    ctx: MigrationContext
    migrations: list[Migration]

    def __init__(self, base_dir: Path, ctx: MigrationContext):
        self.base_dir = base_dir
        self.migrations = []

        for filename in filter(lambda f: f[-3:] == '.py', os.listdir(base_dir)):
            spec = importlib.util.spec_from_file_location(filename, Path(base_dir, filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.migrations.append(Migration(filename, module, ctx))
