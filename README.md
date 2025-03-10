# IOT-algorithm-2025
IOT 개발자 자료구조와 알고리즘(코딩테스트) 리포지토리 2025

## 1일차

### 자료구조
- 데이터를 구성하고 효율적으로 관리하는 형태

#### 자료구조의 종류
- 단순 자료구조
    - 정수, 실수, 문자, 문자열 
- 선형 자료구조
    - 배열, 리스트, 스택, 큐
- 비선형 자료구조
    - 트리, 그래프
- 파일 자료구조
    - 순차파일, 색인파일, 직접파일

### 알고리즘
- 문제를 해결하는 논리적인 방법, 순서

#### 알고리즘 성능
- `빅오 표기법`(빠른 순)
    - $O(1)$ : 데이터 수에 관계없이 항상 일정한 시간 소요
    - $O(log n)$ : 단순 for문이지만 전체 중 일부만 처리 
    - $O(n)$ : 단순 for문
    - $O(n log n)$ : 이중 for문인데 안쪽 for문이 전체 중 일부만 처리
    - $O(n^2)$ : 이중 for문
    - $O(n^3)$ : 삼중 for문
    - $O(2^n)$ : 지수 시간 복잡도를 의미

### 리스트 복습 
- 1차원, 2차원 
    - 리스트 생성, 인덱싱, 슬라이싱!!, 함수들,...
    - 2차원 행,열 개념, 생성...


## 2일차 
- 기초 문법
    - 리스트 컴프리헨션 복습 :[노트북](./day02/da01_list_again.ipynb)

- 자료구조
    - 선형리스트부터 : [노트북](./day02/da02_linear_list.ipynb) 
    - 원형 리스트까지 : [노트북](./day02/da03_linked_list.ipynb)


## 3일차
- 자료구조
    - 연결리스트
        - 연결리스트 구현 : [파이썬](./day03/da01_linked_list.py)
        - 파이썬 list() : 이중연결리스트와 유사
        - 연결 리스트 실습 : 주소록 (단순연결리스트) [파이썬](./day03/da01-1_147pg.py) --> 해야함
        - 원형 연결 리스트 - 시작노드 변경시 오버헤드 없음
        - 이중 연결 리스트 - 앞에서 검색, 뒤에서 검색 용이
        - 연결리스트 사용 예시 - 가상메모리 관리, 윈도우 이벤트 관리,...

    - 스택 : [노트북](./day03/da02_stack.ipynb)
        - 노트북 참조
        - 알고리즘 DFS(깊이우선 탐색)시 스택 사용
        - 스택 구현 : [파이썬](./day03/da03_stack.py)

    - 큐 : [노트북](./day03/da04_queue.ipynb)
        - 개념, 노트북 참조
        - 알고리즘 BFS(너비우선탐색) 시 사용


## 4일차
- 자료구조/알고리즘
    - 큐
        - 큐 구현 : [파이썬](./day04/da01_queue.py)
    - 이진 트리 : [노트북](./day04/da02_binary_tree.ipynb)
        - 컴퓨터 시스템 등, 많은 분야에서 사용
        - 이진트리 검색
        - 이진트리 구현 : [파이썬](./day04/da03_binary_tree.py)
    

## 5일차
- 자료구조 /알고리즘  
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Directed.svg/1024px-Directed.svg.png" width="300">

    - 그래프 : [노트북](./day05/da01_graph.ipynb)
        - 깊이우선탐색 : [파이썬](./day05/da02_dfs.py)
        - 최소비용 신장트리 : [파이썬](./day05/da03_min_cost_spanningTree.py)
            - 응용예제 [파이썬](./day05/da03-1_min_cost_spanningTree(355pg).py) --> 업데이트 예정

    - 재귀호출 : [노트북](./day05/da04_recursive_call.ipynb)


## 6일차
- 자료구조/알고리즘
    - 재귀호출
        - 재귀호출 연습 : [노트북](./day06/da01_recursive_practice.ipynb)
        - 프랙탈 연습 : [파이썬](./day06/da02_fractal01.py) | [파이썬](./day06/da03_fractal02.py)
            - 응용 예제 : [파이썬](./day06/da03-1_fractal(P385).py)  

https://github.com/user-attachments/assets/bed7957c-af64-4a8f-b810-2dd6a35ea2d7


- 자료구조/알고리즘        
    - 정렬 : [노트북](./day06/da04_sort.ipynb)
        - 응용 예제 1. [파이썬](./day06/da04-1_sort(p416).py)
        - 응용 예제 2. [파이썬](./day06/da04-2_sort_practice(p421).py)



## 7일차
- 자료구조/알고리즘
    - 정렬
        - 퀵 정렬 [노트북](./day06/da04_sort.ipynb)
        - 정렬 알고리즘 응용
            - 응용 예제 1. [파이썬](./day07/da02-1_practice(p453).py)
            - 응용 예제 2. [파이썬](./day07/da02-2_practice(p457).py) --> 업데이트 예정

    - 동적 계획법 [노트북](./day07/da03_dynamic_programming.ipynb)
        - 응용 예제 1. [파이썬](./day07/da04_dynamic_proPractice(p504).py) --> 업데이트 예정
        - 응용예제 2. [파이썬] -> 업데이트 예정



## 8일차
- 자료구조/알고리즘
    - 검색 : [노트북](./day08/da01_search.ipynb)
        - 검색 구현
            [파이썬](./day08/da02_searchEx.py)
    - 코딩테스트