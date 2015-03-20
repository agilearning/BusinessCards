"""
╔═╗┬ ┬┬┬ ┬   ╔═╗┬ ┬┌─┐┌┐┌┌─┐  ╦  ┬┌─┐┌┐┌┌─┐
║  ├─┤│├─┤───║  ├─┤├┤ ││││ ┬  ║  │├─┤││││ ┬
╚═╝┴ ┴┴┴ ┴   ╚═╝┴ ┴└─┘┘└┘└─┘  ╩═╝┴┴ ┴┘└┘└─┘
"""
from agilearning import agilearner
 
 
@agilearner
def chihcheng(**my):
    """ Learning Supervisor """
 
    assert my["github"] is "http://github.com/ChihChengLiang"
    assert my["email"] is "chihchengliang@gmail.com"
    assert my["phone_number"] is "+886 921-315607"
    assert agilearning.VAT_ID is 24755908


