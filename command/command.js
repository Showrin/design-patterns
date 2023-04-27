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

// # Output
// Upgrading Migration id: 1
// Upgrading Migration id: 2
// Upgrading Migration id: 3
// Upgrading Migration id: 4
// ------------------------
// Downgrading Migration id: 4
// Downgrading Migration id: 3
// Downgrading Migration id: 2
// Downgrading Migration id: 1
