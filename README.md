# Public Transit Open Data Challenge 2026 — Application-Make-Flow

**Version:** 2.0.0 · **Scope:** 公共交通オープンデータチャレンジ2026に応募する**新規アプリをゼロから**企画・検証・開発・公開するための運用ワークフロー · **Established:** 2026-10-08

> **基本原則：**「作れそうなアイデア」をそのまま開発しない。解決すべき移動課題を発見し、既存サービス・実データ・実利用者によって反証した後、残った1案の最小限の価値を既存手段と比較し、作品種別に応じて独立検証する。そこから初めて完成品へ拡張する。

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

## v2.0.0で改訂したこと

- 成立判断、分析支援、可視化の検証種別を導入。可視化という形式だけでは棄却しない。
- 候補選定前の初期試用と、最大の未確認事項を確かめる小さな実験を追加。
- 既存手段との同等タスク比較と、ODが生んだ価値の比較を必須化。
- Stage 09/10で利用者タスク単位の実装と試用を反復し、運用の更新失敗も検証。
- 応募前READYと提出後の受付確認を分離。作品側の証拠、入力版、判定revision、有効期限を検査するスクリプトを追加。

ステージの意味と判定ルートが変わるため、[既存の版規則](GOVERNANCE.md)に従いメジャー改訂。v1の作品は不足項目だけを再評価する。

## ステージ・マップ

| Stage | 名前 | 先へ進むための核心 |
|:---:|---|---|
| 00 | Contest Intake | 公式要件を特定し、遵守可能な開発範囲を確定 |
| 01 | Problem Discovery | 実在の利用者の課題と検証種別を定義し、初期試用を準備 |
| 02 | Data Feasibility | 実際に取得したGTFS等で解決に必要な入力が揃うか実測 |
| 03 | Prior Art / Novelty Kill | 既存アプリ・既存手法との実質差を立証 |
| 04 | Candidate Selection | 初期試用と最大の未確認事項を調べ、限定試作する1案を選定 |
| 05 | Minimum Evidence Prototype | 作品種別に応じて核心タスクと欠損時の挙動を実データで実証 |
| 06 | Independent Red Team | 判定、集計、表示の核心出力と境界を独立参照で検証 |
| 07 | Value / Portability / Novelty Re-Kill | 既存手段との比較、OD寄与、条件変更、実装後の差を検証 |
| 08 | Product Spec / Core Freeze | 機能の核心仕様、失敗時の振舞い、成功指標、非目標を固定 |
| 09 | Vertical Slice / Build | タスク単位で実装と試用を反復し、データ更新と復旧を試験 |
| 10 | UX / Field Evaluation | 修正後のタスク、比較価値、モバイル操作、アクセシビリティを実査 |
| 11 | Release Red Team | 実サイトで独立E2E・ライセンス・安全・作品主張の整合性を監査 |
| 12 | Submission Freeze | 公開版・応募文・証拠・提出記録を確定し再現可能に保存 |

各Stageは `GO` / `CONDITIONAL GO` / `NO-GO` で閉じ、根拠・次の作業・戻し先を記録します。重要な入力データ・ユーザー主張が変われば前工程の合格も無効になり得ます。

## 最初の実行手順

1. [templates/STAGE_REPORT.md](templates/STAGE_REPORT.md) を作品プロジェクトに複製し、Stage 00を開始。
2. [templates/CANDIDATE_REGISTER.md](templates/CANDIDATE_REGISTER.md) で期限付きの複数案探索を開始。既存プロジェクトを勝者として扱わない。
3. [templates/DATA_FEASIBILITY.md](templates/DATA_FEASIBILITY.md) と [templates/PRIOR_ART_AUDIT.md](templates/PRIOR_ART_AUDIT.md) で候補のデータと重複を精査。
4. Stage 04までに[初期試用と検証計画](templates/VALIDATION_PLAN.md)、Stage 07までに[既存手段とOD寄与の比較](templates/USER_COMPARISON.md)を実施。
5. Stage 05がPASSするまでは大規模UI・全国対応・3D演出を目的化しない。
6. 作品の開発、CI、公開、応募は独立した**作品リポジトリ**で実施する。ワークフロー変更と作品コード変更を混ぜない。

[タスク反復記録](templates/ITERATION_LOG.md)、[運用計画](templates/OPERATIONS_PLAN.md)、[作品側の証拠検査](docs/PROJECT_EVIDENCE_CHECK.md)も作品に取り込む。

**反例や棄却案も成果物。** 「未取得」「不明」「未検証」「テスト失敗」を、存在しない・ゼロ・正常・PASSに変換しない。

## 現在の状態

- このリポジトリには**開発方法のみ**を定義した。アプリの構想選定・データ取得・応募・本番公開は実行していない。
- Stage 01以降の候補や検証記録は未作成。特定作品（通院、部活、防災等）を事前に優先・確定しない。
- 初版日付：2026-10-08。今後のコンテスト公式ルール変更は、根拠URLと確認日を記録して差分修正する。
