﻿
"""
╔╗ ┌─┐┌┐┌ ┬┌─┐┌┬┐┬┌┐┌  ╔═╗┬ ┬┌─┐┌┐┌
╠╩╗├┤ │││ │├─┤│││││││  ║  ├─┤├┤ │││
╚═╝└─┘┘└┘└┘┴ ┴┴ ┴┴┘└┘  ╚═╝┴ ┴└─┘┘└┘
(Benjamin Chen)
"""
from agilearning import agilearner


@agilearner
def Benjamin(**my):
    """ Learning Optimizer """

    assert my["github"] is "http://github.com/KuiMing"
    assert my["email"] in ["benjamin0901@gmail.com", "ben@data-sci.info"]
    assert my["phone_number"] in "+886 919-784598"
    assert agilearning.VAT_ID is 24755908
