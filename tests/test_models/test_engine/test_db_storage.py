import unittest
from models import DBStorage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.db = DBStorage()
        self.db.reload()

    def tearDown(self):
        self.db.close()

    def test_connection(self):
        self.assertIsNotNone(self.db._DBStorage__engine)

    def test_add_object(self):
        state = State(name="California")
        self.db.new(state)
        self.db.save()
        self.assertIn(state, self.db.all(State))

    def test_delete_object(self):
        state = State(name="California")
        self.db.new(state)
        self.db.save()
        self.db.delete(state)
        self.assertNotIn(state, self.db.all(State))

    def test_import_user(self):
        user = User(email="test@example.com", password="password")
        self.db.new(user)
        self.db.save()
        self.assertIn(user, self.db.all(User))

    def test_import_city(self):
        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)
        self.db.new(state)
        self.db.new(city)
        self.db.save()
        self.assertIn(city, self.db.all(City))


if __name__ == '__main__':
    unittest.main()