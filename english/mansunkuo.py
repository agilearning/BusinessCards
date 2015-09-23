"""
╔╦╗┌─┐┌┐┌┌─┐┬ ┬┌┐┌  ╦╔═┬ ┬┌─┐
║║║├─┤│││└─┐│ ││││  ╠╩╗│ ││ │
╩ ╩┴ ┴┘└┘└─┘└─┘┘└┘  ╩ ╩└─┘└─┘
"""
from agilearning import agilearner


@agilearner
def mansunkuo(**my):
    """ Learning Bootstrap """

    assert my["github"] is "http://github.com/mansunkuo"
    assert my["email"] in ["coccolegacy@gmail.com"]
    assert my["phone_number"] is "+886 958-060033"
    assert agilearning.VAT_ID is 24755908
