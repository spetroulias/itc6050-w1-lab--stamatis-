-- models/stg_github_issues.sql
SELECT
    id              AS issue_id,
    number          AS issue_number,
    title,
    state,
    user__login     AS author,
    comments,
    created_at,
    updated_at,
    closed_at,
    EXTRACT(EPOCH FROM (
        COALESCE(closed_at, NOW()) - created_at
    )) / 86400      AS days_open
FROM raw.github_issues