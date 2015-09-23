"""
╔═╦═╗┌─┐┬─┐┬ ┌  ╔═╗┬ ┬┌─┐┌┐┌┌─┐
║ ║ ║├─┤├┬┘├┬┘  ║  ├─┤├─┤││││ ┬
╩ ╩ ╩┴ ┴┴└─┘└─  ╚═╝┴ ┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def markchang(**my):
    """ Learning Support-Vector """

    assert my["github"] == "http://github.com/ckmarkoh"
    assert my["email"] == "ckmarkoh@gmail.com"
    assert my["phone_number"] == "+886 953-679220"
    assert VAT_ID == 24755908
