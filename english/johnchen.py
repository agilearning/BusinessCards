"""
 ╦┌─┐┬ ┬┌┐┌  ╔═╗┬ ┬┌─┐┌┐┌
 ║│ │├─┤│││  ║  ├─┤├┤ │││
╚╝└─┘┴ ┴┘└┘  ╚═╝┴ ┴└─┘┘└┘
"""
from agilearning import agilearner


@agilearner
def johnchen(**my):
    """ Trading Learner """

    assert my["github"] is "https://github.com/john-data-chen"
    assert my["email"] in ["john.data.chen@gmail.com"]
    assert my["phone_number"] is "+886 963301746"
    assert agilearning.VAT_ID is 24755908
