"""
 ╦┌─┐┬ ┬┌┐┌  ╔═╗┬ ┬┌─┐┌┐┌
 ║│ │├─┤│││  ║  ├─┤├┤ │││
╚╝└─┘┴ ┴┘└┘  ╚═╝┴ ┴└─┘┘└┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def johnchen(**my):
    """ Trading Learner """

    assert my["github"] == "https://github.com/john-data-chen"
    assert my["email"] == "john.data.chen@gmail.com"
    assert my["phone_number"] == "+886 963-301746"
    assert VAT_ID == 24755908
