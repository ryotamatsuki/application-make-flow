# Canonical Workflow — Greenfield App, ODPT Challenge 2026

**v1.0.0 / 2026-10-08**。対象：何も作っていない時点から、課題発見、価値検証、アプリ制作、公開、応募まで。作品候補やフレームワーク、県内特定地域に依存しない。各Stageの標準フォーマットは [STAGE_REPORT](templates/STAGE_REPORT.md)、判定・変更ルートは [GOVERNANCE](GOVERNANCE.md)。

## Stage common contract

各Stageに `Purpose / Inputs / Required work / Evidence / Kill tests / Exit gate / Artifacts / Verdict / Next authorized action` を適用。`GO` の口頭宣言では進行しない。Stage番号の進行は品質の代理指標ではない。最初の本命候補を失った場合も別案に自動承認を引き継がない。

## Stage 00 — Contest Intake / Eligibility

**Purpose**: 開始前にコンテスト制約と制作・公開上の権利を確認する。

- **Inputs**: [公式開催概要](https://challenge2026.odpt.org/ja/outline.html)、[応募規約](https://challenge2026.odpt.org/ja/entry.html)、[FAQ](https://challenge2026.odpt.org/ja/faq.html)、[開発者サイト](https://developer.odpt.org/)。
- **Required**: 公式応募要件、23:59 JST締切、応募者と著作権、データ利用制限、公開方式、運用費／時間上限、公開／問い合わせ担当、デモ参加可能性を記録。利用者の個人情報は原則持たない前提で設計。
- **Kill tests**: 応募条件に合わない、公開無償が実現不可能、公開前のデータ権利問題を解消できない。
- **Exit**: 公式情報へのURL・確認日時、ハード制約／推奨事項の区別があり、応募経路がある。
- **Artifacts**: `project/CONTEST_REQUIREMENTS.md`、`project/STAGE_00.md`。結果：GO / CONDITIONAL GO / NO-GO。

## Stage 01 — Problem Discovery / User Decision

**Purpose**: コンテストテーマに実際に合致する「行動ができない」「判断できない」課題を特定する。

- **Inputs**: 公式交通政策資料、地域課題、観察・利用者ヒアリング、現行の移動サービス、公開データの存在。
- **Required**: 誰が、どの時点で、何を判断し、今どう失敗しているかを`When / Who / Decision / Failure / Consequence`で書く。最低一つの一次資料または明示的な実ユーザー観察を得る。候補群の件数／調査期間／停止ルールを予算化し、構造重複を統合。入力が偏っているときは不足を明示する。
- **Kill tests**: 単なるデータ可視化、利用者がいない仮説、事実にない課題を捏造、公共交通ODの活用が本質でない。
- **Exit**: 少なくとも一つの実在根拠つきで、観測・反証可能な課題定義ができる。
- **Artifacts**: `CANDIDATE_REGISTER.md`（候補ID、独立性、棄却理由）と課題エビデンス台帳。未確定の仮説は仮説のまま残す。

## Stage 02 — Data Feasibility / Provenance

**Purpose**: 公共交通オープンデータによる中核の判断が本当に計算可能か、実ファイル／APIで検証する。

- **Required**: 配信元・ID・ライセンス・APIキー有無・データ版／取得時刻・対象地域／運行期間・利用権利を保存。GTFSの`agency/stops/routes/trips/stop_times`、`calendar/calendar_dates`（存在・適用条件）、サービス日・24時超、ID参照、停留所座標、徒歩／乗換条件の有無を検査。必要ならGTFS-RT/GTFS-Flex・ほこナビ/LINKS/PLATEAUを実際に取得・接続し、任意／必須・取得不能／不存在を分離。
- **Required measurement**: 機能が必要とする項目ごとに充足`PASS / PARTIAL / MISSING / UNAVAILABLE / UNKNOWN`を、サンプル例／対象範囲／再現コードとともに記録。公開時の再配布・API条件も調べる。
- **Kill tests**: 必須入力がなく算出不可能、対象地域とサービス日が合わない、必要なライセンスがない、観測できない値を推測で補ってしまう。
- **Exit**: 対象利用者の1ケースに必要な入力を、許諾を満たし再現可能な形で得られる。残欠損がある場合は扱いを明示して核心判定を過剰主張しない。
- **Artifacts**: [DATA_FEASIBILITY](templates/DATA_FEASIBILITY.md)、再現ログ、データ辞書。独立監査リポジトリの既存分析は**参照できるが、それだけで新作品の合格証書にはしない**。

## Stage 03 — Prior Art / Novelty Kill

**Purpose**: 既存サービスですでに解ける問題を単に作り直さない。

- **Required**: 国内外の乗換案内、地図、MaaS、行政サイト、自治体調達製品、学術研究、OSS、過去のODPT受賞作品を、狙う利用者タスクごとに探索。名前や画面ではなく`input → decision logic → output → action enabled`で同型性を比較。上位の脅威は実際に動作確認するかその限界を書く。
- **Required classification**: `EXACT SUBSTITUTE` / `STRONG OVERLAP` / `PARTIAL OVERLAP` / `ADJACENT` / `PLAUSIBLE GAP`。競合欠如の断定を禁止。
- **Kill tests**: 同じ利用者が現行サービスで同じ判断を同水準で行える／UI色違い程度／誤った既存サービス理解を差別化根拠にする。
- **Exit**: 最も強い代替サービスとの差分と、差分が利用者にとってなぜ重要かを検証可能に説明できる。
- **Artifacts**: [PRIOR_ART_AUDIT](templates/PRIOR_ART_AUDIT.md)。

## Stage 04 — Candidate Selection / Bounded Investment

**Purpose**: 一番見栄えのよい案ではなく、最も検証価値の高い1案を限定的に選ぶ。

- **Required**: 構造重複を除いた候補群を用い、社会課題／利用者の行為／ODデータの本質的利用／競合との差／実装可能性／独立検証可能性／時間内公開可能性を比較。重み付き点数は補助情報であり証拠ではない。高評価だが必須データ未取得の候補は選定しない。
- **Bound**: 次の実証で何を証明／否定し、どの時間・費用まで許可するか、停止ルールと棄却・保留候補の再開条件を定義。生成案数のノルマなし。
- **Kill tests**: 「既に作り始めた」「最新技術が使える」「候補に思い入れがある」だけで決める。
- **Exit**: 1案を`Candidate Freeze`し、仮説・失敗条件・最大試作範囲を固定。選ばなかった候補を破棄せず台帳に残す。
- **Artifacts**: `SELECTION_DECISION.md`、[CANDIDATE_REGISTER](templates/CANDIDATE_REGISTER.md)。

## Stage 05 — Minimum Evidence Prototype

**Purpose**: 実データ×一つの利用者判断を最小限の作りで端から端まで実現できるか検証する。

- **Required**: ごく少数の代表起点・目的地、1〜2の運行日・時刻、実GTFSと必要な付加データを使い、入力→計算→結果→利用者アクションが一周する試作。UIは低忠実度でよい。最小実証の期待値と失敗条件を実装前に定義。
- **Examples only**: 通院往復成立、部活動終了後帰宅、車いす乗換成立、運休時到達性等。**どれも自動選定せず、同じStage 01〜04審査を受ける**。
- **Prohibitions**: 全国自動対応、3D演出、巨大アーキテクチャ、過度な精度宣言、API規約違反の生データの配布。
- **Kill tests**: コアケースを実データで再現できない。フィード欠損を便なしと誤表示。外部接続がなく固定のサンプル結果を実績と偽る。
- **Exit**: 正ケース1、負ケース1、`UNKNOWN`1を再現可能に提示し、入力版・モデル仮定・使用コードSHA・実行コマンドを記録。典型例の期待値の根拠がある。
- **Artifacts**: `PROTOTYPE_REPORT.md`、最小実証コードと入力マニフェスト、代表的ユーザーストーリー。

## Stage 06 — Independent Computational Red Team

**Purpose**: 「動く」≠「正しい」。高影響の誤判定を独立の経路から探索し証明範囲を確定。

- **Required**: [INDEPENDENT_VALIDATION](templates/INDEPENDENT_VALIDATION.md) を適用。参照ロジックと製品ロジックの共通部分、非公開にした設計情報、独立計算パスを記録。手検算可能なミニGTFSや別実装の参照判定器で結果を照合。
- **Attack**: GTFS日付・祝日・24時超、minimum_transfer_time、逆順・同時刻、停留所名重複、期限切れ、欠便・運休、時刻表の揺れ、徒歩速度・距離、GTFS-RTの遅延／欠損、GTFS-Flexの予約／運行条件、データの不一致、入力範囲外、false positive/false negative。
- **Kill tests**: 独立参照と主要ケースが食い違う／影響が高い誤案内が残る／unknownを成功へ潰す。CI greenだけで認証したと言い張る。
- **Exit**: 期待値と判定境界を照合し、重要な反例を回帰テストとして保持。解決できないケースは製品仕様で`UNKNOWN`を返す、範囲から明確に除外する、またはNO-GO。
- **Artifacts**: 独立検証記録、照合差分、golden fixture、失敗事例。

## Stage 07 — User Value / Portability / Novelty Re-Kill

**Purpose**: 実装に成功したものが、本当に利用者に役立ち、条件差で壊れず、依然として差別化されているかを調べる。

- **Required**: 実ユーザーまたは職務に近い第三者に、正解や結論を先に教えず利用者タスクを試してもらう。対象人数・選定・同意・タスク・観測された成功／迷い／失敗を記録。実利用者を確保できない場合は`USER VALIDATION UNVERIFIED`と明記。
- **Required robustness**: 別の地域／事業者フィード、平日／休日、徒歩能力や乗換条件、欠損、サービス日変更などから**実装後に扱う範囲**を選び、条件変更時の判定安定性と失敗境界を示す。汎用性を保証するまで必ず複数地域対応する必要はない。単一地域なら主張を限定。
- **Novelty Re-Kill**: 実際に実装された機能・操作・判断出力をもとに、最強競合への同型性／代替可能性を再監査。単なるモック比較ではなく現時点の使用可能なサービスに照合する。
- **Kill tests**: 利用者が判断改善を実感・理解できず、比較で既存サービスに価値差が消えた、誤案内の改善不能、未検証を全国対応と表現。
- **Exit**: 最も強い利用者価値の証拠と失敗境界、差分、ターゲット利用者、機能の非目標を決定。
- **Artifacts**: `VALUE_EVIDENCE.md`、`PORTABILITY_BOUNDARY.md`、PRIOR_ART更新版。

## Stage 08 — Product Specification / Core Freeze

**Purpose**: 作るもの・作らないものと安全な判定ロジックを固め、仕様漂流を防ぐ。

- **Required**: [PRODUCT_SPEC](templates/PRODUCT_SPEC.md) に対象行動、I/O contract、意味論、Data Contract、`SUCCESS / FAILURE / UNKNOWN`、警告文と出典、最低限の画面、非目標、運用負荷、公開・無償条件、性能／アクセシビリティ基準を明記。利用者観察からMUSTを選別する。
- **Required review**: 公的推奨と見える表現、医療・防災・最終便の誤案内リスク、プライバシー、ライセンス、データ期限に応じたfail-safeをレビュー。
- **Kill tests**: 失敗の意味が決まっていない、モデル出力を保証値と呼ぶ、許諾不明の公開設計、必須データなしでMUSTを約束。
- **Exit**: 製作者が`Core Freeze`を承認。以後の変更は影響Stageと検証項目を記録。
- **Artifacts**: バージョンつき仕様、`CHANGE_LOG`、試験基準、作品リポジトリ作成指示。

## Stage 09 — Vertical Slice / Build / CI

**Purpose**: **ここから新規作品リポジトリで**本番利用可能なWeb/アプリを構築。技術選択は最小要件・運用に合わせる。

- **Required**: 入力→データ読込→核心計算→画面→ユーザーの行動→問い合わせ先、まで縦方向に完成。自動テスト、再現可能なロック済み環境、安定したデプロイ手順、secret管理、ログ／例外処理、データ更新・有効期限・停止時対応、データ出典表示を整備。
- **Required QA**: ユニット、契約、GTFS境界、Golden、統合、実ブラウザE2E、モバイルviewport、データ版照合、秘密情報スキャン、アクセシビリティ基礎。GitHub Actionsのテスト名は実行内容に正確に対応させる。PR reviewとmain保護の方法を決める。
- **Kill tests**: デモだけ機能し一般公開URLで使えない、秘密情報露出、ライセンス違反、静的モックが実データ処理を偽装。
- **Exit**: 統合された現実のユースケースが本番公開環境と一致する。`CI PASS`と`実サイトPASS`を別々に示す。
- **Artifacts**: 作品リポジトリ、テスト、CI logs、公開preview URL、出典・バージョン。

## Stage 10 — UX / Field Evaluation

**Purpose**: 初見利用者が説明無しで使えるか、判断を誤らないか実測。

- **Required**: タスク達成・所要・つまずき・誤解・重要情報への到達を複数デバイスと対象利用者で観察。計画時の成功基準を採用し、不利な結果も保存。WCAGに沿うキーボード・コントラスト・フォーカス・テキストサイズ・操作対象、画面読上げ、地図に依存しない結果テキストを検証。
- **First 30 seconds**: 誰のどんな問題を何のODで解き、入力／結果の意味が何か説明できる。30秒は内部の評価用設計原則であり公式配点ではない。
- **Kill tests**: バナーやアニメーションは美しいが主要タスクを完了できない、失敗状態が成功に見える、障害・視力・操作方法の差に配慮がない。
- **Exit**: 根拠のある改善と再テストを記録し、主要ユーザータスクが実行可能。改善のための変更がコア仕様を破った場合はStage 08へ戻す。
- **Artifacts**: `UX_TEST_REPORT.md`、撮影・キャプチャ（同意とプライバシー条件を遵守）。

## Stage 11 — Release Red Team / Competition Claim Audit

**Purpose**: 独立の初見利用者／審査員になり切り、実サイト・データ・作品主張を攻撃。

- **Required**: [SUBMISSION_QA](templates/SUBMISSION_QA.md)を使用。クリーン環境・匿名ウィンドウ・モバイルからLive URLを実際に操作。データ鮮度、鍵、ログ、依存、例外、ライセンス、出典、問い合わせ先、無料公開・再現性を点検。
- **Judge view**: 公式4観点それぞれについて、ユーザーストーリー→データ→処理→結果→画面→検証証拠へのトレースを作る。代表例を1〜3件に絞り、伝えることの重要性を優先。賞・採択・公式保証は創作しない。
- **Independent**: 既存開発チーム／同一LLMの開発ノートに依拠せず、公開サイトと説明文から主要結果を検証する。見た目のPASSと計算のPASSを分ける。
- **Kill tests**: 応募条件違反、匿名で使えない、データの不当再配布、虚偽／未証明の主張、致命的誤案内、スクリーンショットが現公開版と異なる。
- **Exit**: 全ハードゲートPASS、4観点の証拠、残余制限を記録。変更により古くなった証拠は再実行。
- **Artifacts**: `RELEASE_AUDIT.md`、`EVIDENCE_CHAIN.md`、版・環境の記録。

## Stage 12 — Submission Freeze / Hearing Readiness

**Purpose**: コンテスト要件と実際の公開・提出状態を一致させ固定。

- **Required**: 公式規約とFAQ再確認。作品URL、公開commit SHA、入出力データと利用条件、作品紹介文、出典・問い合わせ先、操作手順、デモ、動画（必要な場合）、説明上の注意、報告された制限を凍結。応募サイトの必須項目を確認し、提出操作・受領証跡を記録する。
- **Hearing readiness**: 一次ヒアリングの対象に選出された場合に備え、デモ失敗時の説明、技術・独自性・価値・ライセンスのQ&A、代替デモを準備。ヒアリング選出／受賞は確定扱いしない。
- **Kill tests**: 作品未公開、公開版と説明不一致、提出未完なのにSubmitted表示、締切後の大幅変更。
- **Exit**: `READY FOR SUBMISSION` と `SUBMITTED WITH RECEIPT` を**別々に**記録。実際の応募操作と受付証拠が無ければ後者は未完。
- **Artifacts**: `SUBMISSION_MANIFEST.md`、タグ／SHA、応募画面の受理証拠（個人情報は公開保存しない）、運用引継ぎ、応募後変更台帳。

## Whole-workflow stopping decisions

- 期限が近づいたら探索候補を追加するのではなく、条件を満たす最小公開作品へスコープを狭める。
- Stage 05/06で不可解な誤判定がある場合は公開対象範囲を縮小、または他候補へ戻す。誤案内を隠す機能変更は禁止。
- 必須規約違反を抱えたまま提出しない。
- 「コンテストに適する新しいアプリを一から作る」ことと「受賞確実」を混同しない。
