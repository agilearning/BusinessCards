"""
╔═╗┌─┐┌─┐┬─┐┌─┐┌─┐  ╔═╗┬ ┬┌─┐┌─┐
║ ╦├┤ │ │├┬┘│ ┬├┤   ║  ├─┤├─┤│ │
╚═╝└─┘└─┘┴└─└─┘└─┘  ╚═╝┴ ┴┴ ┴└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def whizzalan(**my):
    """ Learning Smoother """

    assert my["github"] == "http://github.com/whizzalan"
    assert my["email"] in ["george@data-sci.info", "whizzalan@gmail.com"]
    assert my["phone_number"] == "+886 910-799795"
    assert VAT_ID == 24755908
