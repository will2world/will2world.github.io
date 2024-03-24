---
title: \[리눅스 정착기 시리즈\] 5. 프로그램 설치하기 - flatpak 사용하기
toc: true
toc_sticky: true
categories:
- linux_series
tags:
- linux
- packages
---
# flatpak이 무얼하는 것인고?
다음의 영상은 flatpak에서 공식적으로 제작한 홍보 영상이다.
그림과 키워드 위주로만 보아도 충분히 무슨 말을 하는지 이해할 수 있다.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jDVCITRWGgs?si=m-oP52ZKvyokm-ZY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

위 영상에서의 핵심 키워드들은 다음과 같다.
1. 수많은 linux distributions
2. 컨테이너 기술
3. Newest version
4. Flathub

정리하자면, 리눅스는 `수많은 종류의 distribution들`이 존재하고 이들 배포판들은 저마다 다른 구동환경을 가지고 있다. 
따라서 개발자 입장에서 이들 모두에 대해 앱을 관리하는 것은 여간 까다로운 일이 아니다.
그래서 `컨테이너 기술`을 사용하여 앱들을 동일한 구동환경에서 실행될 수 있도록 포장하고 사용자들에게 배포할 수 있도록 하는 서비스가 flatpak이다.

사용자 입장에서 Flatpak의 좋은 점은 `Newest version`의 앱들을 다운로드할 수 있다는 점이다.
일반적으로 distribution의 repository에 업로드 되어있는 앱들은 그 안정성이 확인된 버전이기 때문에 최신버전이 아닌 경우가 더 많다.
사용자에 따라서는 최신버전을 사용하고 싶을 수도 있는데, 이 경우 flatpak이 좋은 선택이 될 수 있다.

Flatpak은 자체적으로 앱스토어와 같은 기능을 하는 웹페이지를 운영하는데 그것이 `Flathub`이다.
Flathub에서 원하는 앱을 찾을 수 있으며 설치를 위한 터미널 명령어를 확인할 수 있다.

# flatpak을 설치하고 사용하는 방법
## flatpak 설치하기
flathub은 현재 사용하고 있는 배포판에 따라 조금씩 차이가 있다.
그래서 각 배포판별 설치 방법에 따라 설치해야 한다.
각 배포판에 대한 설치 방법은 [Flathub setup 페이지](https://www.flatpak.org/setup/)에서 원하는 배포판을 선택함으로써 확인할 수 있다.

데비안을 사용하는 경우 데비안 마크를 클릭하면 다음과 같은 설치 방법을 확인할 수 있다.

## flathub에서 원하는 앱 검색하고 설치하기
원하는 앱을 [flathub](https://flathub.org/)에서 검색하면 설치를 위한 터미널 명령어를 확인할 수 있다.
예를들어 obsidian을 설치하고자 하는 경우 다음과 같은 설치 명령어를 사용하여 설치한다.
```bash
flatpak install flathub md.obsidian.Obsidian
```
## flatpak으로 설치된 앱 실행하기
설치된 앱은 배포판의 런처를 통해 실행할 수 있다.
터미널로 flatpak 앱을 실행할 때는 다음과 같은 터미널 명령어를 통해 실행할 수 있다. (이름이 복잡하다는 점이 조금은 불편해 보인다.)
```bash
flatpak run md.obsidian.Obsidian
```
## flatpak으로 설치된 앱의 목록 확인하기
설치된 앱이 무엇이 있나 확인하고 싶거나 혹은 터미널로 실행하기 위한 bash alias를 생성하고자 앱의 복잡한 이름(md.obsidian.Obsidian과 같은 복잡한 이름 말이다.)을 확인하고 싶을 때가 있다.
이 경우 다음의 명령어를 사용한다.
```bash
flatpak list
```
## flatpak으로 설치된 앱 제거하기
설치된 앱을 제거할 때는 다음의 명령어를 사용한다. 이때 앱의 이름은 위 flatpak list를 통해 확인한 복잡한 이름을 사용해야 한다.
```bash
flatpak remove md.obsidian.Obsidian 
```

## 파일시스템 접근 권한 부여하기
앱에 따라 usb에 접근해야하는 경우가 종종 있다.
그러나 flatpak은 앞서 언급한 것과 같이 container화 되어 동작하는 앱이기 때문에 host의 file system에 대한 접근 권한을 별도로 부여해주기 전까지는 접근할 수 없다.
특정 앱이 file system에 접근할 수 있도록 하는 명령어는 다음과 같다. 다음의 사례는 obsidian이 sdc2라는 usb에의 접근 권한을 부여하고 있다.
```bash
sudo flatpak override md.obsidian.Obsidian --filesystem=/dev/sdc2
```

# 참고자료
- [flatpak official homepage](https://www.flatpak.org/)
- [flathub](https://flathub.org/)
- [Quick: Give full filesystem access to Flatpak-installed application](https://davejansen.com/give-full-filesystem-access-to-flatpak-installed-applications/)