from model_background import Background
class Camada1(Background):
    def __init__(self,xpos):
        super().__init__('Renangame\layers\ground_3.png',xpos)

    def set_largura(self,camada_largura):
        super().set_largura(camada_largura)