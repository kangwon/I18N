from django.test import TestCase

from app.models import Key, Translation


class KeyTestCase(TestCase):
    def setUp(self):
        self.sample_obj = {
            "id": 1,
            "name": "test.first.key"
        }
        Key.objects.create(**self.sample_obj)

    def test_list(self):
        response = self.client.get('/keys/')
        self.assertJSONEqual(response.content, {"keys": [self.sample_obj]})

    def test_search(self):
        response = self.client.get('/keys/?name=first')
        self.assertJSONEqual(response.content, {"keys": [self.sample_obj]})
        response = self.client.get('/keys/?name=second')
        self.assertJSONEqual(response.content, {"keys": []})

    def test_retrieve(self):
        response = self.client.get('/keys/1/')
        self.assertJSONEqual(response.content, {"key": self.sample_obj})

    def test_create(self):
        response = self.client.post('/keys/', {
            'name': 'test.seconde.key',
        })
        self.assertJSONEqual(response.content, {"key": {
            'id': 2,
            'name': 'test.seconde.key',
        }})

    def test_create_duplicated(self):
        response = self.client.post('/keys/', {
            'name': self.sample_obj['name'],
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"name": [
            "key with this name already exists."
        ]})

    def test_invalid_key_name(self):
        response = self.client.post('/keys/', {
            'name': '1234',
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"name": [
            "This value does not match the required pattern."
        ]})
        response = self.client.put('/keys/1/', {
                'name': '1234',
            },
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"name": [
            "This value does not match the required pattern."
        ]})


    def test_update(self):
        response = self.client.put('/keys/1/', {
                'name': 'test.first.key.updated',
            },
            content_type='application/json',
        )
        self.assertJSONEqual(response.content, {"key": {
            'id': self.sample_obj["id"],
            'name': 'test.first.key.updated',
        }})


class TranslationTestCase(TestCase):
    def setUp(self):
        self.sample_key = Key.objects.create(**{
            "id": 1,
            "name": "test.first.key"
        })
        Translation.objects.create(**{
            "id": 1,
            "value": "test translation",
            "key": self.sample_key,
            "locale": "en",
        })
        self.sample_obj = {
            "id": 1,
            "value": "test translation",
            "keyId": 1,
            "locale": "en",
        }

    def test_list(self):
        response = self.client.get('/keys/1/translations/')
        self.assertJSONEqual(response.content, {"translations": [self.sample_obj]})

    def test_retrieve(self):
        response = self.client.get('/keys/1/translations/en/')
        self.assertJSONEqual(response.content, {"translation": self.sample_obj})

    def test_create(self):
        response = self.client.post('/keys/1/translations/ko/', {
            'value': '테스트 변역문',
        })
        self.assertJSONEqual(response.content, {"translation": {
            'id': 2,
            "value": "테스트 변역문",
            "keyId": 1,
            "locale": "ko",
        }})

    def test_create_duplicated(self):
        response = self.client.post('/keys/1/translations/en/', {
            'value': 'test test',
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, [
            "There already exist the translation."
        ])

    def test_create_invalid_locale(self):
        response = self.client.post('/keys/1/translations/py/', {
            'value': 'test = TestCase()',
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {
            'locale': 'Invalid locale: py'
        })

    def test_update(self):
        response = self.client.put('/keys/1/translations/en/', {
                'value': 'updated translation',
            },
            content_type='application/json',
        )
        self.assertJSONEqual(response.content, {"translation": {
            "id": 1,
            'value': 'updated translation',
            "keyId": 1,
            "locale": "en",
        }})
