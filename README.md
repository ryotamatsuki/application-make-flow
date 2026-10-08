# Public Transit Open Data Challenge 2026 — Application-Make-Flow

**Version:** 1.0.0 · **Scope:** 公共交通オープンデータチャレンジ2026に応募する**新規アプリをゼロから**企画・検証・開発・公開するための運用ワークフロー · **Established:** 2026-10-08

> **基本原則：**「作れそうなアイデア」をそのまま開発しない。解決すべき移動課題を発見し、既存サービス・実データ・実利用者によって反証した後、残った1案の最小限の価値を独立検証する。そこから初めて完成品へ拡張する。

## これは何か／何ではないか

このリポジトリは、**コンテスト固有の開発方法・Stage判定・チェックリスト・記録テンプレート**を管理する「ワークフロー本体」です。特定のアプリ作品のコード、応募フォーム、GTFS生データ、APIキー、ユーザー情報を置く場所ではありません。制作作品はStage 08で個別リポジトリを起こし、このワークフローのバージョンと判定証跡を参照します。別作品に再利用できるものの、コンテスト外への転用は本リポジトリの目的ではありません。

既存の研究用ワークフロー [research-paper-workflow v2.8](https://github.com/ryotamatsuki/research-paper-workflow) の**有限探索・Novelty Kill・独立した反証・反例保存・最小モデル・成果凍結・差分管理**を応用しています。ただし理論証明・学術誌投稿の手順はソフトウェア開発用の監査へ置換しました。

## 公式要件（2026-10-08確認）

- **応募締切：2027-01-11 23:59 JST**。一次ヒアリング：2027-01-23〜24（対象作品に選ばれた場合）。
- **必須：** 公共交通オープンデータセンター又はGTFSデータリポジトリ等、公式応募要件に合致する公共交通オープンデータを作品内で実質的に利用すること。単にダウンロード・出典表示しただけではデータ活用の価値は示せない。
- **公開条件：** チャレンジ期間中、一般の人が無償で利用できること。作品応募は開発者サイトから実施。
- **強く推奨（必須ではない）：** ほこナビ、Project LINKS、Project PLATEAU等の追加オープンデータ。
- **公式審査の4観点：** 社会課題解決、オープンデータ活用のインパクト、技術的完成度、UI/UX。
- API利用規約、データ再配布制限、著作権・権利処理、問い合わせ先表示、締切後の重要変更制限を遵守する。

一次情報： [開催概要](https://challenge2026.odpt.org/ja/outline.html) · [エントリー／応募規約](https://challenge2026.odpt.org/ja/entry.html) · [FAQ](https://challenge2026.odpt.org/ja/faq.html) · [開発者サイト](https://developer.odpt.org/) 。詳細な判定は [COMPETITION_RULES.md](COMPETITION_RULES.md) にまとめ、応募時には公式サイトを再確認する。

## 最初に読む文書

1. [GOVERNANCE.md](GOVERNANCE.md) — 判断基準、証拠、戻し先、凍結、検証の独立性
2. [WORKFLOW.md](WORKFLOW.md) — Stage 00〜12の具体的作業、成果物、Kill Test、Exit Gate
3. [COMPETITION_RULES.md](COMPETITION_RULES.md) — 出典つき公式条件と再確認事項
4. [AGENTS.md](AGENTS.md) — AI／開発エージェントに委譲するときの強制ルール
5. [docs/START_NEW_PROJECT.md](docs/START_NEW_PROJECT.md) — まだ作品を持たない状態からの開始手順
6. [templates/](templates/) — 記録を複製して使う（未確定をPASSと書かない）

## ステージ・マップ

| Stage | 名前 | 先へ進むための核心 |
|:---:|---|---|
| 00 | Contest Intake | 公式要件を特定し、遵守可能な開発範囲を確定 |
| 01 | Problem Discovery | 実在のユーザーと検証可能な移動課題を発見 |
| 02 | Data Feasibility | 実際に取得したGTFS等で解決に必要な入力が揃うか実測 |
| 03 | Prior Art / Novelty Kill | 既存アプリ・既存手法との実質差を立証 |
| 04 | Candidate Selection | 複数案を構造比較し、有限の費用で試作する1案を選定 |
| 05 | Minimum Evidence Prototype | 単一の生活行為・意思決定が現実データ上で成立する最小実証 |
| 06 | Independent Red Team | 既存の計算コードに依存しない検証で誤判定・危険な境界を検出 |
| 07 | Value / Portability / Novelty Re-Kill | 実利用者価値・条件変更・実装後の既存サービスとの差を検証 |
| 08 | Product Spec / Core Freeze | 機能の核心仕様、失敗時の振舞い、成功指標、非目標を固定 |
| 09 | Vertical Slice / Build | 新規作品リポジトリでUIから実データ処理まで一貫して実装 |
| 10 | UX / Field Evaluation | タスク達成、理解可能性、モバイル操作、アクセシビリティを実査 |
| 11 | Release Red Team | 実サイトで独立E2E・ライセンス・安全・作品主張の整合性を監査 |
| 12 | Submission Freeze | 公開版・応募文・証拠・提出記録を確定し再現可能に保存 |

各Stageは `GO` / `CONDITIONAL GO` / `NO-GO` で閉じ、根拠・次の作業・戻し先を記録します。重要な入力データ・ユーザー主張が変われば前工程の合格も無効になり得ます。

## 最初の実行手順

1. [templates/STAGE_REPORT.md](templates/STAGE_REPORT.md) を作品プロジェクトに複製し、Stage 00を開始。
2. [templates/CANDIDATE_REGISTER.md](templates/CANDIDATE_REGISTER.md) で期限付きの複数案探索を開始。既存プロジェクトを勝者として扱わない。
3. [templates/DATA_FEASIBILITY.md](templates/DATA_FEASIBILITY.md) と [templates/PRIOR_ART_AUDIT.md](templates/PRIOR_ART_AUDIT.md) で候補のデータと重複を精査。
4. Stage 05がPASSするまでは大規模UI・全国対応・3D演出を目的化しない。
5. 作品の開発、CI、公開、応募は独立した**作品リポジトリ**で実施する。ワークフロー変更と作品コード変更を混ぜない。

**反例や棄却案も成果物。** 「未取得」「不明」「未検証」「テスト失敗」を、存在しない・ゼロ・正常・PASSに変換しない。

## 現在の状態

- このリポジトリには**開発方法のみ**を定義した。アプリの構想選定・データ取得・応募・本番公開は実行していない。
- Stage 01以降の候補や検証記録は未作成。特定作品（通院、部活、防災等）を事前に優先・確定しない。
- 初版日付：2026-10-08。今後のコンテスト公式ルール変更は、根拠URLと確認日を記録して差分修正する。
