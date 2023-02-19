---
title: 파이썬 코딩 환경 설정하기 (입문자를 위한 순한맛)
toc: true
toc_sticky: true
categories:
- coding
tags:
- python
---
## 도입
코딩과 인공지능에 대한 인기가 높아지면서 많은 사람들이 파이썬을 찾는 것 같다. 아마 그들 중 대다수는 코딩을 처음 접하기 때문에 코딩환경 설정에 어려움을 겪지 않을까 싶다. 그래서 설치에 필요한 기본 개념들을 간단하게 설명하고, 설치 과정을 차근차근 설명해보고자 한다.

~~개념은 머리아프니까 스킵하고~~ 코딩 환경 설정 방법만 알고싶다면 [파이썬 코딩환경을 설정하는 두 가지 방식](#파이썬-코딩환경을-설정하는-두-가지-방식)부터 읽으면 된다.

## 기본 개념
### 가상환경(Virtual environment)
파이썬을 사용하다보면 pip나 conda를 통해 많은 패키지를 설치하게 된다. 그러다보면 어느 순간 각 패키지들 사이의 호환성이 꼬이는 문제가 발생한다. 이런 호환성 문제는 하나를 해결하면 또 다른 패키지에서 문제가 생기는 등 해결하기가 여간 까다로운 게 아니다. 특히나 여러 프로젝트를 동시에 수행할때 이런 호환성 문제가 빈번하게 발생한다. `1번 프로젝트`에서는 잘 돌아가는데 `2번 프로젝트` 코드를 실행했더니 버전이 맞지 않아 수행이 되지 않는다거나, `2번 프로젝트`를 수행하는 중 어떤 패키지 하나를 깔았는데 잘 돌아가던 `1번 프로젝트` 코드가 실행이 안된다거나 하는 문제가 이에 해당한다.

이와 같은 문제를 원천적으로 예방하기 위해 사용하는 기술이 `가상환경(Virtual environment)`이다. 비유하자면 각각의 프로젝트마다 `개인방`을 주는 것이다. 각 프로젝트는 `개인방`을 가지게 되고 거기에 각자 필요한 버전의 python, 필요한 package를 설치하고 활용하게 된다. 이때 `개인방`들은 서로 독립적으로 존재하므로 서로 간에 영향을 미치지 못한다.

이와 같은 `가상환경`을 만드는 방식에는 대표적으로 세 가지가 있다.
1. python에서 제공하는 venv를 활용하는 방법
2. virtualenv 패키지를 활용하는 방법
3. conda를 활용하는 방법

아나콘다를 통해 파이썬을 설치했다면 3번 방식을 사용하는 편이 좋아보인다. 그렇지 않다면 1번이나 2번 방식을 사용해야 한다.

### 패키지 관리자(conda, pip)
파이썬으로 코드를 짜다보면 다른 사람들이 만들어둔 패키지를 가져와서 사용하게 된다. 이때 필요한 패키지를 검색하고, 특정 패키지를 설치하고, 설치된 패키지 목록을 확인하고, 불필요한 패키지를 삭제하는 기능을 하는 프로그램이 `패키지 관리자`이다. conda[^1]와 pip가 이에 해당된다. (Windows에서 설치된 앱 관리 페이지와 같은 기능을 한다. 단, GUI가 아니라 CLI라는 점에서 차이는 있다.)

conda로 환경을 설치했다면, 대부분의 패키지는 conda를 통해 설치할 수 있으나 어떤 패키지는 pip로만 설치되는 경우도 있긴하다. (그래서 결국 둘 모두의 사용법에 익숙해진다.)

### Conda vs. Miniconda vs. Anaconda
공통적으로 conda를 가지며 여기에 필요하다고 생각되는 package들을 붙여서 만든 것이 Miniconda와 Anaconda라고 보면된다. 그 포함관계는 다음과 같다.

$$ Conda \subset Miniconda \subset Anaconda $$

파이썬이 처음이라면 Anaconda를 설치하는 것을 추천한다.

### 코드는 어디서 작성하는가? IDE에서
파이썬을 설치했다면 코드를 작성하고 실행해야 한다. 그럼, 파이썬 코드는 어디서 작성하고 실행하는가? Integrated Development Environment(IDE)에서 작성 및 실행할 수 있다. 대표적으로 다음과 같은 IDE가 있다.[^ide_ranking]
1. Visual Studio Code(VS code)
2. PyCharm
3. Spyder
4. Jupyter

이들 중 원하는 것을 선택하고 설치한 뒤 사용하면 된다. 설치는 각각의 프로그램 홈페이지의 설치 절차를 따라가면 된다. 필자는 이들 중 VS code를 메인으로 사용하고 있다.

이들 중 무엇을 써야할 지 모르겠다면 VS code를 추천한다. 처음에 설정하는게 조금 까다롭지만 시간이 지나 돌아보면(여러 개의 가상환경을 갖추고 코딩을 하게 되고, 서버컴퓨터에 원격으로 연결하여 코딩, 디버깅하는 때가 오면) 굉장히 잘한 선택이라고 생각하게 된다.

## 파이썬 코딩환경을 설정하는 두 가지 방식
파이썬 코딩환경을 설정하는 방식은 크게 두 가지다.
1. 직접 python을 설치한 뒤 pip로 필요한 패키지를 설치하는 방식
2. Anaconda(혹은 miniconda)를 통해 python을 설치하는 방식

`1번 방식`은 파이썬을 설치하고 필요한 패지키들은 pip를 통해 하나씩 설치하는 방식이다. Anaconda나 Miniconda와 달리 기본 패키지들을 한번에 설치해주지 않으므로 하나씩 설치해주어야 한다. 또한 Command line에서 사용할 수 있도록 환경변수를 직접 설정해주어야 한다. 필요한 것들만 추려서 설치할 수 있겠으나 파이썬 코딩환경 설정이 처음이라면 어려운 방식이라 추천하지 않는다.

`2번 방식`은 Anaconda를 설치함으로써 python 뿐만 아니라 기본적으로 많이 사용되는 패키지들까지 한번에 설치하는 방식이다. 이후 conda를 통해 원하는 패키지를 추가로 설치해주면 된다.

파이썬 코딩환경 설정이 처음이라면 2번 방식을 추천한다.

## 파이썬 코딩환경 설정 - 2번 방식
앞서 설명한 두 가지 방식 중 좀 더 쉬운 2번 방식을 통해 파이썬 코딩환경을 설정하는 방식에 대해 설명한다.
### Step 1 : Anaconda (혹은 miniconda) 다운로드
Anaconda 혹은 Miniconda 중 원하는 것을 선택하고 본인 PC의 사양에 맞는 설치파일을 다운로드 한다. 공식 다운로드 페이지는 다음과 같다.
- [Anaconda 공식 다운로드 페이지](https://www.anaconda.com/products/distribution)
- [Miniconda 공식 다운로드 페이지](https://docs.conda.io/en/latest/miniconda.html)

![1](https://drive.google.com/uc?id=1fSSUEKpg_pLlb_FXCDrhj99QleTZQZ_O)

![2](https://drive.google.com/uc?id=19jVN1DnQMNSOU7Ny52VafuGOBMuM7V7s)


### Step 2 : Anaconda (혹은 miniconda) 설치
#### 설치하기
`Step 1`에서 다운로드한 설치파일을 실행하여 설치한다. 설치 과정에 뜨는 선택사항들은 기본설정 그대로 두고 전혀 문제될 것이 없다. 그냥 Next만 눌러주며 설치를 끝낸다.

![3.1](https://drive.google.com/uc?id=1xWwGLM6ppZtz4MjALtrzxbnIKOc9d2tg)

![4.1](https://drive.google.com/uc?id=1c4g6qaLyRY9ZlBsb7gNmQKUYxVsm51RY)


#### 설치가 잘 되었나 확인하기
잘 설치가 되었다면 다음과 같이 윈도우 시작버튼을 누르고 `anaconda`라고 검색했을 때 `Anaconda Prompt (anaconda3)` 혹은 `Anaconda Prompt (miniconda3)`가 검색된다. 이를 클릭하여 실행해준다.

![4.3](https://drive.google.com/uc?id=1XhrXhy_xlqlAYAx156nQUYB4uW2NOf44)

실행된 Prompt에 보면 `(base)`라는 표시가 있는 것을 확인할 수 있다. 여기에 다음과 같이 입력해보면 conda와 python 버전을 확인할 수 있다. 
```sh
conda --version
```
```sh
python --version
```
이들 모두가 정상적으로 확인된다면 설치가 잘 된 것이다.

[![4.4](https://drive.google.com/uc?id=1mKytUr-Eo4Zh62wjT9ZgPYNRRbyGpkaH)](https://drive.google.com/uc?id=1mKytUr-Eo4Zh62wjT9ZgPYNRRbyGpkaH){:target="_blank"}


### Step 3 : IDE 설치 - VS code
Anaconda 혹은 Miniconda가 설치되었으면 이어서 원하는 IDE를 설치한다. 해당 IDE의 공식홈페이지의 설치 가이드를 따라 설치할 수 있다. 본 포스팅에서는 VS code를 기준으로 설명한다. VS code의 공식 다운로드 페이지는 다음과 같다.

- [VS code 공식 다운로드 페이지](https://code.visualstudio.com/)

![5](https://drive.google.com/uc?id=1nkWlbJZqtxVoj_Ipc1p7eIGXVkx72tU8)

VS code 역시 그냥 다음 다음 넘어가면서 기본 설정으로 설치를 한다.

![6](https://drive.google.com/uc?id=1I_fXmfWwV7hOyyG8onRWKHXh1GtVhk8I)

### Step 4 : Python을 위한 IDE 설정 - VS code
#### Python Extension 설치하기
VS code는 막 설치된 상태에서는 그냥 메모장과 같은 상태이다. (스마트폰을 처음 구입하면 기본 계산기나 달력말곤 없는 것과 비슷하다.) 지금 상태에서는 코드를 실행할 수도 디버깅을 할 수도 없다. 그래서 내가 원하는 언어에 필요한 앱들(Extensions)을 깔아주어야 한다. 우리는 파이썬 코딩을 할 것이므로 `Python Extension`을 설치해준다. VS code 좌측의 Extension 버튼을 누르고 Python을 검색하면 Microsoft에서 제작한 Python extension이 검색된다. 이를 설치한다. 

![7.1](https://drive.google.com/uc?id=1sPghcCJovli3x0EgFqPh_MWbrojnyoJM)

설치가 끝나면 아래 그림처럼 나타난다.

[![7.2](https://drive.google.com/uc?id=1CLqInon4F3MHSvOcWDqC22hesqe9_x-u)](https://drive.google.com/uc?id=1CLqInon4F3MHSvOcWDqC22hesqe9_x-u){:target="_blank"}

#### Python Interpreter 선택하기
한 PC에 여러 버전의 파이썬이 존재할 수 있다. 예를들어 가상환경을 5개 구축해서 각각 다른 프로젝트의 코딩을 진행하고 있다면 각 가상환경별로 각기 다른 버전의 파이썬이 설치되어 있을 수 있다.
그러나 VS code는 한 개만 설치된다. 그래서 VS code는 여러 개의 파이썬 중 원하는 것을 선택하고 코딩할 수 있도록 해준다. 그림에 빨간색 박스로 표시된 `interpreter select 버튼`을 누르면 현재 사용 가능한(설치된) 파이썬 Interpreter들이 나오고 그들 중 원하는 것을 선택할 수 있다. (현재는 Anaconda에 설치된 'base' 한 개의 파이썬만 존재하므로 한 개만 표시되고 있다.)

[![8](https://drive.google.com/uc?id=1s7eXArLYuDLa18DYrkiFgEOPrtlri4GQ)](https://drive.google.com/uc?id=1s7eXArLYuDLa18DYrkiFgEOPrtlri4GQ){:target="_blank"}

#### Working directory 선택하기
특정 프로젝트의 코드들을 저장할 폴더를 생성하고 해당 폴더를 Working directory로 설정한다. 그럼 왼쪽 Explorer 탭에 해당 폴더가 표시되는 것을 볼 수 있다. author 관련한 창이 뜨면 `Yes, I trust the authors`를 눌러준다.

![9.1](https://drive.google.com/uc?id=1ivGITpP3e_-y-PCwykLtYbyKFjioEDEh)

![9.2](https://drive.google.com/uc?id=1VCG3Oxj1U9vKwDQX6-eeGBdAkq9NwJCb)

### Step 5 : 코드 작성하고 실행하기
#### Code 파일 생성하고 작성하기
Explorer 탭에서 우클릭을 하면 새 파일을 생성할 수 있다. 원하는 이름으로 파일을 생성하되 확장자로 `.py`를 붙여준다.[^3] 그러면 파이썬 스크립트 파일이 생성된다. 해당 스크립트에 원하는 코드를 작성하면 된다.

#### 코드 실행하기
##### Jupyter Notebook 방식으로 (cell 단위로) 코드 실행하기
VS code의 파이썬 Extension을 기본적으로 Jupyter notebook과 같이 사용할 수 있다. 원래 Jupyter notebook은 Jupyter 서버를 켜고 크롬 등을 통해 해당 서버에 접속하여 코딩을 해야 한다. 그러나 VS code에서는 Jupyter extension이 알아서 이 작업을 수행하므로 우리는 이를 신경쓰지 않아도 된다. 단지 Jupyter notebook 코드 cell을 만들고 각 cell 단위로 코드를 작성, 실행하기만 하면 된다.

코드 cell은 `#%%`를 입력함으로써 생성할 수 있다. 생성된 cell 상단에는 `Run cell`, `Run below`, `Debug cell`이라는 버튼이 생긴다. 여기에 코드를 작성하고 `Run cell`을 눌러(혹은, 해당 셀에 커서를 두고 `Ehift+Enter`를 눌러) 셀 단위의 코드를 실행해볼 수 있다.

![11](https://drive.google.com/uc?id=1j_X-UJQC4p2wf_Ay-ttP3dA2GcZ_fnP_)

실제 작성된 코드 셀을 실행하면 다음처럼 Interactive 창이 생기면서 실행된 결과가 출력된다.

[![10](https://drive.google.com/uc?id=1asr87PaqE8PAq4TyznmBjnFPwTcNFp50)](https://drive.google.com/uc?id=1asr87PaqE8PAq4TyznmBjnFPwTcNFp50){:target="_blank"}

##### 정석(Command line 방식)으로 코드 실행하기
작성한 스크립트 파일을 Command line 환경에서 사용할 예정이라면 정석으로 py 스크립트 파일을 실행해 볼 필요가 있다. 이 때는 VS code 메뉴의 `Run-Start Debugging` 혹은 `Run-Run Without Debugging`을 활용한다. 이를 누르면 다음의 그림과 같이 VS code창 하단의 Terminal에서 전체코드(.py파일 자체)가 실행되는 것을 볼 수 있다.

[![12](https://drive.google.com/uc?id=1Q7yrBC7H9jSJzKVYFCP36NLQugWXZ4SV)](https://drive.google.com/uc?id=1Q7yrBC7H9jSJzKVYFCP36NLQugWXZ4SV){:target="_blank"}

이는 Anaconda prompt(terminal)에 다음의 명령어를 수행한 것과 동일하다. 단, 이 방식은 `Run Without Debugging`과 같이 실행만 한다.
```sh
python ~/workingDir/helloWorld.py
```

## 마치며
파이썬 코딩환경 설정과 관련한 기본 개념들을 정리하고 코딩환경을 설정하는 방식에 대해 설명하였다. 최대한 자세히 풀어서 설명한 것 같다.
본문에 나온 링크들은 나중에 시간이 지나면 달라질 수 있으므로 변경된 내용은 구글링을 통해 찾아갈 수 있을 것이라 생각한다.

다음 포스팅은 아마 `Conda 기초 사용법`과 `가상환경을 다루는 방법`이 되지 않을까 싶다.

---
[^1]: 정확히 말하면 conda는 `패키지 관리자 + 환경 관리 프로그램`이다.
[^ide_ranking]:  이외에도 더 다양한 종류의 IDE가 있다. 궁금하면 [12 Best Python IDE](https://www.softwaretestinghelp.com/python-ide-code-editors/)를 참조하면 된다.
[^3]: 확장자를 `.ipynb`로 지정하여 주피터 노트북 스크립트를 생성하면 Jupyter notebook과 완전히 동일한 환경에서 코딩하는 것이 가능하다. 그러나 `.py`로 생성해도 Jupyer notebook의 기능을 동일하게 사용할 수 있으므로 굳이 `.ipynb`로 생성할 필요는 없어보인다.