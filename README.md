# Hermes Agent configuration backup

이 저장소는 Hermes Agent `aria` 프로필의 복구 가능한 설정 백업입니다.

## 포함 항목

- `config/config.yaml`: 현재 Hermes 설정
- `profile/SOUL.md`: 에이전트 성격/행동 지침
- `manifests/env.example`: 필요한 환경변수 이름만 기록한 템플릿(값 없음)
- `manifests/skills.manifest`: 설치된 번들 스킬과 버전 해시
- `manifests/backup-metadata.json`: 백업 메타데이터와 파일 체크섬

## 의도적으로 제외한 항목

보안과 개인정보 보호를 위해 다음 항목은 백업하지 않습니다.

- `.env` 및 API 키, GitHub/Slack 토큰, OAuth 인증정보
- 세션 기록, 메모리 DB, 응답 DB
- 로그, 캐시, PID/소켓/락 파일
- 채널·사용자 식별자가 들어갈 수 있는 플랫폼 런타임 상태

## 복구 개요

1. Hermes Agent를 설치하고 `aria` 프로필을 생성합니다.
2. `config/config.yaml`을 해당 프로필의 `config.yaml`로 복사합니다.
3. `profile/SOUL.md`를 해당 프로필의 `SOUL.md`로 복사합니다.
4. `manifests/env.example`에 나열된 변수 중 필요한 비밀값을 새 `.env`에 직접 설정합니다.
5. Hermes를 재시작하고 설정을 점검합니다.

주의: 이 저장소에는 비밀값을 절대 커밋하지 마세요.
