---
date: '2025-10-30T11:19:17+09:00'
draft: false
toc: true
comments: true
authors:
  - 손준호
tags:
  - autonomous ship
title: '대표적인 선박 데이터 - AIS 데이터 개요'
---

## AIS와 AIS 데이터
{{<my-img image="https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Ais_dcu_bridge.jpg/1920px-Ais_dcu_bridge.jpg" caption="AIS on ship from [wikipedia](https://en.wikipedia.org/wiki/Automatic_identification_system)" width="60%">}}

선박의 가장 대표적인 데이터로 **Automatic identification system (AIS) 데이터**를 꼽을 수 있다.
AIS 데이터는 **AIS**로부터 송신되는 메시지들을 수집한 것이다.

AIS는 선박의 위치 및 운항 정보를 담은 메시지를 주변 선박 및 연안국을 향해 사전 정의된 주기에 따라 자동으로 송신하는 역할을 하는 장비다.
AIS의 목적은 선박과 연안국이 주변 해역의 상황을 파악하는데 도움을 주고, 선박과 선박 그리고 선박과 연안국 사이의 불필요한 음성 통신 없이도 정보 교환이 가능하도록 만들기 위함이다.

AIS 메시지 송신은 [Very high frequency (VHF)](https://en.wikipedia.org/wiki/Very_high_frequency) 주파수(161.975MHz, 162.025MHz)를 통해 이뤄진다.
그래서 이를 수신할 수 있는 장치만 있다면, 수신 범위 내의 누구라도 이를 수집할 수 있다.

AIS 메시지의 수신가능한 수평거리는 10--20 해리(nautical mile)로 짧은 편이다.
km로 환산하면 약 20--40km 정도가 된다.
그렇기 때문에 너무 먼 거리에서는 AIS 통해 선박을 확인할 수 없으며, 인근의 선박들만을 파악할 수 있다.

이처럼 전파 거리가 짧은 건 VHF의 강한 직진성 때문이다.
그래서 장애물과 굴곡이 없는 상공을 향해서는 최대 400km까지 도달할 수 있다.
이에 착안하여 최근에는 지구 저궤도 위성에 AIS 수신기를 부착하고 AIS 메시지를 수집하는 방식(Satellite-AIS 방식)도 사용된다.
이를 통해, 육상의 전파가 닿지않는 대양항해 (태평양, 대서양을 가로지르는 항해)를 하는 선박의 AIS 데이터를 수집할 수 있다.
([여기](https://www.marinetraffic.com/en/ais/home/centerx:-12.0/centery:25.0/zoom:4)를 보면 태평양과 대서양을 가로지르는 선박들을 확인할 수 있다.)

## AIS 메시지의 구성
AIS 메시지는 1)정적 데이터와 2)동적 데이터로 구성된다.
1. **정적 데이터**:  
    - 정적 데이터는 AIS 설치 시 입력되는 선박의 고유 정보이다.
    - Maritime Mobile Service Identity (MMSI), International Maritime Organization (IMO) 번호, 호출부호 (Call sign), 선명, 선종, 선박의 길이와 폭이 이에 해당한다.
    - 이들은 한번 부여된 후 거의 변화할 일이 없다.

1. **동적 데이터**:  
    - 동적 데이터는 선교에 설치된 센서들과 연동되어 수신되는 정보이다.
    - 선박의 위치와 그때의 UTC 시각, Speed Over Ground (SOG), Course Over Ground (COG), 선수 방위 (heading), 항해와 관련한 데이터가 이에 해당한다.
    - 항해와 관련한 데이터는 *선박의 항해사에 의해 수동으로 입력되는 정보*로, 선박의 흘수(draft), 선적된 위험 화물의 종류, 목적지, ETA(Estimated Time of Arrival)가 이에 해당한다.

## 실무를 통해서만 알 수 있는 것들
- 어선이나 소형 선박들은 끄고 다니기도 한다.
- 해적 출몰 해역에서는 의도적으로 끈다.
- 수기로 입력하는 데이터는 틀린 경우도 많다. 
항해사들이 실수로 바꾸지 않았거나 귀찮아서 안바꾸기도 하기 때문이다.
- 어선들은 설치한 어망을 추적하기 위한 목적으로 어망 부이 (buoy)에도 AIS를 설치한다.
그리고, 아시아 연안에는 이런 어망이 수도없이 깔려있어서 AIS 디스플레이를 엉망으로 만든다.
- 대양에서는 알려진 것보다 *훨씬 더 먼 거리에서도 수신이 되기도 한다*.
80해리가 넘는 곳에 있는 선박이 탐지되기도 한다.
아마 장애물이 없기 때문이지 싶다.

## References
- [Son, J.-H., 2022. PSO 알고리즘에 기반한 AIS 데이터로부터의 선박항로 패턴 추출](https://kmou.dcollection.net/srch/srchDetail/200000603089) 

{{< authors-inline >}}
