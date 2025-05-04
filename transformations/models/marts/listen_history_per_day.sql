with
    source as (
        select COUNT(*) as listen_count, date(played_at) as date
        from {{ ref("stg_listen_history") }}
        GROUP BY date(played_at)
    )

select *
from source