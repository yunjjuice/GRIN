from create_model import create_model_emo
from predic_emo import predic



model = create_model_emo()

text = "잘 분석한다면 기분이가 좋겠어요"
pred = predic(model, text)
