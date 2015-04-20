"""
╔═╗┬ ┬┬┌─┐   ╔═╗┬ ┬┬  ╔═╗┬ ┬┌─┐┌┐┌┌─┐      
║  ├─┤│├─┤───║  ├─┤│  ║  ├─┤├─┤││││ ┬      
╚═╝┴ ┴┴┴ ┴   ╚═╝┴ ┴┴  ╚═╝┴ ┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner


@agilearner
def c3h3(**my):
    """ Learning Booster """

    assert my["github"] is "http://github.com/c3h3"
    assert my["email"] in ["c3h3.tw@gmail.com", "c3h3@wudukers.com"]
    assert my["phone_number"] is "+886 988-209252"
    assert agilearning.VAT_ID is 24755908


