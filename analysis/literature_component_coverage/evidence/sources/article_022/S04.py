low_data = """phi-2 0.981 0.987 0.927
gemma-2b 0.524 0.994 0.630
gemma-7b 0.812 0.288 0.990
Llama-2-7b 0.754 0.967 0.830
Llama-2-13b 0.718 0.715 0.325
Llama-2-70b 0.882 0.881 0.540
Llama-3-8b 0.860 0.968 0.958
Llama-3-70b 0.971 0.926 0.967
Mistral-7B 0.981 0.959 0.994
Mixtral-8x7B 0.999 0.994 0.997
Gpt-3.5-turbo 0.908 0.466 0.983
Gemini-1.0-pro 0.994 0.996 0.996"""

high_data = """phi-2 0.668 0.772 0.804
gemma-2b 0.319 0.882 0.396
gemma-7b 0.609 0.341 0.685
Llama-2-7b 0.356 0.593 0.603
Llama-2-13b 0.187 0.107 0.900
Llama-2-70b 0.209 0.118 0.906
Llama-3-8b 0.329 0.512 0.751
Llama-3-70b 0.757 0.881 0.657
Mistral-7B 0.612 0.507 0.860
Mixtral-8x7B 0.876 0.879 0.863
Gpt-3.5-turbo 0.409 0.513 0.732
Gemini-1.0-pro 0.857 0.888 0.885"""

data = high_data 

data = data.split('\n')
model_result = []
for d in data:
    model_result.append(d.split(" ")[1:])

import numpy as np

model_result = np.array(model_result, dtype=float)

row_sums = model_result.sum(axis=1, keepdims=True)

normalized_model_result = model_result / row_sums


pb = []
sb = []
C_t = []
def kl(result, position):
    for res in result:
        ans = 0
        ans = res[position] * np.log(res[position] / res[0]) + res[position] * np.log(res[position] / res[3-position]) + (1-res[position]) * np.log((1-res[position]) / (1-res[0])) + (1-res[position]) * np.log((1-res[position]) / (1-res[3-position]))
        if position==1:
            pb.append(ans)
        else:
            sb.append(ans)

position_bias = 1
selection_bias = 2

kl(normalized_model_result, position_bias)
kl(normalized_model_result, selection_bias)
a, b = 0.1, 0.1
for i in range(len(model_result)):
    real = 0
    real += model_result[i][0] * (1 - a*pb[i] - b*sb[i])
    real += model_result[i][1] * (1 - a*pb[i] + b*sb[i])
    real += model_result[i][2] * (1 + a*pb[i] - b*sb[i])
    C_t.append(real / 3)
    
print(C_t)
print(pb)
print(sb)