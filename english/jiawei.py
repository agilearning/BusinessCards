"""
 ╦╦╔═╗╦ ╦╔═╗╦  ╔═╗╦ ╦╔═╗╔╗╔
 ║║╠═╣║║║║╣ ║  ║  ╠═╣║╣ ║║║
╚╝╩╩ ╩╚╩╝╚═╝╩  ╚═╝╩ ╩╚═╝╝╚╝
"""
from agilearning import agilearner, VAT_ID


@agilearner
def jiawei(**my):
    """ Active Learner """

    assert my["github"] == "https://github.com/sk413025"
    assert my["email"] == "sk413025@gmail.com"
    assert my["phone_number"] == "+886 987-233507"
    assert VAT_ID == 24755908
