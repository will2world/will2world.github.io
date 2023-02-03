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
## 도입
[Github pages 포스팅에 이미지 넣는 방법](https://will2world.github.io/blog/inserting-image-github-pages-posting/)에서 포스팅에 이미지 넣는 법을 다루었다. 이때  blog repository에 이미지를 직접 업로드하고 repository 상 이미지의 상대주소[^1]를 활용하여 이미지를 삽입할 수 있었다. 이와 같은 방식은 다음과 같은 한계를 가진다.
1. 이미지는 blog repository의 용량을 사용한다. 그런데 Github 정책 상 무료 repository는 1GB[^2]로 용량이 제한된다. 따라서 포스팅에 이미지를 많이 사용하기가 부담스럽다.
2. 이미지를 일일이 업로드하고 각각에 대한 상대주소를 만들어서 포스팅 md 파일에 입력해줘야 한다. 그래서 귀찮고 번거롭다.

이런 한계는 장기적으로 보았을 때 문제가 될 수 있을 듯 하다. 특히나 이미지 용량이 크다면 1번이 치명적이다. 그래서 다른 방식들을 조사하여 외부 저장소에 이미지를 업로드하는 세 가지 방식을 알게 되었다. 세 가지 방식 모두 지금 당장 무료로 활용할 수 있는 방식이다.

## 구글 드라이브를 외부 저장소로 사용하기
구글 계정만 있으면 무료로 15GB의 클라우드 저장소를 사용할 수 있다. 이 저장소를 블로그 포스팅에 사용할 이미지를 업로드하는 데 사용한다. 다음의 절차들은 구글 드라이브 desktop이 아닌 웹에서 수행해야 한다.
### Step 1 : 포스팅용 폴더 만들고 공유 설정하기
이미지들은 모든 사람에게 공개가 되어야 하므로 별도의 폴더를 하나 만들어준다. 폴더를 만들었으면 이어서 해당 폴더를 공유한다. 이때 빨간색 네모로 표시한 부분에서 처럼 모든 사람이 접근할 수 있도록 설정해줘야 한다. 그래야 이미지를 볼 수 있다.

![2](https://user-images.githubusercontent.com/53478216/216277831-8251c096-1abf-4dd9-a594-a7a09cff527b.png)
### Step 2 : 이미지 업로드하기
이미지 폴더에 포스팅할 이미지 파일을 업로드한다. 필자는 `sample.jpg`라는 파일을 업로드 하였다.

![3](https://user-images.githubusercontent.com/53478216/216278322-b8464c81-bd15-4da1-a2e9-5fe1f82ecf4a.png){: width="50%"}
### Step 3 : 업로드한 이미지의 share 주소 중 이미지 ID 알아내기
업로드한 이미지를 우클릭하여 `공유`를 선택한다. 그러면 그림과 같은 창이 뜨며 그 중 빨간색 네모로 표시한 부분의 버튼을 누르면 공유 주소가 복사가 된다.

![4](https://user-images.githubusercontent.com/53478216/216279761-f76f8d9e-1dc5-455c-8837-726c2516cef6.png)

공유 주소는 다음과 같은 형태를 가지고 있다. 공유 주소 중 `이미지 ID`만 복사해둔다.
```
https://drive.google.com/file/d/{이미지_ID}/view?usp=sharing
```

### Step 4 : 이미지 ID로부터 이미지 삽입용 주소 만들기
다음과 같은 형태로 이미지 삽입을 위한 코드를 만들어준다. 다음의 마크다운 코드에서 `{이미지_ID}`를 제거하고 앞서 복사해둔 이미지 ID를 넣어준다.
```markdown
![이미지_이름](https://drive.google.com/uc?id={이미지_ID})
```
### Step 5 : 포스팅 md 파일에 삽입하기
Step 4에서 생성한 코드를 포스팅에 삽입하면 그림이 입력된다. 다음 그림은 본 방식을 사용해서 삽입한 이미지이다.

![image](https://drive.google.com/uc?id=1VM9ljPWkttQjW6RG4zTVE6hODDjo8FnS)

### 번외 : 파이썬으로 이미지 삽입 markdown 코드 생성 자동화 하기 
구글 드라이브를 사용하는 방식은 굉장히 번거롭다.
다행히 여러 파일을 동시에 선택하고 한번에 공유링크를 생성할 수 있는 drive용 앱[^4]이 개발되어 있어 공유링크를 한번에 생성, 복사할 수 있다.

구글 드라이브 웹 자체에도 한번에 여러 파일의 공유링크를 생성하는 기능이 있지만 이미지들이 정렬되지 않은 상태로 링크를 생성하므로 어떤 이미지의 링크인지 특정하기 어렵다. 그래서 불가피하게 drive용 앱을 사용하였다.

![화면 캡처 2023-02-02 194310](https://user-images.githubusercontent.com/53478216/216303472-426d74eb-2df5-4d95-974d-5ab3a3450e63.png)

![화면 캡처 2023-02-02 193807](https://user-images.githubusercontent.com/53478216/216302302-e35881ae-c261-4acf-aefd-4a8ffaaac131.png)

다음의 코드는 각 이미지에 대한 md 코드를 생성하는 파이썬 스크립트이다. 복사한 공유링크를 txt 파일에 저장하고 다음의 파이썬 스크립트에 입력으로 주면 각 이미지에 대한 md 코드가 있는 txt 파일이 생성된다. 출력 txt 파일 각 줄의 md 코드를 포스팅의 원하는 위치에 삽입하면 된다.
```python
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

해당 스크립트의 입력, 출력 파일은 다음의 그림과 같다.

![input](https://user-images.githubusercontent.com/53478216/216304034-ba846cd7-26f0-4c44-a66d-51007178a824.png)

![output](https://user-images.githubusercontent.com/53478216/216304054-c4e1b6c7-443d-4b36-b4db-a26009bdba91.png)


## 원드라이브를 외부 저장소로 사용하기
작성 중
## Github issue 이미지 첨부 활용하기
작성 중

[^1]: `/assets/images/image_name.jpg`와 같은 상대주소를 사용하였다.
[^2]: 최대 5GB까지는 허용한다고 되어있으며(2023년 정책 기준) 초과 시 경고 메일을 받을 수 있다고 한다.
[^4]: Bulk share url shortener를 사용하였다.