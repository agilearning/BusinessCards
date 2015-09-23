"""
╔═╗┬ ┬┬┌─┐   ╔═╗┬ ┬┬  ╔═╗┬ ┬┌─┐┌┐┌┌─┐
║  ├─┤│├─┤───║  ├─┤│  ║  ├─┤├─┤││││ ┬
╚═╝┴ ┴┴┴ ┴   ╚═╝┴ ┴┴  ╚═╝┴ ┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def c3h3(**my):
    """ Learning Booster """

    assert my["github"] == "http://github.com/c3h3"
    assert my["email"] in ["c3h3@agilearning.io", "c3h3.tw@gmail.com"]
    assert my["phone_number"] == "+886 988-209252"
    assert VAT_ID == 24755908
