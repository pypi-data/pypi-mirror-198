def test_package_import():
    import botcity.plugins.ms365.onedrive as plugin
    assert plugin.__file__ != ""
