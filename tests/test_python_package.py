from python_package.python_package import cwd

def test_cwd():
    assert len(str(cwd()))
