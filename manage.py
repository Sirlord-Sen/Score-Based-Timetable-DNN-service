import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from dotenv import load_dotenv
load_dotenv()

from app import create_app, db

from app.score_based_study_hour.model.course_model import Course

app = create_app(os.getenv('ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    port = os.environ.get('PORT')
    app.run(port= port)

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()