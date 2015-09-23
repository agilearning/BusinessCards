"""
╔═╗┬ ┬┌┬┐┌┬┐┬┌┬┐  ╔═╗┬ ┬┌─┐┌┐┌
╚═╗│ ││││││││ │   ╚═╗│ │├┤ │││
╚═╝└─┘┴ ┴┴ ┴┴ ┴   ╚═╝└─┘└─┘┘└┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def suensummit(**my):
    """ Learning Kernel """

    assert my["github"] == "http://github.com/suensummit"
    assert my["email"] in ["summit.suen@data-sci.info", "summit.suen@gmail.com"]
    assert my["phone_number"] in ["+886 920-390985", "+886 972-715285"]
    assert VAT_ID == 24755908
