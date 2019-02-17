from orator.migrations import Migration


class CreatePracticeDataTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('practice_data') as table:
            ts = table.string
            table.increments('id')
            ts('namef')
            ts('namel')
            ts('note')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('practice_data')
