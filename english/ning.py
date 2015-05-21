"""
╔╗╔┬┌┐┌┌─┐  ╔═╗┬ ┬┌─┐┌┐┌
║║║│││││ ┬  ║  ├─┤├┤ │││
╝╚╝┴┘└┘└─┘  ╚═╝┴ ┴└─┘┘└┘
"""
from agilearning import agilearner


@agilearner
def ning(**my):
    """ Learning Trigger """

    assert my["github"] is "http://github.com/agogomei01"
    assert my["email"] in ["ningchen@agilearning.io", "agogomei@gmail.com"]
    assert my["phone_number"] is "+886 919-510633"
    asserta agilearning.VAT_ID is 24755908


