# Starting a New App from Zero

このリポジトリはワークフローのひな型。**製品の企画、コード、データ、実地検証はまだ何も完成していない**ことを前提として実行する。既存の愛媛県アプリや過去プロジェクトを勝者にしない。

## Step A — Confirm rules and create a project record

1. `README.md` → `GOVERNANCE.md` → `COMPETITION_RULES.md` → `WORKFLOW.md` を読む。
2. 初期段階では候補比較用のローカル／非公開`project/`フォルダを作る。複数案がある間は製品固有のコード・巨大アーキテクチャを決めない。
3. `templates/STAGE_REPORT.md` を`project/stages/STAGE_00.md`に複製。応募主体、制約、予算、公式規約の確認日を埋める。
4. `Stage 00 GO`を記録。実際に開発者アカウント登録したか、単にURLを確認しただけか区別する。

## Step B — Identify and select one problem

5. Stage 01で利用者の判断を具体化。「誰が、いつ、何を判断、理解、体験しづらいか」。検証種別を選び、対象者の初期試用を準備する。少数の異質な候補で開始し、有限の探索予算を宣言。アイデアの数は成果でない。
6. `templates/CANDIDATE_REGISTER.md` に比較記録し、真に異なる候補だけを保持。
7. Stage 02で実GTFS/ODPTデータの取得と期間・権利・計算項目の充足を測定。Stage 03で既存アプリ・過去受賞作・代替組み合わせに負けない価値を探す。
8. Stage 01〜03で候補ごとの最大の未確認事項を小さな実験で確かめ、詳細調査を絞る。Stage 04までに画面ラフや操作例による対象者の初期試用を記録し、**証拠つきで1案のみ**を限定試作に採用。許された試作範囲と棄却条件を明記。初期試用が未実施なら募集と限定実証だけをCONDITIONAL GOで認める。

## Step C — Prove the core before polishing

9. Stage 05は**単一の端から端までの実ケース**に限定。成立判断は正／負／UNKNOWN、分析は検算／条件変更／欠損、可視化は表示照合／読み取り／欠損のケースを事前定義する。
10. Stage 06は別コード／参照ケースによる独立検証。例：プロダクションの最短路と別の簡約GTFS/時刻表参照判定が一致するか。食い違いは隠さず戻す。
11. Stage 07で同等の課題を既存手段と試作品により実施し、判断や理解の正確さ、時間、負担、誤解を比較。必須ODと追加データの寄与も比較する。未確認の価値をGOとせず、劣る案を投入済み費用のために救済しない。

## Step D — Build a competition-ready product

12. Stage 08で仕様・範囲・公開条件をfreezeし、ここで新規作品リポジトリを作成する。`docs/`に証拠台帳とステージ記録を移して追跡できるようにする。
13. Stage 09/10でタスク単位の実装、preview試用、修正を反復。データ更新失敗や期限切れを試し、運用担当と費用を確定する。Stage 11で独立QAと価値主張を監査。CIを通しただけで完了にしない。
14. Stage 12で実サイトと応募記録を固定し、**応募準備完了と応募受理を厳格に分離**。作品内容の提出後修正制約を事前確認。

## Recommended project artifact layout (once a project exists)

```text
project-repository/
  README.md
  AGENTS.md
  docs/
    CONTEST_REQUIREMENTS.md
    CANDIDATE_REGISTER.md
    DATA_FEASIBILITY.md
    PRIOR_ART_AUDIT.md
    VALIDATION_PLAN.md
    USER_COMPARISON.md
    ITERATION_LOG.md
    OPERATIONS_PLAN.md
    PROJECT_STATE.json
    PRODUCT_SPEC.md
    EVIDENCE_LEDGER.md
    DECISIONS.md
    stages/
      STAGE_00.md ... STAGE_12.md
    INDEPENDENT_VALIDATION.md
    SUBMISSION_MANIFEST.md
  src/            # project-specific; choose after selection
  scripts/check_project.py
  tests/
    fixtures/
  .github/workflows/ci.yml
```

初期の`project/`試作作業は必要なら別の private repo で行い、秘匿データ・個人情報・許諾不明なデータを公開リポジトリへ持ち込まない。

## A ready-to-run Stage 00 prompt

> 公共交通オープンデータチャレンジ2026専用の `application-make-flow` v2.0.0に従い、新規アプリのStage 00のみ実施する。`GOVERNANCE.md`、`COMPETITION_RULES.md`、`WORKFLOW.md`、`AGENTS.md`、`templates/STAGE_REPORT.md` を読む。公式開催概要・応募規約・FAQ・開発者サイトを現時点で再確認し、締切・作品条件・データ利用・公開無償・技術制約を出典付きで記録する。未確認事項をPASSにせず、`GO / CONDITIONAL GO / NO-GO`を根拠つきで判断し、Stage 01の許可範囲と候補探索の時間上限を提案する。まだアプリ案の勝者を決めたりアプリを実装したりしない。

## Evidence and iteration setup

[VALIDATION_PLAN](../templates/VALIDATION_PLAN.md)、[USER_COMPARISON](../templates/USER_COMPARISON.md)、[ITERATION_LOG](../templates/ITERATION_LOG.md)、[OPERATIONS_PLAN](../templates/OPERATIONS_PLAN.md)を必要なStageで更新する。記録を増やすために同じ結果を別文書へ複製せず、同一証拠をリンクする。

[PROJECT_STATE](../templates/PROJECT_STATE.json)と[scripts/check_project.py](../scripts/check_project.py)を作品へコピーし、[利用説明](PROJECT_EVIDENCE_CHECK.md)に従って証拠検査をCIで実行する。GOの証拠不足、入力や前段判定の変更、期限切れを検出する。チェックは観測や承認を代行しない。

## Example anti-patterns

- 「全国のGTFSが公開されているので全国で動くはず」→ 必須フィールド・日時・許諾・地域別カバレッジを実測。
- 「過去の受賞作と名前が違う」→ 同一ユーザータスク・計算・出力なら重複し得る。
- 「AIがテストに成功したと言った」→ ログ・ケース・実行環境・実サイト上の動作を確認。
- 「移動手段が表示されない」→ 対応データで検出できないという意味に限定。
- 「情報を多く重ねた」→ ユーザーの判断に寄与した証拠が無ければ機能追加の根拠にならない。
