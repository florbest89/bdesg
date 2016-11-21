from weblayer import WebLayer3857


class OlBuenosAiresMapLayer(WebLayer3857):

    emitsLoadEnd = True

    def __init__(self):
        WebLayer3857.__init__(self, groupName="Buenos Aires Maps", groupIcon="bsas_icon.png",
                              name='Buenos Aires map', html='bsas.html')

