#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~
#  MIT License
#
#  Copyright (c) 2021 Nathan Juraj Michlo
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#  ~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~

from ._schedule import Schedule

# schedules
from ._schedule import ClipSchedule
from ._schedule import CosineWaveSchedule
from ._schedule import CyclicSchedule
from ._schedule import LinearSchedule
from ._schedule import NoopSchedule
from ._schedule import MultiplySchedule
from ._schedule import FixedValueSchedule
from ._schedule import SingleSchedule


# aliases
from ._schedule import ClipSchedule as Clip
from ._schedule import CosineWaveSchedule as CosineWave
from ._schedule import CyclicSchedule as Cyclic
from ._schedule import LinearSchedule as Linear
from ._schedule import NoopSchedule as Noop
from ._schedule import MultiplySchedule as Multiply
from ._schedule import FixedValueSchedule as FixedValue
from ._schedule import SingleSchedule as Single
