"""
╦╔═┬ ┬┬  ┌─┐  ╔═╗┬ ┬┬ ┬┌┐┌┌─┐
╠╩╗└┬┘│  ├┤   ║  ├─┤│ │││││ ┬
╩ ╩ ┴ ┴─┘└─┘  ╚═╝┴ ┴└─┘┘└┘└─┘

"""
from agilearning import agilearner


@agilearner
def kylechung(**my):
    """ Learning ensemble """

    assert my["github"] is "https://github.com/everdark"
    assert my["email"] in ["kylechun9@gmail.com"]
    assert my["phone_number"] is "+886 975933202"
    assert agilearning.VAT_ID is 24755908
