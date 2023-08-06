from dicee import KGE

x=KGE('Experiments/2023-03-03 09:07:31.822737')

print(x.predict(head_entities=["acquired_abnormality"], relations=["location_of"],tail_entities=["experimental_model_of_disease"]))

exit()
import torch
import numpy as np

hat_y = torch.tensor([[0.1, 0.4, 0.3, 0.2, 0.8, 0.1],
                      [0.4, 0.2, 0.1, 0.2, 0.1, 0.4],
                      [0.1, 0.7, 0.1, 0.0, 0.3, 0.6],
                      [0.1, 0.1, 0.1, 0.0, 0.3, 0.6],
                      [0.1, 0.5, 0.4, 0.0, 0.3, 0.6]]).unsqueeze(0)
y = torch.tensor([1, 2, 0, 2, 3, 4]).unsqueeze(0).long()

loss = torch.nn.CrossEntropyLoss(reduction='sum')
print(loss(hat_y, y))

loss = 0
for ith, index_of_true_class in enumerate([1, 2, 0, 2, 3, 4]):
    scores = hat_y[0, :, ith].numpy()
    score_of_true_class = scores[index_of_true_class]
    loss += np.log(np.exp(score_of_true_class) / np.sum(np.exp(scores)))
print(-loss)

y = torch.zeros((5, 6))
y[:, 0][1] = 1
y[:, 1][2] = 1
y[:, 2][0] = 1
y[:, 3][2] = 1
y[:, 4][3] = 1
y[:, 5][4] = 1

print(y)

print(hat_y)

exit(1)

yy=hat_y.squeeze(0).flatten()
loss = torch.nn.BCEWithLogitsLoss(reduction='sum')
print(loss(yy, y.flatten()))
exit(1)

hat_y = hat_y.view(5, 6).numpy()
y = y.flatten().numpy()
print(hat_y.shape)
print(y.shape)
#
import numpy as np

loss = 0
for i_th_row in range(len(hat_y)):
    hat_y_i = hat_y[i_th_row]
    true_class_for_ith_row = y[i_th_row]
    loss += np.log(np.exp(hat_y_i[true_class_for_ith_row]) / sum(np.exp(hat_y_i)))
loss = -loss

print(loss / len(hat_y))
