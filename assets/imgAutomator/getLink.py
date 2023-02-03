 # %%
if __name__ == "__main__":
    head = '!['
    middle = '](https://drive.google.com/uc?id='
    tail = ')'

    file = './input.txt'
    names = ['reesult_withname'] # bulk share url shortener에 입력된 순서대로 기입
    names = list(map(str, names))
    with open(file, 'r') as f:
        links = f.readlines()

    result = []
    for name, link in zip(names, links):
        id = link.split('/')[5]
        embedLink = head + name + middle + id + tail
        result.append(embedLink)
    result.sort()

    with open('image_md_codes_with_name.txt', 'w', encoding='UTF-8') as f:
        for mdCode in result:
            print(mdCode, file=f)

# %%
