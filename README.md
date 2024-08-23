# 10$ - SPARTAMARKET

## Project Description
중고거래 플렛폼을 만드는 과제, 회원만 이용할 수 있도록 구성해야한다.

## App
### products
- 조회/등록/수정/삭제
    - 웹페이지의 기본적인 기능 CRUD
- 찜하기
    - 기능설명
- 사진
    - 기능설명
- 찜 횟수, 조회수
    - 기능설명
- 인기도순/최신순 정렬
    - 기능설명
- 해시태그
    - 기능설명
- 제목/내용/유저명/해시태그로 검색
    - 기능설명
### accounts
- 회원가입
    - 기능설명
- 로그인/로그아웃
    - 서비스를 사용하기 위해 사용자 인증
    - 서비스 접속 종료
- 회원정보수정
    - 기능설명
- 회원탈퇴
    - 기능설명
- 계정상세 페이지
    - 기능설명
- 프로필사진 등록/수정
    - 기능설명

## ERD/Framework
- 
- 

## Troubling/Troubleshooting
- 서재일: 브랜치 생성을 잊고 dev에서 작업함.
    - 다행히 로컬환경이라 remote에 영향은 가지 않았지만 이전에 작성했던 코드를 소실하여 다시 작성하게 됨.
- 서재일: 게시글의 경우 데이터베이스가 로컬에 저장되기 때문에 깃허브에는 업로드 되지 않는데 게시글을 작성할 때 삽입한 이미지가 깃허브에 업로드 되는 문제가 있었음.
    - .gitignore에 해당 위치의 폴더를 제거하고 git이 해당 파일을 추적하지 않도록 설정했음.

## Our Team
### 서재일
- 기본 데이터베이스 구현
- CRUD 구현 및 이미지 업로드
### 윤찬민
- 로그인,로그아웃 기능 구현
- 홈 하이버링크 구현
### 임선오
- 역할
### 정성원
- 회원가입 기능
- base.html css 

## Version
- asgiref==3.8.1
- asttokens==2.4.1
- colorama==0.4.6
- decorator==5.1.1
- Django==4.2
- django-extensions==3.2.3
- exceptiongroup==1.2.2
- executing==2.0.1
- ipython==8.26.0
- jedi==0.19.1
- matplotlib-inline==0.1.7
- parso==0.8.4
- pillow==10.4.0
- prompt_toolkit==3.0.47
- pure_eval==0.2.3
- Pygments==2.18.0
- six==1.16.0
- sqlparse==0.5.1
- stack-data==0.6.3
- traitlets==5.14.3
- typing_extensions==4.12.2
- tzdata==2024.1
- wcwidth==0.2.13