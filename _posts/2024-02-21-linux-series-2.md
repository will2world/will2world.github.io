---
title: \[리눅스 정착기 시리즈\] 2. 리눅스에서 한글 사용하기 - 한글 입력기 및 한글 깨짐 해결하기 
toc: true
toc_sticky: true
categories:
- linux_series
tags:
- linux
- Korean_IME
- Korean font
---

# 리눅스에서 한글을 사용하기 위해 필요한 것들
대부분의 배포판 리눅스는 한글을 완벽하게 사용할 수 있는 상태로 설치되지 않는다.
예를 들어 한글을 표시하기 위한 폰트가 내장되어 있지 않아 웹 상에 존재하는 한글이 이상하게 표시되며 한글이 입력되지 않는다.
많은 사람들은 이와 같은 상황을 마주하면 곧바로 리눅스 사용을 포기해버리고 원래 사용하던 OS로 돌아가곤 한다.

리눅스에서 한글을 온전하게 사용하기 위해서는 두 가지를 설치해주면 된다.
1. 한글 입력을 지원하는 Input method editor(IME)
2. 한글 폰트

본 포스팅에서는 IBus를 사례로 한글 환경을 구축하는 방식을 설명한다.

# IME 설치하고 설정하기
## IME들 중 원하는 것 선택하기
IME는 한 가지만 있는 것이 아니다.
그 목록은 [아치위키-IME 목록](https://wiki.archlinux.org/title/Input_method#List_of_available_input_method_editors) 중 Korean 항목을 보면 된다.
이들 중 본인이 원하는 한 가지를 선택하여 설치를 해주면 된다.
리눅스가 처음이라면 `IBus`를 추천한다.

<p align='center'>
    <img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211974&authkey=%21AJBfF4j5SyLgs5g&width=1062&height=139" width="auto" height="auto" />
</p>

리눅스 배포판 중 일부는 이들 IME 중 하나를 내장하고 있는 경우가 있다.
예를들어 우분투와 같은 GNOME desktop environment(DE)는 IBus를 내장하고 있다.
이 경우 내장된 IME를 사용하면 된다.

## 선택한 IME 설치하기
설치한 리눅스 공식 repository로부터 해당 IME를 설치한다.
이때 일반적으로 IME 패키지 자체에 한국어 라이브러리를 내장하고 있지 않으므로 이것도 함께 설치해야 한다.
예를들면 IBus는 다음의 두 가지 패키지를 설치해야 한다.
1. ibus
2. ibus-hangul

<p align='center'>
    <img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211975&authkey=%21AA0ER-4xO1fyUog&width=1062&height=139" width="auto" height="auto" />
</p>

IME를 내장하고 있는 배포판의 경우는 한국어 라이브러리만 추가로 설치해주면 된다.
예를들어 IBus는 ibus-hangul만 추가로 설치한다.

## 설치한 IME를 환경변수에 등록하기
환경변수에 IME를 저장해둠으로써 다른 프로그램들이 입력기를 인지할 수 있도록 만드는 작업이 필요하다.
이를 위해 sudo 권한으로 `/etc/environment` 파일을 열고 다음과 같은 내용을 입력하고 저장한다.
이때 설치한 IME가 ibus가 아니라면 설치한 IME 이름을 ibus 자리에 입력해준다.

```sh
GTK_IM_MODULE=ibus
QT_IM_MODULE=ibus
XMODIFIERS=@im=ibus
```
혹시 사용하는 terminal emulator가 `kitty`나 `alacritty`라면 다음 내용까지 함께 추가해주어야 터미널에서 한글입력이 가능하다.

```sh
GLFW_IM_MODULE=ibus
```

## IME 데몬을 시작 프로그램으로 등록하기
본인이 사용하는 리눅스 배포판에 맞는 [autostart 방법](https://wiki.archlinux.org/title/Autostarting)을 통해 IME 데몬이 자동시작 되도록 설정한다. IBus의 경우 다음과 같은 command를 사용한다.
```sh
ibus-daemon -rxRd
```

## IME의 설정에서 한글 키보드 등록 및 한영전환 방식 설정하기
우리가 사용할 키보드는 영어와 한글 두 가지이나 기본적으로 영어 키보드만 사용하도록 설정되어 있다.
따라서 한글 키보드를 추가해주고 전환 방식을 설정해줘야 한다.
IBus의 경우 다음의 그림에서처럼 add 버튼을 눌러 `Hangul`로 검색되는 키보드를 추가해주고 영어 키보드는 제거한다.
키보드를 `Hangul`만 둔 것은 자체적으로 영어를 지원하기 때문이다.

<p align='center'>
    <img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211977&authkey=%21AHirGkp3w19XtC8&width=737&height=498" />
</p>

추가한 뒤에는 `Preferences`를 눌러 한영 전환키를 설정한다.
그림에서는 `Shift+Space`를 한영전환에 사용하도록 설정한 모습을 보여준다.

<p align='center'>
    <img src="https://onedrive.live.com/embed?resid=CFD7A556C71EAC85%211976&authkey=%21AJXU8ic3SDm5qmk&width=1174&height=533" />
</p>

## 재부팅
모든 작업이 끝난 후 재시작하면 된다.
재시작 후 한글 입력이 잘 되지 않는 경우 위의 작업들을 차근차근 다시 확인해보고 빠진 부분을 해결하면 된다.

# 한글 폰트 설치하기
리눅스를 갓 설치한 경우라면 한글 폰트가 없어 한국어 웹 페이지의 글꼴이 깨져서 출력된다.
이는 폰트만 설치해주면 간단하게 해결할 수 있다.
보통 사용하는 리눅스의 공식 repository에 한글 폰트가 존재한다.
배포판마다 명칭이 다르긴 하나 noto font 계열 중 `noto-fonts-cjk` 폰트를 설치해주면 된다.
데비안 계열에서는 `fonts-noto-cjk`라는 이름으로, 아치 계열에서는 `noto-fonts-cjk`라는 이름으로 배포되고 있다.
설치가 완료되면 한글 웹 페이지가 정상적으로 출력되는 것을 확인할 수 있다.

# Wayland에서의 한글 문제
본 포스팅은 wayland가 아니라 xorg를 사용하는 것을 전제로 작성하였다.
xorg는 본 포스팅의 방식을 사용하면 한글을 문제없이 사용할 수 있다.

wayland의 경우 한국인 개발자분이 개발하고 있는 Kime 입력기를 사용하면 웹 서핑이나 터미널 작업에서 한글 입력이 가능하다.
그러나 vs code와 같이 electron에 기반한 특정 앱을 wayland native로 실행할 경우 한글 입력이 되지않는 문제가 여전히 존재한다(24년 2월 기준).
사무실에서 리눅스를 사용하는 필자는 이런 불완전성으로 인해 현재 xorg를 사용하고 있다.

# 참고자료
- [Arch wiki - Localization/Korean](https://wiki.archlinux.org/title/Localization/Korean)
- [Arch wiki - IBus](https://wiki.archlinux.org/title/IBus)
- [Arch wiki - autostarting](https://wiki.archlinux.org/title/Autostarting)
- [Arch wiki - input method](https://wiki.archlinux.org/title/Input_method)
- [Kime](https://github.com/Riey/kime)