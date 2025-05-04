with
    source as (
        select *
        from {{ source("spotify_data", "listen_history") }}
    )

select *
from source