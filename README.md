# Alone Camping

![캡처](https://user-images.githubusercontent.com/56110972/131883289-956b7308-7389-485b-918a-ca8267f5124b.PNG)

- 캠핑장 검색 및 리뷰 사이트
<br>
  
## 구축 배경

- 코로나로 바뀐 여행 문화, 이번 여름에는 나홀로 캠핑을 떠나보자!
- 회원가입 후 내가 원하는 지역의 캠핑 장소, 리뷰를 검색하고 방문 후기를 남길 수 있다.
<br>
  
## 기능

![Untitled](https://user-images.githubusercontent.com/56110972/131882160-4bdefddd-91d9-4409-afea-380ba742903d.png)

1. 회원가입 및 로그인
    - 회원가입
    - jwt 로그인
    - 네이버 로그인

2. 지역별 캠핑 장소 검색
    - 네이버 검색 API 이용, 지역별 캠핑장 정보 수집
    - 다음 검색 API 이용, 캠핑장 정보 추가 수집
    - 네이버 지도 API 이용
    - github action cron schedule time 설정, 일정 시간마다 data scraping

3. 캠핑장 리뷰 페이지
    - 리뷰 페이지 CRUD
    - 사진 업로드
<br>
      
## 데이터베이스 구조 

* 회원
    * 회원번호 (user_no)
    * 아이디 (user_id)
    * 비밀번호 (user_pw)
    * 닉네임 (user_nickname)
    
* 리뷰 게시판
    * 게시글 번호 (review_no)
    * 게시글 제목 (review_title)
    * 등록일자 (review_date)
    * 조회수 (review_hits)
    * 추천수 (review_gets)
    * 회원번호 (review_user_no)
    * 게시글 내용 (review_write)
    
* 코멘트
    * 코멘트 번호 (comment_no)
    * 게시글 번호 (comment_review_no) 
    * 회원번호 (comment_user_no)
    * 등록일자 (comment_date)
    * 코맨트 내용  (comment_write)
  
* 캠핑장
    * 캠핑장 이름 (campsite_name)
    * 캠핑장 분류 (category)
    * 캠핑장 전화번호 (phone)
    * 캠핑장 주소 (address)
    * 캠핑장 도로명 주소 (road_address) 
    * 링크 (link)
    * 이미지 주소 (image)
    * 태그 (tag)
    * 상세설명 (description)
    * 지도 좌표 (x, y)  