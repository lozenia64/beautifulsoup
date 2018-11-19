# BeautifulSoup

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
이름, 그룹, 시즌, 사용시간, 메인노트, 지속시간, 범위, 점수, 투표 수 등에 대한 데이터 수집

* fragrantica에서는 일정 횟수 이상 접근하는 경우 차단하므로 딜레이를 크게 주었다. perfume.txt 파일을 여러 input.txt 파일들로 나누어 작업.
* 또한 딜레이 때문에 작업시간이 매우 길어지므로 여러 PC에 나누어 작업했다.

```bash
python3 fragrantica.py
```

* fragrantica.txt 파일 생성.

---
## 3.Numeric 데이터들을 Nominal 데이터로 변환

마이닝 과정을 쉽게 하기 위하여 Numeric 데이터들을 Nominal 데이터들로 변환해 주었다.

* 앞 단계에서 딜레이 때문에 3개의 PC에 나누어 작업하였으므로 파일 3개를 병합하는 동시에 분류 작업을 동시에 해주었다.

```bash
python3 merge.py
```
