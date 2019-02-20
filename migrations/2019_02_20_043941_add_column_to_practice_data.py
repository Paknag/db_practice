from orator.migrations import Migration


class AddColumnToPracticeData(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('practice_data') as table:
            table.integer('age').unsigned().nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('practice_data') as table:
            table.drop_column('age')
