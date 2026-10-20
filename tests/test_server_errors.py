import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

from bson import ObjectId
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import ValidationError

from app.auth.jwt import create_token
from app.models.cart import CartAdd, CartUpdate
from app.routes import auth, cart


class ServerErrorTests(unittest.IsolatedAsyncioTestCase):
    async def test_invalid_token_returns_401(self):
        credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials="invalid")
        with self.assertRaises(HTTPException) as error:
            await auth.get_me(credentials)
        self.assertEqual(error.exception.status_code, 401)

    async def test_token_without_user_returns_401(self):
        credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=create_token(""))
        with self.assertRaises(HTTPException) as error:
            await auth.get_me(credentials)
        self.assertEqual(error.exception.status_code, 401)

    async def test_new_cart_is_json_serializable(self):
        async def insert(document):
            document["_id"] = ObjectId()

        collection = SimpleNamespace(find_one=AsyncMock(return_value=None), insert_one=AsyncMock(side_effect=insert))
        with patch.object(cart, "db", SimpleNamespace(carts=collection)):
            result = await cart.get_cart(SimpleNamespace(id="test-user"))
        self.assertEqual(jsonable_encoder(result)["items"], [])
        self.assertNotIn("_id", result)

    async def test_cart_updates_exclude_mongo_id(self):
        collection = SimpleNamespace(
            find_one=AsyncMock(return_value={"user_id": "test-user", "items": [{"product_id": "p", "quantity": 1}]}),
            update_one=AsyncMock(),
        )
        with patch.object(cart, "db", SimpleNamespace(carts=collection)):
            await cart.update_cart_quantity("p", CartUpdate(quantity=2), SimpleNamespace(id="test-user"))
        collection.find_one.assert_awaited_once_with({"user_id": "test-user"}, {"_id": 0})
        self.assertNotIn("_id", collection.update_one.call_args.args[1]["$set"])

    def test_invalid_cart_inputs_are_rejected(self):
        for payload in ({}, {"product_id": "p", "quantity": -1}, {"product_id": "p", "quantity": "two"}):
            with self.subTest(payload=payload), self.assertRaises(ValidationError):
                CartAdd(**payload)
        with self.assertRaises(ValidationError):
            CartUpdate(quantity=0)


if __name__ == "__main__":
    unittest.main()
