"""
╦╔═┬ ┬┬  ┌─┐  ╔═╗┬ ┬┬ ┬┌┐┌┌─┐
╠╩╗└┬┘│  ├┤   ║  ├─┤│ │││││ ┬
╩ ╩ ┴ ┴─┘└─┘  ╚═╝┴ ┴└─┘┘└┘└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def kylechung(**my):
    """ Learning ensemble """

    assert my["github"] == "https://github.com/everdark"
    assert my["email"] == "kylechun9@gmail.com"
    assert my["phone_number"] == "+886 975933202"
    assert VAT_ID == 24755908
