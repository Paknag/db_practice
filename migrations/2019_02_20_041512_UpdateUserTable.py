from orator.migrations import Migration


class UpdateUserTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('practice_data') as table:
            table.rename_column('namef', 'first')
            table.rename_column('namel', 'last')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('practice_data')
