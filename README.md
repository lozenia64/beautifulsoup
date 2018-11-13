# bs

파이썬을 사용한 웹 크롤링

---
## 1. 목록 페이지에서 링크 얻기

designers.py 파일을 사용하여 각 designer 페이지에 대한 링크를 designers.txt에 저장

```bash
python3 designers.py > designers.txt
```
같은 방법으로 perfume.py 파일을 사용하여 한 designer 페이지에 있는 모든 제품 링크를 perfume.txt에 저장

```bash
python3 perfume.py > perfume.txt
```

---
## 2. 제품 페이지에서 데이터 얻기

fragrantica.py 파일을 사용하여 각 제품 페이지에 존재하는
이름, 그룹, 시즌, 사용시간, 메인노트, 지속시간, 범위 등에 대한 데이터 수집

```bash
python3 fragrantica.py > fragrantica.txt
```
