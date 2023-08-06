import pytest
import os
from librtree import RTree, RTreeStyle
from tempfile import TemporaryDirectory

@pytest.fixture
def rtree():
    rtree = RTree(2)
    rtree.add_rect(43, (0, 0, 1, 1))
    rtree.add_rect(44, (1, 1, 2, 2))
    return rtree

@pytest.fixture
def style():
    return RTreeStyle.from_list(
        [
            {
                "stroke": {
                    "grey": 0.9,
                    "width": 1.0
                },
                "fill": {
                    "rgb": (0.9, 0.1, 0.1)
                }

            },
            {
                "fill": {
                    "rgb": (0.8, 0.2, 0.2)
                }
            }
        ]
    )

def test_postscript_callable(rtree):
    assert callable(rtree.postscript)

def test_postscript_valid(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            rtree.postscript(io, style)
        assert os.path.exists(path)

def test_postscript_invalid_io(rtree, style):
    with pytest.raises(ValueError, match=r'no fileno'):
        rtree.postscript(None, style)

def test_postscript_invalid_style(rtree):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            with pytest.raises(TypeError, match=r'not a style'):
                rtree.postscript(io, None)

def test_postscript_height(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            rtree.postscript(io, style, height=300)
        assert os.path.exists(path)

def test_postscript_invalid_height(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            with pytest.raises(TypeError, match=r'extent'):
                rtree.postscript(io, style, height='meh')

def test_postscript_width(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            rtree.postscript(io, style, width=300)
        assert os.path.exists(path)

def test_postscript_invalid_width(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            with pytest.raises(TypeError, match=r'extent'):
                rtree.postscript(io, style, width='meh')

def test_postscript_height_and_width(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            with pytest.raises(RuntimeError, match=r'width and height'):
                rtree.postscript(io, style, width=300, height=300)

def test_postscript_margin(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            rtree.postscript(io, style, margin=5)
        assert os.path.exists(path)

def test_postscript_invalid_margin(rtree, style):
    with TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'file.eps')
        with open(path, 'w') as io:
            with pytest.raises(TypeError, match=r'margin'):
                rtree.postscript(io, style, margin='meh')
