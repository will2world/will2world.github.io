 # %%
if __name__ == "__main__":
    head = '[!['
    middle1 = ']('
    middle2 = 'https://drive.google.com/uc?id='
    tail1 = ')]('
    tail2 = '){:target="_blank"}'

    file = './input.txt'
    names = [1, 2, 3.1, 3.2, 4.1, 4.2, 4.3, 4.4, 5, 6, 7.1, 7.2, 8, 9.11, 9.1, 9.2, 10, 11, 12] # bulk share url shortener에 입력된 순서대로 기입
    names = list(map(str, names))
    with open(file, 'r') as f:
        links = f.readlines()

    result = []
    for name, link in zip(names, links):
        id = link.split('/')[5]
        mergedLink = middle2 + id
        embedLink = head + name + middle1 + mergedLink + tail1 + mergedLink + tail2
        result.append(embedLink)
    result.sort()

    with open('image_md_codes_with_name.txt', 'w', encoding='UTF-8') as f:
        for mdCode in result:
            print(mdCode, file=f)

# %%
