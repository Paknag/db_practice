from orator.migrations import Migration


class CreatePracticeDataTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('practice_data') as table:
            table.increments('id')
            table.string('namef')
            table.string('namel')
            table.string('note')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('practice_data')
