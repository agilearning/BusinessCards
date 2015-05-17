"""
╔═╗┬ ┬┬┬ ┬   ╔═╗┬ ┬┌─┐┌┐┌┌─┐  ╦  ┬┌─┐┌┐┌┌─┐
║  ├─┤│├─┤───║  ├─┤├┤ ││││ ┬  ║  │├─┤││││ ┬
╚═╝┴ ┴┴┴ ┴   ╚═╝┴ ┴└─┘┘└┘└─┘  ╩═╝┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner
 
 
@agilearner
def chihcheng(**my):
    """ Learning Supervisor """
 
    assert my["github"] == "http://github.com/ChihChengLiang"
    assert my["email"] == "chihchengliang@gmail.com"
    assert my["phone_number"] == "+886 921-315607"
    assert agilearning.VAT_ID == 24755908


