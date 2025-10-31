---
date: '2025-10-31T13:01:55+09:00'
draft: false
toc: true
comments: true
authors:
  - 손준호
  # - 이정욱
tags:
  - autonomous ship
title: 'AIS 데이터 수집하기'
---

## AIS 데이터를 수집한다고?
[대표적인 선박 데이터 - AIS 데이터 개요](../what-is-ais)에서 VHF 전파를 수신하여 AIS 메시지를 수집할 수 있다고 했는데, 그럼 직접 안테나를 설치하고 수집한다는 말인가?

아니다.
우리는 개인이기 때문에 그 비용을 감당할 수도 없고, 비용을 감당할 수 있다 하더라도 우리나라 전체 연안에서 수집하는 것은 거의 불가능에 가까울 것이다.

감사하게도 몇몇 나라들은 국가차원에서 이들을 수집하고 웹상에 무료로 배포한다.
(**안타깝게도 우리나라는 여기에 포함되지 않는다.**)
그래서 우린 이걸 다운받아서 데이터를 수집할 것이다.

## AIS 데이터를 무료로 배포하는 국가들
대표적으로 *미국*과 *덴마크*가 AIS 데이터를 무료로 제공하고 있다.
덴마크 AIS 데이터는 북해를 통항하는 선박들의 데이터를 포함하고 있으며, 미국 AIS 데이터는 태평양과 대서양, 미국 연안을 통항하는 선박들의 데이터를 포함하고 있다.

개인 연구자로써 이런 대량의 데이터를 무료로 공개하는 이들 국가들에게 감사함을 전한다.

- 덴마크: [Danish Maritime Authority](http://aisdata.ais.dk/)
- 미국: [National Oceanic and Atmospheric Administration (NOAA)](https://hub.marinecadastre.gov/pages/vesseltraffic)

{{<my-img image="https://private-user-images.githubusercontent.com/53478216/508024990-a7de3423-ab95-4412-9a94-ca431c12ed48.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjE4ODkyMDYsIm5iZiI6MTc2MTg4ODkwNiwicGF0aCI6Ii81MzQ3ODIxNi81MDgwMjQ5OTAtYTdkZTM0MjMtYWI5NS00NDEyLTlhOTQtY2E0MzFjMTJlZDQ4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDMxVDA1MzUwNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQ4M2JhM2FiMzdjYzFlYzk0MGY3NzgyZDU2OGIyZjc2OTA2MmFmNDQ4ZTQxZjRlMjk3MmRjYTcxNjc3NTk2NmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5OqIIKSuy4pxnlPLWkeqB-ZTUki_SMHZ4jRLpVLd0RU" caption="덴마크 AIS 데이터 다운로드 페이지" width="90%">}}
{{<my-img image="https://private-user-images.githubusercontent.com/53478216/508025339-f28c16aa-08c3-4404-b33d-b97227850388.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjE4ODkyMDYsIm5iZiI6MTc2MTg4ODkwNiwicGF0aCI6Ii81MzQ3ODIxNi81MDgwMjUzMzktZjI4YzE2YWEtMDhjMy00NDA0LWIzM2QtYjk3MjI3ODUwMzg4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMzElMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDMxVDA1MzUwNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY1YzY3ZWMyZDM2ZDZlNzRhMTI1OGMyMTQxYTQyMzQ5NDFjZjcxNzhiMjMyMTMyYjQwNTY1NTgwYmMyYWQwN2MmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.WiQ-IFEwqvF83hSpHnBoQ8-POashnJgjNkw6Ki7fxwk" caption="미국 AIS 데이터 다운로드 페이지" width="90%">}}

## 데이터가 배포되는 형태
두 국가의 데이터 모두 일 단위로 AIS 메시지를 집계하여 하나의 csv를 만들고, 이걸 압축하여 일단위로 배포한다.
하루 데이터만 1기가 이상이기 때문에 압축하여 배포되고 있으며, 하루치 압축된 파일만해도 약 700 MB가 넘는다.
그러니까 필요한 만큼만 다운받도록 하자.

혹시나 연단위로 수집해야 한다면, 다운로드 페이지의 링크들을 순회하며 다운받는 **wget 스크립트**를 작성하여 사용하면 될 것이다.

{{< authors-inline >}}
