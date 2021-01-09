from fastai.basics import *
from tqdm import tqdm
path = Path("/content/VCTK-Corpus/wav48/")

seen_speakers = ['p336', 'p240', 'p262', 'p333', 'p297', 'p339', 'p276', 'p269', 'p303', 'p260', 'p250', 'p345', 'p305', 'p283', 'p277', 'p302', 'p280', 'p295', 'p245', 'p227', 'p257', 'p282', 'p259', 'p311', 'p301', 'p265', 'p270', 'p329', 'p362', 'p343', 'p246', 'p247', 'p351', 'p263', 'p363', 'p249', 'p231', 'p292', 'p304', 'p347', 'p314', 'p244', 'p261', 'p298', 'p272', 'p308', 'p299', 'p234', 'p268', 'p271', 'p316', 'p287', 'p318', 'p264', 'p313', 'p236', 'p238', 'p334', 'p312', 'p230', 'p253', 'p323', 'p361', 'p275', 'p252', 'p374', 'p286', 'p274', 'p254', 'p310', 'p306', 'p294', 'p326', 'p225', 'p255', 'p293', 'p278', 'p266', 'p229', 'p335', 'p281', 'p307', 'p256', 'p243', 'p364', 'p239', 'p232', 'p258', 'p267', 'p317', 'p284', 'p300', 'p288', 'p341', 'p340', 'p279', 'p330', 'p360', 'p285']


npy = get_files(path,".npy",recurse=True)
files = []

for i in npy:
    if "spec" in str(i) or i.parent.name not in seen_speakers:
        continue
    files.append(i)

test_files = files[:20]
eval_files = files[20:30]
train_files = files[30:]

train_list = []
eval_list  = []
test_list  = []

train_list.extend(train_files)
eval_list.extend(eval_files)
test_list.extend(test_files)

with open("train.list","w+") as train:
    for i in train_list:
        train.write(f"{i} 135 22\n")

with open("eval.list","w+") as eval:
    for i in eval_list:
        eval.write(f"{i} 135 22\n")

with open("test.list","w+") as test:
    for i in test_list:
        test.write(f"{i} 135 22\n")