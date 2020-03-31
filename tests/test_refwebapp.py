from refwebapp import version


def test_version():
    assert version.version_info.package == "refwebapp"
