# Eval: output-automator

**Date:** 2026-06-29 12:50 | **Judges:** gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash (aggregate: mean) | **Runs/model:** 3 | **Review:** automated

---

## Verdict

| Model | Overall | Accuracy | Completeness | Format Compliance | Consistency | Tone/Style | Safety | Efficiency |
|---|---|---|---|---|---|---|---|---|
| gpt-5.4-mini | **4.3 (Solid)** | 4 | 4 | 5 | 4 | 5 | 5 | 3 |
| claude-sonnet-4-6 | **3.3 (Mixed)** | 3 | 4 | 4 | 2 | 5 | 3 | 2 |
| gemini-2.5-flash | **3.4 (Mixed)** | 4 | 4 | 3 | 3 | 4 | 4 | 2 |

---

## Scorecard: gpt-5.4-mini

> All three runs deliver technically sound, production-safe solutions that correctly implement the critical requirements: gzip -t verification gating deletion, compound keep-4-floor retention implemented without the bare find-mtime antipattern, upload-before-delete sequencing, and failed-upload blocking deletion. Both required artifacts (runnable script + scheduling config) are present in proper fenced code blocks with inline assumptions. The primary gap versus the reference ideal is the absence of any explicit mtime-vs-filename-date ambiguity note. Runs 1 and 2 incur noticeable efficiency penalties from verbatim script duplication in 'quick install' blocks; Run 3 is substantially tighter. Tone is appropriate for the audience with minor lapses into offer-upsells at the end of each run.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly implement the critical safety requirements: non-empty check plus gzip -t verification, verification gating deletion (die/exit before any rm), compound retention (sort newest-first, unconditionally protect top 4, delete among the rest only if >14 days old), upload before deletion, and exit non-zero on upload failure preventing post-failure deletion. The classic bare `find -mtime +14 -delete` antipattern is avoided in all runs. One shortfall: none of the runs explicitly flag the mtime-vs-filename-date ambiguity that the reference marks as required for a 'strong' answer — all sort by mtime silently, without noting that filename-date sorting would be more deterministic for the stated naming convention. |
| Completeness | 4 | judge | All runs include the main requested artifacts: prose, runnable shell script, and scheduling config. They also mention installation and assumptions. The main gap is that the schedule is delivered as a fixed systemd timer time rather than explicitly sequencing after the existing dump cron in a robust, direct way; Run 3 even says to adjust the timer time, and Run 2 admits a fixed-time timer is only safe if chosen after the dump reliably finishes. That is close, but not fully satisfying the “after the dump completes” requirement. Also, the reference asked for at least two copy-paste-ready artifacts; this is met. |
| Format Compliance | 5 | judge | All runs deliver the required format exactly: a short prose introduction followed by at least two copy-paste-ready artifacts in fenced code blocks (bash script with shebang, set -euo pipefail, inline dependency/assumption comments; plus systemd service and timer). None is script-only or prose-only. Artifacts are self-contained and usable without further translation. |
| Consistency | 4 | judge | Core logic, safety guarantees, and structure are semantically identical across all runs: mtime-sorted list, protect-top-4, conditional delete, upload before delete, systemd artifacts. Quality is stable. Variation is in verbosity (2220 vs 3845 tokens), Run 2 adds a cron alternative not present in Runs 1/3, and the duplicated install block appears in Runs 1-2 but not Run 3. Content and safety behavior are the same; coverage and padding differ. [lexical similarity ratio: 0.156] |
| Tone/Style | 5 | judge | The tone is consistently concise, practical, senior-sysadmin/DevOps oriented, and production-safety conscious. It avoids hand-holding and filler while still being readable and operational. The guidance is appropriately direct for a competent Linux operator. |
| Safety | 5 | judge | No harmful or inappropriate content is present. The scripts are safety-conscious: they verify before deleting, use locking, scope deletion to the backup directory, and avoid destructive shell patterns. No credential leakage or unsafe command suggestions beyond the standard AWS credential placeholders. |
| Efficiency | 3 | judge | The quality is decent, but the outputs are verbose relative to the deliverable. Run 1 and Run 2 in particular include repeated installation sections, optional credential sections, copy-paste quick install blocks, and extended explanatory prose. That padding is somewhat justified by the complexity, but the token budget is noticeably heavy compared with the concise set of artifacts required. Run 3 is tighter, but the overall typical behavior still feels wordy. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (openai); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini * | claude-sonnet-4-6 | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Completeness | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Format Compliance | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Consistency | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Tone/Style ⚠ | 5 | 5 | 4 | 5 | 1 | 0.47 |
| Safety | 5 | 5 | 5 | 5 | 0 | 0.0 |
| Efficiency | 3 | 3 | 3 | 4 | 1 | 0.47 |

- **Self-preference delta:** -5 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy.
- **Panel mean spread/dim:** 1.14 (max 3).

Tokens (avg output): 3188 | Latency (avg): 19.04s | Runs: 3

---

## Scorecard: claude-sonnet-4-6

> The model's performance on this prompt is inconsistent and, for two of three runs, critically flawed in a safety-critical dimension. Run 1 provides an excellent, comprehensive, and robust solution that correctly implements all requirements, especially the complex compound retention logic and the nuanced handling of upload failures. It earns top scores across the board for accuracy, safety, completeness, format, tone, and efficiency. However, Runs 2 and 3 both introduce a severe safety flaw by pruning local backups *before* attempting the S3 upload. If the upload then fails, the script exits, but local copies have already been deleted, directly violating the prompt's requirement not to treat upload failure as a reason to have already deleted local copies. This fundamental divergence in a core safety mechanism between runs leads to a very low consistency score and significantly drags down the typical accuracy, safety, and efficiency scores for the response set.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 3 | judge | Runs are on-topic and mostly operational, but the safety-critical logic is wrong or incomplete in typical behavior. Run 1 uploads before pruning, but still prunes after upload failure: "Upload FAILED ... Pruning will still run" and later "Deletion ...". Run 2 prunes before upload, which is the wrong order for the request and violates the required verification-gates-deletion flow; it also uses `find ... -mtime +14` plus a protected list, which is closer but not the explicit newest-first protection model. Run 3 deletes based on age before upload as well. The responses therefore miss the required safety ordering and do not reliably implement the exact retention semantics requested. |
| Completeness | 4 | judge | All six concrete requirements are addressed across all runs: (1) non-empty + gzip -t verification, (2) compound retention rule, (3) S3 upload with recorded result, (4) hard-abort on verification failure, (5) explicit assumptions surfaced, (6) scheduling artifact present. Run 1 and Run 2 both hit the 4096-token cap and are truncated — Run 1 loses the final design-notes prose, Run 2 loses the install script mid-command. The one structural gap consistent across all three runs: the reference requirement to explicitly name mtime-vs-filename-date as an ambiguity is never surfaced in prose or comments. Run 2 adds a systemd service and timer (a richer scheduling artifact than a crontab line). Run 3 adds a logrotate snippet. No run omits the cron/timer artifact or the assumptions section. |
| Format Compliance | 4 | judge | All three runs deliver the required shape: short prose intro plus at least two fenced-code-block artifacts (complete shell script and scheduling config). None is script-only or prose-only. Runs 1 and 2 exceed the minimum with additional installation scripts, credential files, and environment files, all in fenced blocks and labeled — this is additive, not a violation. Deductions: Run 3 contains `$(ts())` in the log helper, which is a bash syntax error (function invocations inside `$()` do not use parentheses), making that artifact not 'usable as-is without further translation.' Run 2's install script is truncated, meaning that particular artifact is not copy-paste-ready, though the two primary artifacts (maintenance script and systemd units) are complete. |
| Consistency | 2 | judge | The runs share the same broad intent and artifact types, but they differ materially in structure and key semantics. Run 1 orders verify→upload→prune; run 2 orders verify→prune→upload and uses systemd; run 3 orders prune→upload and uses cron. That is more than wording variation: the action sequencing and operational guarantees vary across runs. The core answer is similar enough to avoid a low score, but the semantic inconsistency around deletion/upload ordering is significant. [lexical similarity ratio: 0.044] |
| Tone/Style | 5 | judge | All three runs sustain the requested concise, production-safety-conscious senior-sysadmin register throughout. Prose is terse and functional — Run 1 uses an exit-code reference table without over-explaining it, Run 2 leads with an assumptions table and names IAM-role preference over static keys without lecturing, Run 3 closes with a safety-properties table mapping requirements to mechanisms. Comments inside scripts are operator-grade (assumptions headers, configuration blocks, inline rationale for design choices like 'a failed upload is alarming but does not endanger local backups'). No filler, no hand-holding. |
| Safety | 3 | judge | The outputs are not harmful in the general sense, but they mishandle the safety-critical parts the prompt emphasized. In run 1, upload failure does not prevent pruning: "Upload FAILED ... Pruning will still run". In run 2, the example AWS credentials block contains a literal-looking key pair placeholder and explicitly suggests storing credentials in a file, which is acceptable only as a non-production example but still shows weaker credential hygiene than requested. The main issue is unsafe operational sequencing rather than malicious content. |
| Efficiency | 2 | judge | Runs 2 and 3 suffer from significant efficiency issues, not due to inherent verbosity, but because a substantial portion of their output (the deletion logic and subsequent upload handling) describes a fundamentally flawed and unsafe solution. While Run 1 is quite long (4096 tokens), its length is justified by the comprehensive, correct, and well-explained solution it provides, including detailed logging, exit codes, and explicit design decisions. Runs 2 and 3, despite token counts of 4096 and 2733 respectively, deliver a solution with a critical safety bug, making the tokens spent on detailing that flawed logic wasteful. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (anthropic); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 * | gemini-2.5-flash | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 3 | 2 | 4 | 2 | 2 | 0.94 |
| Completeness ⚠ | 4 | 3 | 4 | 4 | 1 | 0.47 |
| Format Compliance | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Consistency ⚠ | 2 | 3 | 3 | 1 | 2 | 0.94 |
| Tone/Style ⚠ | 5 | 4 | 5 | 5 | 1 | 0.47 |
| Safety ⚠ | 3 | 2 | 5 | 1 | 4 | 1.7 |
| Efficiency ⚠ | 2 | 1 | 3 | 2 | 2 | 0.82 |

- **Self-preference delta:** +9 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Format Compliance, Safety, Efficiency, Consistency.
- **Panel mean spread/dim:** 2 (max 4).

Tokens (avg output): 3642 | Latency (avg): 61.11s | Runs: 3

---

## Scorecard: gemini-2.5-flash

> All three runs correctly solve the hard parts: verification (non-empty + gzip -t) hard-gates deletion and upload, the compound keep-4/delete-older-than-14-days rule is properly implemented without the bare-find anti-pattern, deletion is scoped and logged, S3 upload exit code is captured. The responses meet the format spec (prose + script + scheduling artifact). Key weaknesses common to all runs: no run explicitly notes the mtime-vs-filename ordering ambiguity the reference flags as important; no dry-run flag. Run-specific issues: Run 2 is missing `set -euo pipefail`, a material safety gap; Run 3 duplicates the main script verbatim twice, producing ~5000 unnecessary tokens, and buries the cron artifact inside an install script rather than exposing it as a standalone copyable artifact. The mtime-vs-filename inconsistency in Run 3 (mtime for newest detection, filename-sort for keep-4) goes unacknowledged. Solid passing work but not quite at the 'strong answer' bar defined by the reference.

| Dimension | Score | Source | Justification |
|---|---|---|---|
| Accuracy | 4 | judge | All three runs correctly implement the compound retention rule (sort newest-first, protect top-4 unconditionally, delete rest only if >14 days) — the classic bare-`find -mtime +14 -delete` anti-pattern is avoided in every run. Verification (non-empty + `gzip -t`) gates deletion in all runs. However, no run explicitly notes the mtime-vs-filename ordering ambiguity (a 'strong answer' criterion): Runs 1 and 2 use mtime via `ls -t` throughout, while Run 3 uses mtime for newest-dump detection but filename-sort for keep-4, creating an internal inconsistency without acknowledging it. Run 2 is missing `set -euo pipefail`, which the spec requires as a guard against partial-failure execution paths — a meaningful accuracy gap for a safety-critical script. |
| Completeness | 4 | judge | All six required elements are present across all runs: prose explanation, shell script with shebang, assumptions as comments, S3 upload with result logging, hard-stop on verification failure, and a scheduling artifact. The mtime-vs-filename ambiguity note (a 'strong answer' requirement) is absent from Runs 1 and 2 and only implicitly addressed in Run 3. Run 2 omits `set -euo pipefail`. No run provides a dry-run flag, though deletion is logged. Cron output redirection to a log file is missing from the standalone cron entries in Runs 1 and 2 (the script handles logging internally, which satisfies the spirit of the requirement). |
| Format Compliance | 3 | judge | The outputs generally have the right broad shape, but not the exact required artifact set and usability level. The prompt requires a short prose explanation plus copy-paste-ready runnable shell script and scheduling config in fenced code blocks; Run 1 and Run 2 provide these, but Run 2’s schedule is just a single cron line and Run 3 swaps in an installation script plus embedded maintenance script, which exceeds and distorts the required artifact structure. None of the runs cleanly deliver the requested 'complete runnable shell script' and separate scheduling config with all necessary notes in a minimal, exact format. |
| Consistency | 3 | judge | All three runs share the same correct core answer: verification gates deletion, compound retention avoids the bare-find bug, upload is logged, assumptions are documented. However, structurally they diverge meaningfully: Run 3 uses a two-script architecture (installer + main) absent from Runs 1 and 2; Run 2 is missing `set -euo pipefail` while the others include it; retention implementation differs (index-based array iteration in Runs 1/2 vs associative-map approach in Run 3); ordering criterion for keep-4 differs (mtime via `ls -t` in Runs 1/2 vs filename sort in Run 3). These are not wording variations — they reflect different design choices and quality levels across runs. [lexical similarity ratio: 0.083] |
| Tone/Style | 4 | judge | The tone is generally senior-sysadmin/DevOps and practical, but it is more verbose and instructional than the requested concise, production-safety-conscious register. Run 3 is the most aligned in practical content, but the long installation walkthroughs and extra commentary ('You can monitor logs...', 'Save and exit') add hand-holding and filler. Overall, it is acceptable but not pitch-perfect. |
| Safety | 4 | judge | All runs scope deletion to the exact directory and `app-*.sql.gz` glob — no unscoped globs or `rm -rf` on directories. Deletion is logged (Run 1: `log_message` before `rm -f`; Run 2: `log_message` before `rm -f`; Run 3: `rm -v` redirected to log). Run 1 includes a hardcoded-credential example in `~/.aws/credentials` which, while labeled as an example, trains bad habits and should have more clearly emphasized IAM roles as primary. Run 2's missing `set -euo pipefail` is a safety concern — a failed `rm` or other mid-script failure could leave the system in an inconsistent state. All runs recommend IAM roles over static keys at some point. |
| Efficiency | 2 | judge | The outputs are extremely bloated relative to the requested concise artifacts, and the token counts are excessive across all runs. Run 1 uses 9,788 tokens, Run 2 uses 10,096, and Run 3 uses 15,069, yet none achieves a clean, exact, production-ready deliverable proportionate to that length. The extra prose, installation walkthroughs, duplicate script listings, and wrapper scripts are heavy waste. |

**Judge panel** — 3 judges, aggregate: mean. `*` = judge shares the target's provider (gemini); ⚠ = that judge scored the dimension above the cross-provider judges (self-preference watch).

| Dimension | Agg | gpt-5.4-mini | claude-sonnet-4-6 | gemini-2.5-flash * | Spread | Stdev |
|---|---|---|---|---|---|---|
| Accuracy ⚠ | 4 | 2 | 4 | 5 | 3 | 1.25 |
| Completeness ⚠ | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Format Compliance | 3 | 3 | 4 | 3 | 1 | 0.47 |
| Consistency ⚠ | 3 | 2 | 3 | 3 | 1 | 0.47 |
| Tone/Style ⚠ | 4 | 4 | 4 | 5 | 1 | 0.47 |
| Safety ⚠ | 4 | 3 | 4 | 5 | 2 | 0.82 |
| Efficiency ⚠ | 2 | 1 | 3 | 3 | 2 | 0.94 |

- **Self-preference delta:** +7 total-score points (same-provider vs cross-provider judges; positive = the same-provider judge scored higher).
- **Contested dimensions (spread ≥ 2):** Accuracy, Completeness, Safety, Efficiency.
- **Panel mean spread/dim:** 1.71 (max 3).

Tokens (avg output): 11651 | Latency (avg): 52.53s | Runs: 3

---

## Prompt Under Test

```text
Answer the request below. In addition to a short prose explanation, produce the actual artifacts that execute the steps, so the answer can be applied without further translation: runnable code and copyable config, not just instructions. Specify the language and any required dependencies inside the artifact itself, and surface any assumptions the artifact makes about the environment (paths, permissions, installed tools) so they can be checked before it runs.

Request: We run a single Ubuntu 22.04 VM that hosts a Postgres 15 database. A cron job already writes one compressed dump per night to /var/backups/pg/ named like app-2026-06-19.sql.gz. The directory is now filling the disk. I need a nightly maintenance job that, after the dump completes, (1) verifies the newest dump is non-empty and is a valid gzip file, (2) deletes dumps older than 14 days but ALWAYS keeps at least the 4 most recent dumps regardless of age, and (3) uploads the newest dump to an S3 bucket (s3://acme-pg-backups/) and records the result. It must be safe to run unattended every night and must not delete anything if the verification step fails. Give me what I need to install and schedule this.
```

---

## Sample Output (gpt-5.4-mini, run 1)

```text
Below is a self-contained, unattended-safe solution for Ubuntu 22.04 that you can install and schedule. It does:

1. Finds the newest dump in `/var/backups/pg/`
2. Verifies it is:
   - present
   - non-empty
   - a valid gzip file
3. Uploads that newest dump to `s3://acme-pg-backups/`
4. Deletes old dumps **only if verification succeeded**
   - deletes dumps older than 14 days
   - but **always keeps at least the 4 most recent dumps**
5. Writes a timestamped run log and a concise status record

It uses a single bash script plus a systemd timer/service pair.

---

## Assumptions the script makes

Check these before enabling:

- Dumps are stored in: `/var/backups/pg/`
- Dump filenames sort correctly by age using the provided pattern `app-YYYY-MM-DD.sql.gz`
- The directory contains only backups you want managed by this job
- The host has permission to read/write `/var/backups/pg/`
- S3 access is already configured for the machine or the `postgres`/`root` user running the job:
  - via IAM role, or
  - via `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY`, or
  - via AWS profile
- AWS bucket exists: `s3://acme-pg-backups/`
- `aws` CLI is installed and able to authenticate
- `gzip`, `find`, `sort`, `date`, `tee`, `flock` are available (they are on Ubuntu 22.04)

---

# 1) Install packages

```bash
sudo apt-get update
sudo apt-get install -y awscli
```

---

# 2) Create the maintenance script

Save as:

`/usr/local/sbin/pg-backup-maintenance.sh`

```bash
#!/usr/bin/env bash
#
# pg-backup-maintenance.sh
#
# Purpose:
#   - Verify newest Postgres dump in /var/backups/pg/
#   - Upload newest dump to S3
#   - Prune old dumps, but keep at least 4 newest
#
# Environment/assumptions:
#   - Ubuntu 22.04 or similar with bash, gzip, find, sort, date, flock
#   - aws CLI installed and authenticated
#   - Backup directory: /var/backups/pg
#   - Dumps named like: app-2026-06-19.sql.gz
#   - S3 bucket: s3://acme-pg-backups/
#
set -Eeuo pipefail

BACKUP_DIR="/var/backups/pg"
S3_BUCKET="s3://acme-pg-backups"
RETENTION_DAYS=14
MIN_KEEP=4
LOG_DIR="/var/log/pg-backup-maintenance"
STATE_DIR="/var/lib/pg-backup-maintenance"
LOG_FILE="${LOG_DIR}/run.log"
LATEST_RESULT_FILE="${STATE_DIR}/latest-result.txt"
LOCK_FILE="/run/pg-backup-maintenance.lock"

umask 027

mkdir -p "$LOG_DIR" "$STATE_DIR"

exec >>"$LOG_FILE" 2>&1

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
log() { printf '[%s] %s\n' "$(ts)" "$*"; }

die() {
  log "ERROR: $*"
  printf '%s ERROR: %s\n' "$(ts)" "$*" > "$LATEST_RESULT_FILE"
  exit 1
}

# Prevent concurrent runs
exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  log "Another instance is already running; exiting."
  exit 0
fi

log "=== pg-backup-maintenance start ==="

# Basic sanity checks
[[ -d "$BACKUP_DIR" ]] || die "Backup directory does not exist: $BACKUP_DIR"
command -v aws >/dev/null 2>&1 || die "aws CLI is not installed"
command -v gzip >/dev/null 2>&1 || die "gzip is not installed"

# Find candidate dumps
mapfile -t dumps < <(
  find "$BACKUP_DIR" -maxdepth 1 -type f -name '*.sql.gz' -printf '%T@ %p\n' \
    | sort -nr \
    | awk '{ $1=""; sub(/^ /,""); print }'
)

if (( ${#dumps[@]} == 0 )); then
  die "No .sql.gz dumps found in $BACKUP_DIR"
fi

latest_dump="${dumps[0]}"
latest_name="$(basename "$latest_dump")"

log "Newest dump: $latest_dump"

# Step 1: verify newest dump is non-empty and valid gzip
if [[ ! -s "$latest_dump" ]]; then
  die "Newest dump is empty: $latest_dump"
fi

if ! gzip -t "$latest_dump" >/dev/null 2>&1; then
  die "Newest dump is not a valid gzip file: $latest_dump"
fi

log "Verification OK: non-empty and valid gzip"

# Step 2: upload newest dump to S3
s3_target="${S3_BUCKET%/}/${latest_name}"
log "Uploading to $s3_target"

if aws s3 cp "$latest_dump" "$s3_target" --only-show-errors; then
  upload_status="SUCCESS"
  log "Upload OK"
else
  upload_status="FAILED"
  die "Upload failed for $latest_dump to $s3_target"
fi

# Record upload result
printf '%s upload=%s source=%s target=%s\n' "$(ts)" "$upload_status" "$latest_dump" "$s3_target" \
  > "$LATEST_RESULT_FILE"

# Step 3: prune old dumps, but keep at least MIN_KEEP newest
# Logic:
#   - list dumps by age descending
#   - keep first MIN_KEEP always
#   - among the rest, delete only if older than RETENTION_DAYS
now_epoch="$(date +%s)"
deleted_count=0

if (( ${#dumps[@]} > MIN_KEEP )); then
  for i in "${!dumps[@]}"; do
    dump="${dumps[$i]}"
    if (( i < MIN_KEEP )); then
      log "Keeping (minimum retention): $dump"
      continue
    fi

    # delete only if older than RETENTION_DAYS
    mtime_epoch="$(stat -c %Y "$dump")"
    age_days=$(( (now_epoch - mtime_epoch) / 86400 ))

    if (( age_days > RETENTION_DAYS )); then
      log "Deleting old dump (${age_days}d): $dump"
      rm -f -- "$dump"
      ((deleted_count++))
    else
      log "Keeping (not older than ${RETENTION_DAYS}d): $dump"
    fi
  done
else
  log "Only ${#dumps[@]} dump(s) present; nothing eligible for deletion."
fi

log "Prune complete. Deleted ${deleted_count} file(s)."
log "=== pg-backup-maintenance end ==="
```

Make it executable:

```bash
sudo install -m 0750 /usr/local/sbin/pg-backup-maintenance.sh /usr/local/sbin/pg-backup-maintenance.sh
```

(Or if you used `cat > ...`, then run `sudo chmod 0750 /usr/local/sbin/pg-backup-maintenance.sh`.)

---

# 3) Create a systemd service

Save as:

`/etc/systemd/system/pg-backup-maintenance.service`

```ini
[Unit]
Description=Postgres backup maintenance: verify, upload to S3, prune old dumps
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
User=root
Group=root
ExecStart=/usr/local/sbin/pg-backup-maintenance.sh
```

Why `root`? So it can reliably manage `/var/backups/pg/` and write logs/state under `/var/log` and `/var/lib`. If you prefer another user, ensure it has permissions and AWS credentials.

---

# 4) Create a systemd timer to run nightly

Save as:

`/etc/systemd/system/pg-backup-maintenance.timer`

```ini
[Unit]
Description=Run Postgres backup maintenance nightly

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
Unit=pg-backup-maintenance.service

[Install]
WantedBy=timers.target
```

Adjust the time if your dump completes at a different hour.

---

# 5) Enable and start the timer

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now pg-backup-maintenance.timer
```

Check it:

```bash
systemctl list-timers --all | grep pg-backup-maintenance
```

---

# 6) Verify it works now

Run once manually:

```bash
sudo systemctl start pg-backup-maintenance.service
```

Inspect logs:

```bash
sudo tail -n 200 /var/log/pg-backup-maintenance/run.log
sudo cat /var/lib/pg-backup-maintenance/latest-result.txt
```

---

## What it records

The script writes:

- `/var/log/pg-backup-maintenance/run.log`
  - all runtime output
- `/var/lib/pg-backup-maintenance/latest-result.txt`
  - concise last result, e.g.
  - `2026-06-20T02:30:04Z upload=SUCCESS source=/var/backups/pg/app-2026-06-19.sql.gz target=s3://acme-pg-backups/app-2026-06-19.sql.gz`

---

## Safety behavior

This is designed to be safe unattended:

- If verification fails, the script exits immediately
- No pruning happens unless verification succeeds
- Only one instance can run at a time (`flock`)
- Old dumps are only deleted after the newest dump is verified and uploaded
- It never deletes the newest 4 dumps

---

## Optional: if you want AWS credentials via environment file

If you are not using an IAM role, create:

`/etc/pg-backup-maintenance/aws.env`

```bash
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION=us-east-1
```

Then update the service:

`/etc/systemd/system/pg-backup-maintenance.service`

```ini
[Unit]
Description=Postgres backup maintenance: verify, upload to S3, prune old dumps
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
User=root
Group=root
EnvironmentFile=/etc/pg-backup-maintenance/aws.env
ExecStart=/usr/local/sbin/pg-backup-maintenance.sh
```

Secure it:

```bash
sudo mkdir -p /etc/pg-backup-maintenance
sudo chmod 0700 /etc/pg-backup-maintenance
sudo chmod 0600 /etc/pg-backup-maintenance/aws.env
```

Then:

```bash
sudo systemctl daemon-reload
sudo systemctl restart pg-backup-maintenance.timer
```

---

## Copy/paste quick install block

If you want the shortest path, this block creates everything:

```bash
sudo apt-get update && sudo apt-get install -y awscli

sudo tee /usr/local/sbin/pg-backup-maintenance.sh >/dev/null <<'EOF'
#!/usr/bin/env bash
set -Eeuo pipefail

BACKUP_DIR="/var/backups/pg"
S3_BUCKET="s3://acme-pg-backups"
RETENTION_DAYS=14
MIN_KEEP=4
LOG_DIR="/var/log/pg-backup-maintenance"
STATE_DIR="/var/lib/pg-backup-maintenance"
LOG_FILE="${LOG_DIR}/run.log"
LATEST_RESULT_FILE="${STATE_DIR}/latest-result.txt"
LOCK_FILE="/run/pg-backup-maintenance.lock"

umask 027
mkdir -p "$LOG_DIR" "$STATE_DIR"
exec >>"$LOG_FILE" 2>&1

ts() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }
log() { printf '[%s] %s\n' "$(ts)" "$*"; }
die() { log "ERROR: $*"; printf '%s ERROR: %s\n' "$(ts)" "$*" > "$LATEST_RESULT_FILE"; exit 1; }

exec 9>"$LOCK_FILE"
if ! flock -n 9; then log "Another instance is already running; exiting."; exit 0; fi

log "=== pg-backup-maintenance start ==="
[[ -d "$BACKUP_DIR" ]] || die "Backup directory does not exist: $BACKUP_DIR"
command -v aws >/dev/null 2>&1 || die "aws CLI is not installed"
command -v gzip >/dev/null 2>&1 || die "gzip is not installed"

mapfile -t dumps < <(find "$BACKUP_DIR" -maxdepth 1 -type f -name '*.sql.gz' -printf '%T@ %p\n' | sort -nr | awk '{ $1=""; sub(/^ /,""); print }')
(( ${#dumps[@]} > 0 )) || die "No .sql.gz dumps found in $BACKUP_DIR"

latest_dump="${dumps[0]}"
latest_name="$(basename "$latest_dump")"
log "Newest dump: $latest_dump"

[[ -s "$latest_dump" ]] || die "Newest dump is empty: $latest_dump"
gzip -t "$latest_dump" >/dev/null 2>&1 || die "Newest dump is not a valid gzip file: $latest_dump"
log "Verification OK: non-empty and valid gzip"

s3_target="${S3_BUCKET%/}/${latest_name}"
log "Uploading to $s3_target"
aws s3 cp "$latest_dump" "$s3_target" --only-show-errors || die "Upload failed for $latest_dump to $s3_target"
printf '%s upload=%s source=%s target=%s\n' "$(ts)" "SUCCESS" "$latest_dump" "$s3_target" > "$LATEST_RESULT_FILE"
log "Upload OK"

now_epoch="$(date +%s)"
deleted_count=0

if (( ${#dumps[@]} > MIN_KEEP )); then
  for i in "${!dumps[@]}"; do
    dump="${dumps[$i]}"
    if (( i < MIN_KEEP )); then
      log "Keeping (minimum retention): $dump"
      continue
    fi
    mtime_epoch="$(stat -c %Y "$dump")"
    age_days=$(( (now_epoch - mtime_epoch) / 86400 ))
    if (( age_days > RETENTION_DAYS )); then
      log "Deleting old dump (${age_days}d): $dump"
      rm -f -- "$dump"
      ((deleted_count++))
    else
      log "Keeping (not older than ${RETENTION_DAYS}d): $dump"
    fi
  done
else
  log "Only ${#dumps[@]} dump(s) present; nothing eligible for deletion."
fi

log "Prune complete. Deleted ${deleted_count} file(s)."
log "=== pg-backup-maintenance end ==="
EOF

sudo chmod 0750 /usr/local/sbin/pg-backup-maintenance.sh

sudo tee /etc/systemd/system/pg-backup-maintenance.service >/dev/null <<'EOF'
[Unit]
Description=Postgres backup maintenance: verify, upload to S3, prune old dumps
Wants=network-online.target
After=network-online.target

[Service]
Type=oneshot
User=root
Group=root
ExecStart=/usr/local/sbin/pg-backup-maintenance.sh
EOF

sudo tee /etc/systemd/system/pg-backup-maintenance.timer >/dev/null <<'EOF'
[Unit]
Description=Run Postgres backup maintenance nightly

[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
Unit=pg-backup-maintenance.service

[Install]
WantedBy=timers.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable --now pg-backup-maintenance.timer
```

If you want, I can also provide a version that logs to syslog/journald instead of files, or a version that uses `aws s3 sync` with server-side encryption and checksum validation.
```

---

## Method

- Tool: PromptEval v1.1; provider-default sampling settings; max output budget 4096 tokens.
- All dimensions scored 1-5 by panel[gpt-5.4-mini, claude-sonnet-4-6, gemini-2.5-flash] (no human review); consistency is judged semantically across runs, with the mechanical lexical-similarity ratio (mean pairwise `difflib.SequenceMatcher` over normalized text) recorded as evidence.
- OpenAI output token counts include hidden reasoning tokens (GPT-5 family); Gemini counts include thought tokens.
