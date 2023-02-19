---
title: Github pages 포스팅에 이미지 넣는 방법
toc: true
toc_sticky: true
comments: true
categories:
- blog
tags:
- jekyll
- image
- github pages
---
## 도입
Github pages와 jekyll 포스팅에 이미지를 넣는 방식이 생각보다 까다로워 보인다. 블로그 서비스들에서 제공하는 편집기와 같은 기능없이 마크다운 레벨에서 이를 처리해야하기 때문이다. 구글링을 통해 알아낸 ~~필자 기준에서 가장 쉬운~~ 방식을 정리해본다.

## Jekyll에서 이미지 넣기
이미지 크기를 별도로 조절하지 않는다면 다음과 같이 할 수 있다. 
```markdown
![내 사진](/assets/images/my_picture.jpg)
```
이때 마크다운 코드 내에 들어가는 이미지 주소는 github repository의 이미지 폴더 주소를 넣어줘야 한다. 나의 경우 `/assets/images` 폴더에 이미지가 들어가있어 위와 같이 코드가 작성되었다.

## 이미지 크기 조절하기
이미지 크기 조절은 마크다운 코드에서 조절하는 방식[^1]을 적용해보았으나 github pages에서 이를 처리하지 못하는 것을 시행착오를 통해 알 수 있었다. 이미지 크기 조절은 앞서 입력한 코드 뒤에`{:}`구문을 추가하는 방식으로 할 수 있다.
```markdown
![내 사진](/assets/images/my_picture.jpg){: width="300px" height="300px"}
```
위 코드에선 2차원(width와 height) 모두를 입력해주었지만 둘 중 하나만 입력해도 정상적으로 작동한다.(이 경우 원본 이미지의 비율이 유지된다.) 단위 또한 `px`이 아니라 `%`[^2]를 사용하더라도 문제없이 작동한다. 이를 적용하여 다음처럼 이미지 크기를 조절할 수 있다.
```markdown
![내 사진](/assets/images/my_picture.jpg){: width="30%"}
```

## 이미지 정렬하기
CSS에서 이미지 정렬에 사용할 class를 정의하고 이를 적용하는 다음과 같은 방식이 있는 것 같다. 
```markdown
![내 사진](/assets/images/my_picture.jpg){:class="img-responsive"}
```
더 간단한 방법을 찾아보고 있으나 당장 눈에 보이진 않는다. 더 알아보려니 귀차니즘이 발동하여 일단 다음으로 미루기로 한다.

## References
1. <https://www.seanosier.com/2021/03/19/resize-images-in-jekyll-markdown/>
2. <https://dev-notes.eu/2016/01/images-in-kramdown-jekyll/#comment-3298552281>

---
[^1]:예를들면, `![내 사진 | 200x](/assets/images/my_picture.jpg)`과 같이 입력하는 방식을 의미힌다.
[^2]:이때 `%`는 이미지 원본 크기에 대한 비율이 아니라 이미지 division에서 이미지가 차지하는 비율을 의미하는 점에 유의해야 한다.