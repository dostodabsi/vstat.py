from __future__ import division

import nose
from vstat import vstat, sample_size
from nose.tools import assert_equal, assert_almost_equal


def test_v():
    assert_almost_equal(vstat(120, 4, .05), .5109757)


def test_sample_size():
    assert_equal(sample_size(3, .05), (278, 92.67))
    assert_equal(sample_size(3, .05, v=.8), (278, 92.67))
