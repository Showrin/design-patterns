from typing import List


class Migration:
    id = None

    def __init__(self, id):
        self.id = id

    def upgrade(self):
        print(f"Upgrading Migration id: {self.id}")

    def downgrade(self):
        print(f"Downgrading Migration id: {self.id}")


class MigrationHistory:
    migrations: List[Migration] = []
    last_executed_migration_id = None

    def add_migration(self, migration: Migration):
        self.migrations.append(migration)

    def downgrade_to(self, id):
        for idx, migration in enumerate(reversed(self.migrations)):
            migration.downgrade()
            self.last_executed_migration_id = self.migrations[idx -
                                                              1] if idx else None

            if migration.id == id:
                break

    def upgrade_all(self):
        for migration in self.migrations:
            migration.upgrade()
            self.last_executed_migration_id = migration.id


migration_history = MigrationHistory()

migration_1 = Migration(1)
migration_2 = Migration(2)
migration_3 = Migration(3)
migration_4 = Migration(4)

migration_history.add_migration(migration_1)
migration_history.add_migration(migration_2)
migration_history.add_migration(migration_3)
migration_history.add_migration(migration_4)

migration_history.upgrade_all()

print("------------------------")

migration_history.downgrade_to(1)

# Output
# Upgrading Migration id: 1
# Upgrading Migration id: 2
# Upgrading Migration id: 3
# Upgrading Migration id: 4
# ------------------------
# Downgrading Migration id: 4
# Downgrading Migration id: 3
# Downgrading Migration id: 2
# Downgrading Migration id: 1
