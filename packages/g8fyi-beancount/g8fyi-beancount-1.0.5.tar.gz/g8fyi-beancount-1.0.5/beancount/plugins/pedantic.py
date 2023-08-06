"""A plugin of plugins which triggers are all the pedantic plugins.

In a sense, this is the inverse of "pedantic." This is useful when doing some
types of quick and dirty tests.
"""
__copyright__ = "Copyright (C) 2017  Martin Blais"
__license__ = "GNU GPLv2"

from beancount import loader
from g8fyi_beancount.plugins import check_commodity
from g8fyi_beancount.plugins import check_drained
from g8fyi_beancount.plugins import coherent_cost
from g8fyi_beancount.plugins import leafonly
from g8fyi_beancount.plugins import noduplicates
from g8fyi_beancount.plugins import nounused
from g8fyi_beancount.plugins import onecommodity
from g8fyi_beancount.plugins import sellgains
from g8fyi_beancount.plugins import unique_prices

__plugins__ = loader.combine_plugins(
    check_commodity,
    coherent_cost,
    leafonly,
    noduplicates,
    nounused,
    onecommodity,
    sellgains,
    unique_prices,
    check_drained,
)
