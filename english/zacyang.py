"""
╔═╗┌─┐┌─┐  ╦ ╦┌─┐┌┐┌┌─┐
╔═╝├─┤│    ╚╦╝├─┤││││ ┬
╚═╝┴ ┴└─┘   ╩ ┴ ┴┘└┘└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def zacariasyang(**my):
    """ Data-driven Evangelist """

    assert my["github"] == "http://github.com/zacariasyang"
    assert my["email"] in ["zac@data-sci.info", "zac.yang@gmail.com"]
    assert my["phone_number"] == "+886 987-007019"
    assert VAT_ID == 24755908
