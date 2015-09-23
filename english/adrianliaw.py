"""
╔═╗┌┬┐┬─┐┬┌─┐┌┐┌  ╦  ┬┌─┐┬ ┬
╠═╣ ││├┬┘│├─┤│││  ║  │├─┤│││
╩ ╩─┴┘┴└─┴┴ ┴┘└┘  ╩═╝┴┴ ┴└┴┘
"""
from agilearning import agilearner, VAT_ID


@agilearner
def adrianliaw(**my):
    """ Learning Reinforcer """

    assert my["github"] == "http://github.com/adrianliaw"
    assert my["email"] in ["whliaw@agilearning.io", "adrianliaw2000@gmail.com"]
    assert my["phone_number"] == "+886 976-407095"
    assert VAT_ID == 24755908
