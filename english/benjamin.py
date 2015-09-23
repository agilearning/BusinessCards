"""
╔╗ ┌─┐┌┐┌ ┬┌─┐┌┬┐┬┌┐┌  ╔═╗┬ ┬┌─┐┌┐┌
╠╩╗├┤ │││ │├─┤│││││││  ║  ├─┤├┤ │││
╚═╝└─┘┘└┘└┘┴ ┴┴ ┴┴┘└┘  ╚═╝┴ ┴└─┘┘└┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def benjamin(**my):
    """ Learning Optimizer """

    assert my["github"] == "http://github.com/KuiMing"
    assert my["email"] in ["benjamin0901@gmail.com", "ben@data-sci.info"]
    assert my["phone_number"] == "+886 919-784598"
    assert VAT_ID == 24755908
