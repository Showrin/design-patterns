# Command Pattern

Command is a behavioral pattern that turns a request into stand-alone object that contains all the information about the request. This transformation lets users pass request as a method argument, delay or queue a request and support undoable operations.

## Real Life use cases

1. Celery task (queue)
2. DB Migrations (Can execute in a queue. Also can undo in a queue.)
3. Operation that supports keyboard shortcuts.

## Implementation

### Command Pattern in Python

```
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
```

#### Output

```
Upgrading Migration id: 1
Upgrading Migration id: 2
Upgrading Migration id: 3
Upgrading Migration id: 4
------------------------
Downgrading Migration id: 4
Downgrading Migration id: 3
Downgrading Migration id: 2
Downgrading Migration id: 1
```

### Command Pattern in JS

```
class Migration {
	id = null;

	constructor(id) {
		this.id = id;
	}

	upgrade() {
		console.log(`Upgrading Migration id: ${this.id}`);
	}

	downgrade() {
		console.log(`Downgrading Migration id: ${this.id}`);
	}
}

class MigrationHistory {
	migrations = [];
	lastExecutedMigrationId = null;

	add_migration(migration) {
		this.migrations.push(migration);
	}

	downgrade_to(id) {
		for (let i = this.migrations.length - 1; i >= 0; i--) {
			const migration = this.migrations[i];

			migration.downgrade();
			this.lastExecutedMigrationId = i ? i - 1 : null;

			if (migration.id === id) {
				break;
			}
		}
	}

	upgrade_all() {
		this.migrations.forEach((migration) => {
			migration.upgrade();
			this.lastExecutedMigrationId = migration.id;
		});
	}
}

const migrationHistory = new MigrationHistory();

const migration1 = new Migration(1);
const migration2 = new Migration(2);
const migration3 = new Migration(3);
const migration4 = new Migration(4);

migrationHistory.add_migration(migration1);
migrationHistory.add_migration(migration2);
migrationHistory.add_migration(migration3);
migrationHistory.add_migration(migration4);

migrationHistory.upgrade_all();

console.log("------------------------");

migrationHistory.downgrade_to(1);
```

#### Output

```
Upgrading Migration id: 1
Upgrading Migration id: 2
Upgrading Migration id: 3
Upgrading Migration id: 4
------------------------
Downgrading Migration id: 4
Downgrading Migration id: 3
Downgrading Migration id: 2
Downgrading Migration id: 1
```
