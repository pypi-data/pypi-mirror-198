# SPDX-FileCopyrightText: 2023-present Tyler McMaster <tyler@tlm13.com>
#
# SPDX-License-Identifier: MIT
__version__ = '0.0.7'

import functools
import logging

from service_days.servicedays import service_day_add, day_count_in_range, map_schedule_txt_to_day_list, days_in_range

__all__ = ['service_day_add', 'day_count_in_range', 'days_in_range', 'map_schedule_txt_to_day_list', __version__]


_log = logging.getLogger('servicedays')

