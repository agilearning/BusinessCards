"""
 ╦╦╔═╗╦ ╦╔═╗╦  ╔═╗╦ ╦╔═╗╔╗╔
 ║║╠═╣║║║║╣ ║  ║  ╠═╣║╣ ║║║
╚╝╩╩ ╩╚╩╝╚═╝╩  ╚═╝╩ ╩╚═╝╝╚╝
"""
from agilearning import agilearner


@agilearner
def markchang(**my):
    """ Learning Support-Vector """

    assert my["github"] == "https://github.com/sk413025"
    assert my["email"] == "sk413025@gmail.com"
    assert my["phone_number"] == "+886 987-233507"
    assert agilearning.VAT_ID == 24755908

