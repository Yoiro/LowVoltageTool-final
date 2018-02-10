#!/usr/bin/env python
# coding=utf-8


from enum import Enum, unique


@unique
class Timestamp(Enum):
    """Enum support for Monte Carlo ease of use."""
    QUARTERS = 1
    HOURS = 2
    DAYS = 3
