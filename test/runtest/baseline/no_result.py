#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Test how we handle a no-results test specified on the command line.
"""

import TestRuntest

test = TestRuntest.TestRuntest()

test.subdir('test')

test.write_no_result_test(['test', 'no_result.py'])

# NOTE:  The "test.no_result   : NO_RESULT" line has spaces at the end.

expect = r"""qmtest.py run --output baseline.qmr --format none --result-stream=scons_tdb.AegisBaselineStream test.no_result
--- TEST RESULTS -------------------------------------------------------------

  test.no_result                                : NO_RESULT

    NO RESULT TEST STDOUT

    NO RESULT TEST STDERR

--- TESTS WITH UNEXPECTED OUTCOMES -------------------------------------------

  test.no_result                                : NO_RESULT


--- STATISTICS ---------------------------------------------------------------

       1 (100%) tests unexpected NO_RESULT
"""

test.run(arguments = '--qmtest -b . test.no_result', stdout = expect)

test.pass_test()
