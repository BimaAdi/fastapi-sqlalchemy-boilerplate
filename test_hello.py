from unittest.async_case import IsolatedAsyncioTestCase


class HelloTest(IsolatedAsyncioTestCase):
    async def test_add(self):
        self.assertEqual(1 + 1, 2)
