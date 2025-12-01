# 나맞지 (Namatji)

> 중소기업·소상공인을 위한 맞춤형 국가 지원사업 추천 플랫폼

[![Website](https://img.shields.io/badge/Website-namatji.com-blue)](https://namatji.com)

## 📋 목차
- [개요](#개요)
- [기획 배경](#기획-배경)
- [주요 기능](#주요-기능)
- [기술 스택](#기술-스택)
- [주요 기술적 특징](#주요-기술적-특징)

## 🎯 개요

**나맞지**는 중소기업과 소상공인을 위한 국가 지원사업 정보 제공 및 맞춤 추천 서비스입니다. 복잡하고 산재되어 있는 정부 지원사업 정보를 한 곳에서 확인하고, 사용자의 기업 정보를 바탕으로 최적의 지원사업을 추천받을 수 있습니다.

## 💡 기획 배경

### 문제 인식
- 매년 수천 개의 국가 지원사업이 공고되지만, 정보가 여러 기관에 분산되어 있어 접근성이 낮음
- 중소기업·소상공인은 본업에 집중하느라 적합한 지원사업을 찾고 신청하는 데 어려움을 겪음
- 복잡한 공고문과 지원 요건으로 인해 정보 파악에 많은 시간 소요

### 솔루션
- **통합 정보 제공**: 기업마당 API를 활용한 지원사업 공고 통합 관리
- **맞춤형 추천**: 사용자의 지역, 업종, 업력 등을 분석하여 적합한 지원사업 자동 추천
- **AI 기반 요약**: OpenAI API를 활용한 공고문 자동 요약으로 핵심 정보 빠른 파악
- **간편한 접근성**: 카카오 소셜 로그인으로 간단한 회원가입 및 로그인

## ✨ 주요 기능

### 1. 지원사업 공고 조회
- 실시간 업데이트되는 국가 지원사업 공고 확인
- 상세한 지원 요건 및 신청 방법 안내
- AI 기반 공고 내용 요약 제공

### 2. 맞춤형 추천 시스템
- 카카오 소셜 로그인을 통한 간편 인증
- 사용자 프로필(지역, 업종, 업력 등) 기반 추천
- 개인화된 지원사업 리스트 제공

### 3. 자동 데이터 수집 및 처리
- 매일 평일 18시 자동 공고 수집 (django-crontab)
- Naver CLOVA OCR을 활용한 공고문 파일 텍스트 추출
- OpenAI GPT를 활용한 공고 내용 분석 및 요약

### 4. SEO 최적화
- Robots.txt 및 Sitemap 설정
- 네이버 서치어드바이저 연동
- 구글 서치콘솔 연동
- 검색 엔진 노출 최적화

### 5. 광고 수익화
- Coupang Ads 통합
- 안정적인 서비스 운영을 위한 수익 모델

## 🛠 기술 스택

### Backend
- **Language**: Python
- **Framework**: Django
- **Database**: MySQL
- **Task Scheduling**: django-crontab

### Frontend
- **Language**: JavaScript

### Infrastructure
- **Deployment**: AWS EC2 (Ubuntu)
- **Web Server**: Nginx
- **WSGI Server**: Gunicorn
- **Storage**: AWS S3

### Authentication
- **Framework**: django-allauth
- **Social Login**: Kakao OAuth 2.0

### External APIs
- **OpenAI API**: GPT 모델을 활용한 공고문 분석 및 요약
- **Naver CLOVA API**: OCR 기능으로 공고문 이미지/PDF 텍스트 추출
- **Bizinfo API**: 기업마당 API를 통한 지원사업 공고 데이터 수집

## 🔑 주요 기술적 특징

### 1. 자동화된 데이터 파이프라인
```python
# django-crontab을 활용한 스케줄링
매일 평일 18:00 → Bizinfo API 호출 → 공고 데이터 수집 
→ Naver CLOVA OCR (파일 텍스트 추출) 
→ OpenAI API (내용 분석 및 요약) 
→ MySQL 저장
```

### 2. 소셜 로그인 통합
- django-allauth를 활용한 카카오 소셜 로그인
- 간편한 회원가입 및 로그인 프로세스
- 사용자 프로필 자동 연동

### 3. 클라우드 기반 인프라
- AWS EC2를 활용한 안정적인 서비스 운영
- AWS S3를 통한 정적 파일 및 미디어 파일 관리
- Nginx + Gunicorn 조합으로 효율적인 요청 처리

### 4. SEO 최적화
- 검색 엔진 친화적인 URL 구조
- 메타 태그 및 구조화된 데이터 제공
- 주요 검색 포털 서치콘솔 연동

### 5. AI 기반 콘텐츠 처리
- GPT 모델을 활용한 자연어 처리
- 복잡한 공고문을 이해하기 쉬운 요약으로 변환
- OCR 기술로 다양한 형식의 문서 처리


## 👥 Contact

- Website: [https://namatji.com](https://namatji.com)

---

**나맞지**와 함께 우리 기업에 딱 맞는 지원사업을 찾아보세요! �