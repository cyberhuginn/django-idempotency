import django


def test_django_version():
    assert django.VERSION[:2] == (5, 2)
