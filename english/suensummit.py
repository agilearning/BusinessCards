"""
╔═╗┬ ┬┌┬┐┌┬┐┬┌┬┐  ╔═╗┬ ┬┌─┐┌┐┌
╚═╗│ ││││││││ │   ╚═╗│ │├┤ │││
╚═╝└─┘┴ ┴┴ ┴┴ ┴   ╚═╝└─┘└─┘┘└┘
"""
from agilearning import agilearner


@agilearner
def suensummit(**my):
    """ Learning Kernel """

    assert my["github"] is "http://github.com/suensummit"
    assert my["email"] in ["summit.suen@data-sci.info", "summit.suen@gmail.com"]
    assert my["phone_number"] in ["+886 920-390985", "+886 972-715285"]
    assert agilearning.VAT_ID is 24755908
