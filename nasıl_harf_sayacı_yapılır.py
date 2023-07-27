#bu kaynak nasıl harf sayacı yapılır adlı videonun kaynağıdır
cümle="harf sayacı cümlenin içinde gezerek aradığım şeyi bulucak"
def harf_sayacı_metot1(cümle=str):
    for i in range(len(cümle)):
        if cümle[i]=="a": print("a bulyundu")

def harf_sayacı_metot2(cümle=str):
    cümle=list(cümle)
    for i in cümle:
        if i=="a": print("abulundu")

harf_sayacı_metot1(cümle)
harf_sayacı_metot2(cümle)
