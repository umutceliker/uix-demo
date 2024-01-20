import uix
from uix.elements import div, button, svg, icon # type: ignore
from uix.elements._button import title, description, sample as code

uix.html.add_css("svg_button",'''
.btn-svg-demo{
        padding: 0 !important;
        min-width: 38px !important;
        width: 38px;
        height: 38px;
}

''')

button_demo_svg = '<g><path fill="#ffffff" d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336h24V272H216c-13.3 0-24-10.7-24-24s10.7-24 24-24h48c13.3 0 24 10.7 24 24v88h8c13.3 0 24 10.7 24 24s-10.7 24-24 24H216c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z"/></g>'

def degistir(ctx, id, value):
    ctx.elements["btn-icon1"].value = "fa-solid fa-user"

def button_example():
    with div().cls("row").style("gap","10px") as main:
        button("Değiştir").on("click", degistir)
        button("Sarı").cls("btn-warning")
        button("Kırmızı").cls("btn-red")
        button("Info").cls("btn-info")
        button("Reset", type="reset").cls("btn-reset")
        with button("", id="myID", type="sumbit").cls("btn-svg-demo"):
            svg(button_demo_svg).size(20,20).viewbox("0,0,512,512")
        with button("", id="btn-fontawesome").cls("btn-inactive btn-svg-demo").style("color","black"):
            icon(id= "btn-icon1", value= "fa-solid fa-house")
        button("Disabled", disabled=True)
            
    return main