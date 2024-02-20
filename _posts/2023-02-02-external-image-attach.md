---
title: Github pages 이미지를 외부 서버에 두는 방법
toc: true
toc_sticky: true
categories:
- blog
tags:
- github pages
- jekyll
- image
---
# 도입
[Github pages 포스팅에 이미지 넣는 방법](https://will2world.github.io/blog/inserting-image-github-pages-posting/)에서 포스팅에 이미지 넣는 법을 다루었다. 이때  blog repository에 이미지를 직접 업로드하고 repository 상 이미지의 상대주소[^1]를 활용하여 이미지를 삽입할 수 있었다. 이와 같은 방식은 다음과 같은 한계를 가진다.
1. 이미지는 blog repository의 용량을 사용한다. 그런데 Github 정책 상 무료 repository는 1GB[^2]로 용량이 제한된다. 따라서 포스팅에 이미지를 많이 사용하기가 부담스럽다.
2. 이미지를 일일이 업로드하고 각각에 대한 상대주소를 만들어서 포스팅 md 파일에 입력해줘야 한다. 그래서 귀찮고 번거롭다.

이런 한계는 장기적으로 보았을 때 문제가 될 수 있을 듯 하다. 특히나 이미지 용량이 크다면 1번이 치명적이다. 다행히 구글링을 통해 외부 저장소에 이미지를 업로드하고 블로그에 연동할 수 있는 세 가지 방식을 알게 되었다. 세 가지 모두 별도의 비용을 지불할 필요없이 활용할 수 있는 방식이다. 그 세가지 방식은 다음과 같다.
1. 구글 드라이브를 외부 저장소로 사용하기[^google]
2. 원드라이브를 외부 저장소로 사용하기
3. Github issue 이미지 첨부 활용하기

# ~~구글 드라이브를 외부 저장소로 사용하기~~
구글은 각 계정별로 15GB의 클라우드 저장소를 무료로 제공한다. 이를 블로그 포스팅에 사용할 이미지를 업로드하는 데 사용한다. 다음의 절차들은 구글 드라이브 desktop이 아닌 웹에서 수행해야 한다.
## Step 1 : 포스팅용 폴더 만들고 공유 설정하기
이미지들은 모든 사람에게 공개가 되어야 하므로 별도의 폴더를 하나 만들어준다. 폴더를 만들었으면 이어서 해당 폴더를 공유한다. 이때 빨간색 네모로 표시한 부분에서 처럼 모든 사람이 접근할 수 있도록 설정해줘야 한다. 그래야 모든 사람이 이미지를 볼 수 있다.

![2](https://user-images.githubusercontent.com/53478216/216277831-8251c096-1abf-4dd9-a594-a7a09cff527b.png)
## Step 2 : 이미지 업로드하기
이미지 폴더에 포스팅할 이미지 파일을 업로드한다. 필자는 `sample.jpg`라는 파일을 업로드 하였다.

![3](https://user-images.githubusercontent.com/53478216/216278322-b8464c81-bd15-4da1-a2e9-5fe1f82ecf4a.png){: width="50%"}
## Step 3 : 업로드한 이미지의 share 주소 중 이미지 ID 알아내기
업로드한 이미지를 우클릭하여 `공유(혹은 share)`를 선택한다. 그러면 그림과 같은 창이 뜨며 그 중 빨간색 네모로 표시한 버튼을 누르면 공유 주소가 복사된다.

![4](https://user-images.githubusercontent.com/53478216/216279761-f76f8d9e-1dc5-455c-8837-726c2516cef6.png)

공유 주소는 다음과 같은 형태를 가지고 있다. 공유 주소 중 `이미지 ID`만 복사해둔다.
```
https://drive.google.com/file/d/{이미지_ID}/view?usp=sharing
```

## Step 4 : 이미지 ID로부터 이미지 삽입용 주소 만들기
다음과 같은 형태로 이미지 삽입을 위한 코드를 만들어준다. 다음의 마크다운 코드에서 `{이미지_ID}`를 제거하고 앞서 복사해둔 이미지 ID를 넣어준다.
```markdown
![이미지_이름](https://drive.google.com/uc?id={이미지_ID})
```
## Step 5 : 포스팅 md 파일에 삽입하기
Step 4에서 생성한 코드를 포스팅에 삽입하면 그림이 입력된다. 다음 그림은 본 방식을 사용해서 삽입한 이미지이다.

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211945&authkey=%21ANebV7MGhzw40D4&width=960&height=720" width="960" height="auto" />

## 번외 : 파이썬으로 이미지 삽입 markdown 코드 생성 자동화 하기 
Step 1-5를 전부 수작업으로 하는 것은 굉장히 번거롭다. (이렇게 써야한다면 그냥 안쓰고 싶을 정도이다.)
다행히 여러 파일을 동시에 선택하고 한번에 공유링크를 생성할 수 있는 drive용 앱[^4]이 개발되어 있어 공유링크를 한번에 생성, 복사할 수 있다. (구글 드라이브 웹 자체에도 한번에 여러 파일의 공유링크를 생성하는 기능이 있지만 이미지들이 정렬되지 않은 상태로 링크를 생성하므로 어떤 이미지의 링크인지 특정하기 어렵다. 그래서 불가피하게 drive용 앱을 사용하였다.)

![화면 캡처 2023-02-02 194310](https://user-images.githubusercontent.com/53478216/216303472-426d74eb-2df5-4d95-974d-5ab3a3450e63.png)

![화면 캡처 2023-02-02 193807](https://user-images.githubusercontent.com/53478216/216302302-e35881ae-c261-4acf-aefd-4a8ffaaac131.png)

다음의 두 코드는 각 이미지에 대한 md 코드를 생성하는 파이썬 스크립트이다. `B 코드`는 수기로 이름을 입력해주는 번거로움은 있으나 출력된 md 코드가 이름에 따라 정렬되어 출력되어 더 유용하다.

```python
# A. 이미지 이름을 입력하지 않는 경우
head = '![image](https://drive.google.com/uc?id='
tail = ')'
file = './input.txt'

with open(file, 'r') as f:
    links = f.readlines()

with open('image_md_codes.txt', 'w') as f:
    for link in links:
        key = link.split('/')[5]
        embedLink = head + key + tail
        print(embedLink, file=f)
```
```python
# B. 이미지 이름을 수기로 입력하는 경우
head = '!['
middle = '](https://drive.google.com/uc?id='
tail = ')'
file = './input.txt'
names = [1,6,5,4,3,2] # bulk share url shortener에 입력된 순서대로 기입

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
```

위 두 스크립트의 입력, 출력 파일은 다음의 그림과 같다.

![input](https://user-images.githubusercontent.com/53478216/216304034-ba846cd7-26f0-4c44-a66d-51007178a824.png)

![output](https://user-images.githubusercontent.com/53478216/216304054-c4e1b6c7-443d-4b36-b4db-a26009bdba91.png)

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211944&authkey=%21AFgTxPVj6R-np2Q&width=627&height=289" width="627" height="auto" />

# 원드라이브를 외부 저장소로 사용하기
## Step 1 : 포스팅 폴더 생성 후 이미지 업로드하기
먼저 원드라이브의 원하는 위치에 포스팅에 사용할 이미지들을 담을 폴더를 생성하고 이미지를 업로드한다. 이떄 포스트별로 이미지 폴더를 따로 관리하는 편이 관리 면에서 좋을 것 같다.

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211966&authkey=%21AFvdoSZD6WypNlM&width=592&height=316" width="592" height="316" />

## Step 2 : 각 이미지 임베드 코드 따기
이미지를 우클릭하면 메뉴에 `임베드` 버튼이 보인다. 이를 클릭하면 임베드 메뉴가 페이지 우측에 나타난다.

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211967&authkey=%21ALSqLr-3n2QWsg0&width=360&height=667" width="360" height="667" />

임베드 메뉴에서 원하는 이미지 크기(그림의 1번 박스)를 선택하고 HTML 태그 포함(그림의 2번 박스)에 체크한다. 그 결과 생성된 이미지 URL(그림의 3번 박스)을 복사한다.

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211968&authkey=%21AEhyG9G8CLTPZds&width=325&height=655" width="325" height="655" />

## Step 3 : 포스팅 md 파일에 삽입하기
복사한 이미지 임베드 URL을 포스팅 md 파일의 원하는 위치에 삽입한다. 그 결과 블로그 포스팅에 이미지가 출력된다.

<img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211969&authkey=%21AAetjoEzYIoNNQ0&width=820&height=130" width="820" height="130" />

# Github issue 이미지 첨부 활용하기
작성 중

---
[^1]: `/assets/images/image_name.jpg`와 같은 상대주소를 사용하였다.
[^2]: 최대 5GB까지는 허용한다고 되어있으며(2023년 정책 기준) 초과 시 경고 메일을 받을 수 있다고 한다. 자세한 내용은 [용량 관련 stackoverflow](https://stackoverflow.com/questions/38768454/repository-size-limits-for-github-com)와 [github 공식문서](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#repository-size-limits)에서 확인할 수 있다.
[^4]: `Bulk share url shortener`를 사용하였다.
[^google]: 2023년 10월 구글의 정책이 변경됨에 따라 본 방식은 사용이 불가해졌다.