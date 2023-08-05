# cython: language_level=3
#  Drakkar-Software OctoBot-Trading
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
cimport octobot_trading.personal_data.state as state_class

cdef class PositionState(state_class.State):
    cdef public object position   # instance of Position
    cdef public object _has_state_changed   # asyncio.Event()

    cpdef bint is_active(self)
    cpdef bint has_to_be_async_synchronized(self)
    cpdef bint is_liquidated(self)
    cpdef void set_is_changing_state(self)
