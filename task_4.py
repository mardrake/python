'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
from words2num import w2n
from google_trans_new import google_translator

translator = google_translator()
with open("text_4.txt", 'r', encoding='utf-8') as text_4:
    for line in text_4:
        l = line.split()
        k = str(w2n(l[0]))
        with open("text_num.txt", 'a', encoding='utf-8') as text_num:
            trans_text = translator.translate(l[0], lang_tgt='ru')
            text_num.write(f"{trans_text+'-'+' '+k}\n")