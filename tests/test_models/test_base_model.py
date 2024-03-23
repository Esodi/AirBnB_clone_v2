import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_updates_updated_at(self):
        original_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_structure(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        base_model_dict = self.base_model.to_dict()
        self.assertCountEqual(base_model_dict.keys(), expected_keys)

    def test_to_dict_values(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_from_dict(self):
        base_model_dict = self.base_model.to_dict()
        new_model = BaseModel(**base_model_dict)
        self.assertEqual(new_model.id, self.base_model.id)
        self.assertEqual(new_model.created_at, self.base_model.created_at)
        self.assertEqual(new_model.updated_at, self.base_model.updated_at)


if __name__ == '__main__':
    unittest.main()
