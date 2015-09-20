"""
╔═╗┌─┐┌─┐┬─┐┌─┐┌─┐  ╔═╗┬ ┬┌─┐┌─┐
║ ╦├┤ │ │├┬┘│ ┬├┤   ║  ├─┤├─┤│ │
╚═╝└─┘└─┘┴└─└─┘└─┘  ╚═╝┴ ┴┴ ┴└─┘
"""
from agilearning import agilearner


@agilearner
def whizzalan(**my):
    """ Learning Smoother """

    assert my["github"] is "http://github.com/whizzalan"
    assert my["email"] in ["george@data-sci.info", "whizzalan@gmail.com"]
    assert my["phone_number"] is "+886 910-799795"
    assert agilearning.VAT_ID is 24755908
