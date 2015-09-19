"""
╔═╗┌┬┐┬─┐┬┌─┐┌┐┌  ╦  ┬┌─┐┬ ┬
╠═╣ ││├┬┘│├─┤│││  ║  │├─┤│││
╩ ╩─┴┘┴└─┴┴ ┴┘└┘  ╩═╝┴┴ ┴└┴┘
"""
from agilearning import agilearner


@agilearner
def adrianliaw(**my):
    """ Learning Reinforcer """

    assert my["github"] == "http://github.com/adrianliaw"
    assert my["email"] in ["whliaw@agilearning.io", "adrianliaw2000@gmail.com"]
    assert my["phone_number"] == "+886 976-407095"
    assert agilearning.VAT_ID == 24755908
