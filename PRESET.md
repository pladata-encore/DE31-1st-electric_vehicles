# 환경구축
## [Git Installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
개발 환경은 WSL Ubuntu 22.04.4 LTS입니다.

윈도우 11에서 작업하셔도 가능합니다.

이 파일에서 설명하는 명령어들은 Git이 설치되었다는 가정하에 설명되었습니다.

혹여나 git이 설치가 제대로 되지 않았거나 다시 설치하고 싶으신 분은 위의 링크를 타고 따라 설치하시면 됩니다.

## Repository Load
저희는 Github이라는 Git 호스팅 사이트를 통해서 소스를 저장합니다.

저희가 사용하는 레포는 [여기](https://github.com/S0rrow/EVDA)입니다.

이전에 공지드렸듯이, 팀원분들 다 Collaborator로 초대를 드렸고, 혹시나 확인 안하신 분은 Github을 가입할 때 사용하신 이메일이나 사이트에서 확인해서 Collaborator로 참여해주시기 바랍니다.

우선적으로 저희가 사용하는 레포지토리를 각자의 로컬 환경에 복제하는 것을 시작합니다.

먼저 터미널(cmd,  git bash,  powershell 등)을 켜서 본인이 폴더를 복제하고자 하는 장소로 이동해줍니다.

```bash
git clone https://github.com/S0rrow/EVDA
```
위의 명령어를 실행하면 개인이 작업하고자 하는 환경에 EVDA라는 폴더가 생깁니다.

앞으로 코드 작성을 할때는 해당 폴더 안에서 작성하게 됩니다.

```bash
cd ./EVDA
```
우선 EVDA 폴더 안으로 이동해줍니다.

현재 EVDA 폴더 내부에는 코드 테스트용으로 만들어둔 "analysis.ipynb"라는 이름의 주피터 노트북이 있습니다.

해당하는 노트북을 사용하기 위해서 먼저 가상환경을 구성해줘야 합니다.

다음의 순서는 Git의 기본설정이 완료되었고, 파이썬 3.10이 설치되었다는 가정하에 진행됩니다.

만약 Git이 설치되지 않았다면, 다음의 명령어를 실행해 git을 설정해준 다음 진행해주시면 됩니다.

```bash
git config --global user.email "깃허브@이메일"
```
위의 명령어를 통해 이메일을 설정합니다.

```bash
git config --global user.name "깃허브아이디"
```
위의 명령어를 통해 유저명을 설정합니다.

만약 파이썬이 설치되어 있지 않다면,  이 [링크](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe)를 통해 파이썬 3.10을 설치해주시면 됩니다.

### Virtual Environment
가상환경을 구성하기 위해 파이썬 3.10이 설치되었다면 다음의 명령어를 실행합니다.

```bash
python -m venv .venv
```
위의 명령어를 통해 ".venv"라는 이름의 가상환경을 구축했습니다.

가상환경을 구축했다면, 그 가상환경을 실행해줍니다.

#### Windows
```bash
.\.venv\Scripts\activate
```

#### Linux
```bash
. ./.venv/bin/activate
```
윈도우11과 리눅스의 경로가 다르기 때문에 맞는 환경에서 실행해주면 됩니다.

가상환경을 실행했다면, pip를 통해 필요한 패키지들을 설치해 줍니다.

```bash
python -m pip install --upgrade pip
```
위의 명령어를 통해 pip 자체를 우선 업데이트합니다.

```bash
python -m pip install -r requirements.txt
```
그 후,  위의 명령어를 통해 requirements.txt 내부에 작성되어있는 pip 패키지들을 재귀적으로 설치해줍니다.

앞선 명령어들을 모두 순서에 맞게 실행했다면 주피터 노트북을 사용하기 위한 준비가 끝났습니다.

### Coding
가장 우선적으로, 개개인이 작성하는 소스코드는 개개인의 branch를 통해 작성되어야 합니다.

branch 개념에 대한 설명은 다음의 [링크](https://nulab.com/ko/learn/software-development/git-tutorial/git-collaboration/branches/what-is-a-git-branch/#:~:text=Git%20%EB%B8%8C%EB%9E%9C%EC%B9%98%EB%8A%94%20%EB%B3%B8%EC%A7%88%EC%A0%81%EC%9C%BC%EB%A1%9C,%EB%A1%9C%20%EB%B3%91%ED%95%A9%ED%95%A0%20%EC%88%98%20%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.)를 참조해 주세요.

```bash
git checkout -b BRANCHNAME
```
위의 명령어는 BRANCHNAME이라는 이름의 branch를 새롭게 생성합니다.

개인의 github ID를 BRANCHNAME에 대입해서 위의 명령어를 실행해주시면 됩니다.


### 폴더 내부의 변동 사항 확인
```bash
git status
```
위의 명령어를 실행하면 현재 폴더 안의 내용물 중에 수정된 내용물이 있는지, 커밋된 내역이 존재하는지 등의 여부를 확인할 수 있습니다.

### 원격 레포지토리의 변동 사항 확인
```bash
git pull
```
위의 명령어를 실행하면 Github에 올라가있는 원격 레포지토리의 커밋들 중 현재 커밋보다 앞서있는, 즉 혹여나 수정된 내용을 누군가가 서버에 올렸다면 이를 받아오게 됩니다.

모든 코드 작성을 하기 전에 수정 내역이 있는지 확인하고 싶으시다면 pull을 실행해주면 됩니다.

### 수정된 사항을 커밋
git은 수정된 내역이 있으면 바로 저장하는 것이 아니라 여러 단계를 거쳐 최종적으로 원격 레포지토리에 저장하게 됩니다.
1. add: 수정된 파일이 있으면 이를 git이 감지합니다.
2. commit: 수정 내역에 대해서 코멘트를 남기고 이 코멘트와 함께 커밋합니다.
3. push: 해당 커밋을 원격 레포지토리에 업로드합니다.

즉 각각의 커밋은 여러 파일 수정 내역들을 묶은 기록입니다.

```bash
git add --all
```
위의 명령어는 EVDA 내부에서 실행되면 모든 수정된 파일을 하나로 묶어 줍니다.

--add 키워드 없이 파일만 따로 add해줄 수도 있습니다.

이 경우 다음의 명령어를 실행합니다.

```bash
git add FILENAME
```
위의 명령어를 통해 단일 파일만 묶을 수 있습니다.


```bash
git commit -m "This is a commit message"
```
위의 명령어는 add 명령어를 통해 묶은 수정된 파일들에 대해서 -m 키워드로 코멘트를 남기고 하나의 새로운 커밋으로 묶어줍니다.

```bash
git push
```
위의 명령어는 묶인 커밋을 Github의 원격 레포지토리에 업로드해 줍니다.

다만, 새로운 branch에서 코드를 작성해 업로드하게 되는 경우,  지속적인 업로드를 위해 원격 레포지토리에도 branch를 만들어주어야 할 필요성이 있습니다.

때문에 그냥 push를 실행하게 되는 경우 문제가 발생할 가능성이 있습니다.

이 경우 다음의 명령어를 통해 push하면 됩니다

```bash
git push -u origin BRANCHNAME
```

위의 명령어를 통해 BRANCHNAME이라는 이름의 branch를 로컬에서 현재 업로드하려는 branch와 연동해 push하게 됩니다.

이 경우 원격 레포지토리에 BRANCHNAME이라는 이름의 branch가 존재하지 않는 경우 새로 추가됩니다.