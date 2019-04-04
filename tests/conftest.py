import django
import pytest


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """Give access to database from anywhere.

    https://pytest-django.readthedocs.io/en/latest/faq.html#how-can-i-give-database-access-to-all-my-tests-without-the-django-db-marker
    """
    pass


def pytest_configure(config):
    from django.conf import settings

    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:"
            }
        },
        SECRET_KEY="53cr3t",
        INSTALLED_APPS=(
            "django.contrib.contenttypes",
            "clonery",
            "tests",
        )
    )

    django.setup()