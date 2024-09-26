import unittest
from unittest.mock import Mock
from ex_user_repository import User, UserService, UserRepository

class TestUserService(unittest.TestCase):
    """Unit tests for UserService."""

    def setUp(self):
        # Create a mock repository
        self.mock_repository = Mock(spec=UserRepository)
        self.user_service = UserService(self.mock_repository)

    def test_register_user(self):
        # Arrange
        name = "Alice"
        email = "alice@example.com"
        expected_user = User(1, name, email)
        self.mock_repository.add.return_value = None

        # Act
        result = self.user_service.register_user(name, email)

        # Assert
        self.assertEqual(result.name, expected_user.name)
        self.assertEqual(result.email, expected_user.email)
        self.mock_repository.add.assert_called_once()

    def test_change_user_email(self):
        # Arrange
        user_id = 1
        old_email = "old@example.com"
        new_email = "new@example.com"
        existing_user = User(user_id, "Alice", old_email)
        self.mock_repository.get.return_value = existing_user

        # Act
        result = self.user_service.change_user_email(user_id, new_email)

        # Assert
        self.assertEqual(result.email, new_email)
        self.mock_repository.get.assert_called_once_with(user_id)
        self.mock_repository.update.assert_called_once()
        
if __name__ == "__main__":
    # Run unit tests
    unittest.main()