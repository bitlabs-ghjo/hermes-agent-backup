# Hermes Agent 전체 프로필 설정 백업

이 저장소는 Hermes 데이터 루트와 모든 멀티 프로필의 복구 가능한 설정을 자동 백업합니다.

## 백업 구조

- `profiles/default/`: 기본 Hermes 데이터 루트(`/opt/data`) 설정
- `profiles/<name>/`: `/opt/data/profiles/<name>`의 프로필별 설정
- `system/active_profile`: 현재 활성 프로필 이름
- `manifests/backup-metadata.json`: 프로필 목록과 SHA-256 체크섬
- `scripts/backup_all_profiles.py`: 프로필 자동 발견·검사·커밋·푸시 스크립트

각 프로필에서 다음 항목을 백업합니다.

- `config.yaml`
- `SOUL.md`
- 비밀값을 제거한 `env.example`
- 설치된 번들 스킬 목록과 버전 해시(`skills.manifest`)
- 번들에 포함되지 않은 사용자 정의 스킬
- 사용자 정의 `skins`, `hooks`, `desktop-plugins`, `tui-widgets`, `pets`

새 프로필이 `/opt/data/profiles/<name>`에 추가되면 다음 자동 백업 실행부터 별도 디렉터리로 포함됩니다.

## 보안상 제외되는 항목

이 저장소는 공개 저장소이므로 다음 항목은 의도적으로 제외합니다.

- `.env`, API 키, GitHub/Slack 토큰, OAuth 및 인증 파일
- 사용자 메모리와 세션/응답/실행 데이터베이스
- 로그, 캐시, PID, 소켓, 락 파일
- 채널·사용자 식별자가 포함될 수 있는 런타임 상태

백업 스크립트는 커밋 전에 모든 프로필의 실제 `.env` 값과 알려진 토큰/개인키 패턴을 검사하며, 발견 시 백업을 중단합니다.

## 수동 실행

검사와 스냅샷 생성만 수행:

```bash
./scripts/backup_all_profiles.py --no-push
```

스냅샷 생성, 커밋, GitHub 푸시 및 원격 커밋 검증:

```bash
./scripts/backup_all_profiles.py
```

## 복구 개요

1. Hermes Agent를 설치합니다.
2. `profiles/default`의 파일을 기본 Hermes 데이터 루트로 복사합니다.
3. `profiles/<name>`의 파일을 각 프로필 디렉터리로 복사합니다.
4. 각 `env.example`을 참고해 비밀값은 로컬 `.env`에 별도로 설정합니다.
5. `system/active_profile`을 참고해 활성 프로필을 선택하고 Hermes를 재시작합니다.

주의: `.env`, 인증 파일 또는 실제 토큰을 절대 커밋하지 마세요.
