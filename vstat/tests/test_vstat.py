import nose
from vstat import vstat
from nose.tools import assert_almost_equal


def test_v():
    assert_almost_equal(vstat(120, 4, .05), .5109757)
