"""
╔╦╗┌─┐┌┐┌┌─┐┬ ┬┌┐┌  ╦╔═┬ ┬┌─┐
║║║├─┤│││└─┐│ ││││  ╠╩╗│ ││ │
╩ ╩┴ ┴┘└┘└─┘└─┘┘└┘  ╩ ╩└─┘└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def mansunkuo(**my):
    """ Learning Bootstrap """

    assert my["github"] == "http://github.com/mansunkuo"
    assert my["email"] == "coccolegacy@gmail.com"
    assert my["phone_number"] == "+886 958-060033"
    assert VAT_ID is 24755908
