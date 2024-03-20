# Portfolio - [졸업 작품] Scheduler_prj

<details open="open">
  <summary>Contents</summary>
  <ol>
    <li>
      <a href="#개요">개요</a>
    </li>
    <li>
      <a href="#내용">내용</a>
      <ul>
        <li><a href="#func">기능적 모델링</a></li>
        <li><a href="#object">정적 모델링</a></li>
        <li><a href="#archi">아키텍쳐 설계</a></li>
        <li><a href="#data">데이터 설계</a></li>
        <li><a href="#flow">프로그램 순서도</a></li>
      </ul>
    </li>
    <li><a href="#구현-화면">구현 화면</a>
      <ul>
        <li><a href="#signup">회원가입 및 로그인</a></li>
        <li><a href="#admin">관리자 로그인 및 사용자 관리</a></li>
        <li><a href="#findpw">비밀번호 찾기</a></li>
        <li><a href="#scheduler">일정 관리</a></li>
      </ul>
    </li>
  </ol>
</details>

---

# 개요
⭐ 프로젝트 명 : Scheduler_prj<br><br>
🚩 프로젝트 기간 : 2022년 10월 18일 ~ 11월 18일 (총 1달)<br><br>
💡 개발 목적 : 대학교 졸업 통과 기준 중 졸업 작품을 위한 프로젝트, 파이썬을 이용한 데스크탑 일정관리 어플리케이션 개발<br><br>
⌨️ 사용된 기술 스택<br><br>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

---

# 내용
**기능**
* 사용자 : 회원가입, 로그인, 비밀번호 찾기, 일정 등록, 일정 수정, 일정 삭제, 일정 확인<br>

* 관리자 : 로그인, 관리자 등록, 사용자 정보 수정, 사용자 삭제<br>

<br>

<h3 id="func">기능적 모델링</h3>

**Usecase Diagram**

![유스케이스 다이어그램 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/67efc02a-e7f2-4a13-9aa4-870b01624e10)

**User Activity Diagram**

![사용자 액티비티 다이어그램 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/f035901d-0d97-4bba-b19c-fc7fe8150840)

**Admin Activity Diagram**

![관리자 액티비티 다이어그램 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/48c9ef36-e616-4d05-9ddc-dccb1242471d)

<h3 id="object">정적 모델링</h3>

**Class Diagram**

![클래스 다이어그램 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/48db0396-8f93-4abe-a56c-afaf941cffcd)

<h3 id="archi">아키텍쳐 설계</h3>

**Package Diagram**

![패키지 다이어그램 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/8a40d3b7-7088-49fb-a9a6-aacfe7fe5d1c)

<h3 id="data">데이터 설계</h3>

**ERD Diagram**

![ERD drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/876764dc-e7c8-4c87-9233-8a5e1a290056)

<h3 id="flow">프로그램 순서도</h3>

**Function Flow Chart**

![프로그램 순서도 drawio](https://github.com/hyunn00/Scheduler_prj/assets/90684987/202330fa-89d6-4a8f-9b02-134381f31103)

---

# 구현 화면


<h3 id="signup">회원가입 및 로그인</h3>

https://github.com/hyunn00/Scheduler_prj/assets/90684987/f9a349b5-6814-477a-8b17-fc74f31e36b8

**구현 기능**

    * 기존에 등록되어 있지 않은 아이디로 로그인 시 'There are no members. Please sign up first.' 메시지 출력
    * sign up 버튼을 통해 회원가입 화면으로 전환
    * 아이디, 비밀번호, 비밀번호 확인, 이름, 전화번호 기입
    * 비밀번호와 비밀번호 확인 칸에 입력된 값이 일치하지 않으면 'Password does not match.' 메시지 출력
    * 회원가입한 아이디로 회원가입 성공시 'Welcome Scheduler.' 메시지 출력 및 일정 관리 화면으로 전환

<h3 id="admin">관리자 로그인 및 사용자 관리</h3>

https://github.com/hyunn00/Scheduler_prj/assets/90684987/56931129-df5c-4543-80dd-11c1cfb642f9

**구현 기능**

    * 등록된 관리자 이이디로 로그인 시 'Admin Account. Welcome Scheduler.' 메시지 출력
    * 사용자 목록 표와 관리자 목록 표로 사용자를 분리하여 관리
    * 사용자 목록 중 수정하고자 하는 요소를 선택하여 수정 및 삭제 가능
    * 관리자를 신규 등록 및 등록된 관리자 정보 수정 가능

<h3 id="findpw">비밀번호 찾기</h3>

https://github.com/hyunn00/Scheduler_prj/assets/90684987/82b6d7e4-4e81-4dc1-ad1d-dba2ec9817ce

**구현 기능**

    * find pw 버튼을 통해 비밀번호 찾기 화면으로 전환
    * 아이디, 이름, 전화번호를 입력하여 정보가 일치하면 비밀번호 출력
    * 빈칸이 있거나 db 정보와 일치하지 않는 값을 입력하면 사용자를 찾는데 실패했다는 메시지 출력
    * 비밀번호 찾기로 찾은 비밀번호로 로그인 시 일정 관리 화면으로 전환

<h3 id="scheduler">일정 관리</h3>

https://github.com/hyunn00/Scheduler_prj/assets/90684987/1300a2d0-c6b4-485e-8946-b75666f02339

**구현 기능**

    * 사용자 아이디로 로그인 시 일정 관리 화면으로 전환
    * 확인하고자 하는 날짜를 달력에서 선택
    * 선택된 날짜에 등록된 일정이 있으면 수정, 삭제 가능
    * 등록된 일정이 없다면 신규 일정을 등록 가능
    
---

<p align = "center">
지금까지 읽어주셔서 감사합니다!🙇‍♀️
</p>
